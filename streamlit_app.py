import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="HR Job Placement Dashboard", layout="wide")

# -------------------------------
# Load Dataset
# -------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("HR_Job_Placement_Dataset.csv")

df = load_data()

# -------------------------------
# Basic Cleaning
# -------------------------------
num_cols = df.select_dtypes(include=['int64','float64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

df.drop_duplicates(inplace=True)

# -------------------------------
# Feature Engineering
# -------------------------------
def experience_category(x):
    if x == 0:
        return "Fresher"
    elif x <= 3:
        return "Junior"
    else:
        return "Senior"

df['Experience_Category'] = df['years_of_experience'].apply(experience_category)

df['Academic_Percentage'] = (
    df['ssc_percentage'] +
    df['hsc_percentage'] +
    df['degree_percentage']
) / 3

df['Interview_Score'] = (
    df['technical_score'] +
    df['aptitude_score'] +
    df['communication_score']
) / 3

df["Skills_Match_Level"] = pd.cut(
    df["skills_match_percentage"],
    bins=[0, 50, 75, 100],
    labels=["Low", "Medium", "High"]
)

# Encode target
df['status'] = df['status'].map({'Placed':1, 'Not Placed':0})

# -------------------------------
# Train Model
# -------------------------------
X = df.drop("status", axis=1)
y = df["status"]

categorical_cols = X.select_dtypes(include=['object']).columns
numerical_cols = X.select_dtypes(include=['int64','float64']).columns

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ])

rf_model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=200, random_state=42))
])

rf_model.fit(X, y)

# 🔥 Save training columns
training_columns = X.columns

# -------------------------------
# Dashboard KPIs
# -------------------------------
st.title("📊 HR Job Placement Dashboard")

total_candidates = len(df)
placement_rate = df["status"].mean() * 100
dropout_rate = 100 - placement_rate
avg_interview = df["Interview_Score"].mean()
avg_skills = df["skills_match_percentage"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("👥 Total Candidates", f"{total_candidates:,}")
col2.metric("📈 Placement Rate", f"{placement_rate:.2f}%")
col3.metric("⚠️ Dropout Rate", f"{dropout_rate:.2f}%")

col4, col5 = st.columns(2)
col4.metric("🎤 Avg Interview Score", f"{avg_interview:.2f}")
col5.metric("💡 Avg Skills Match %", f"{avg_skills:.2f}%")

st.markdown("---")

# -------------------------------
# Prediction Section
# -------------------------------
st.header("🤖 Candidate Placement Prediction")

years_of_experience = st.number_input("Years of Experience", 0, 30, 2)
technical_score = st.slider("Technical Score", 0, 100, 70)
aptitude_score = st.slider("Aptitude Score", 0, 100, 65)
communication_score = st.slider("Communication Score", 0, 100, 75)
skills_match_percentage = st.slider("Skills Match %", 0, 100, 80)
company_tier = st.selectbox("Company Tier", df["company_tier"].unique())
gender = st.selectbox("Gender", df["gender"].unique())

# Create base input from first row (SAFE METHOD)
input_data = df.drop("status", axis=1).iloc[0:1].copy()

# Overwrite user fields
input_data["years_of_experience"] = years_of_experience
input_data["technical_score"] = technical_score
input_data["aptitude_score"] = aptitude_score
input_data["communication_score"] = communication_score
input_data["skills_match_percentage"] = skills_match_percentage
input_data["company_tier"] = company_tier
input_data["gender"] = gender

# Recalculate engineered fields
input_data["Experience_Category"] = experience_category(years_of_experience)
input_data["Interview_Score"] = (
    technical_score + aptitude_score + communication_score
) / 3

if st.button("Predict Placement"):

    # Ensure column order matches training
    input_data = input_data.reindex(columns=training_columns)

    prediction = rf_model.predict(input_data)[0]
    probability = rf_model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.success(f"✅ Likely to be Placed (Probability: {probability:.2f})")
    else:
        st.error(f"❌ Likely NOT to be Placed (Probability: {probability:.2f})")