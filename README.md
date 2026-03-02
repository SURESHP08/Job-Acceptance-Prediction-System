📊 HR Job Placement & Acceptance Prediction System
==================================================

🚀 Project Overview
-------------------

This project is an end-to-end **HR Analytics & Machine Learning System** designed to analyze candidate placement data and predict job acceptance outcomes.

The system processes 50,000 candidate records, performs data cleaning, feature engineering, exploratory analysis, machine learning modeling, and deploys an interactive Streamlit dashboard for real-time insights and predictions.

The goal is to help recruitment teams:

*   Predict job acceptance probability
    
*   Reduce offer dropouts
    
*   Identify high-risk candidates
    
*   Improve hiring strategies
    
*   Make data-driven recruitment decisions
    

📁 Dataset Description
======================

The dataset contains **50,000 candidate records** and mimics real-world recruitment data.

### 🔎 Features Include:

*   Academic performance (SSC, HSC, Degree %)
    
*   Skills match percentage
    
*   Certifications count
    
*   Years of experience
    
*   Interview scores (Technical, Aptitude, Communication)
    
*   Company tier
    
*   Gender
    
*   Placement status (Target Variable)
    

### ⚠️ Real-World Data Challenges Included:

*   Missing values
    
*   Duplicate-like records
    
*   Inconsistent categorical values
    

🧹 Step 1–3: Data Collection & Cleaning
=======================================

### ✔ Initial Data Checks

*   Dataset shape & size
    
*   Data types validation
    
*   Sample record inspection
    
*   Missing value distribution analysis
    

### ✔ Data Preprocessing

*   Missing values handled (Median for numerical, Mode for categorical)
    
*   Duplicate records removed
    
*   Standardized categorical labels
    
*   Target variable encoding:
    
    *   Placed → 1
        
    *   Not Placed → 0
        
*   Feature scaling using StandardScaler
    
*   One-hot encoding for categorical variables
    

📊 Step 4: Exploratory Data Analysis (EDA)
==========================================

Key business insights analyzed:

*   Interview score vs Job acceptance
    
*   Skills match % impact on placement
    
*   Company tier vs Acceptance rate
    
*   Experience vs Placement probability
    
*   Certification impact
    
*   Correlation matrix analysis
    

Visualizations created using:

*   Matplotlib
    
*   Seaborn
    

🧠 Step 5: Feature Engineering
==============================

Derived analytical features:

### 🔹 Experience Category

*   Fresher (0 years)
    
*   Junior (1–3 years)
    
*   Senior (>3 years)
    

### 🔹 Academic Performance Bands

*   Low
    
*   Medium
    
*   High
    

### 🔹 Skills Match Level

*   Low
    
*   Medium
    
*   High
    

### 🔹 Interview Performance Category

*   Poor
    
*   Average
    
*   Excellent
    

### 🔹 Placement Probability Score

Weighted score based on:

*   Academic %
    
*   Skills Match %
    
*   Interview Score
    
*   Experience Scaling
    

### 🔹 High-Risk Candidate Identification

Candidates with low probability scores flagged as high risk.

🗄 Step 6: Data Storage (Optional)
==================================

*   Cleaned dataset stored in MySQL
    
*   Tables created with proper data types
    
*   Data inserted using SQLAlchemy
    
*   Enables scalable querying & reporting
    

🤖 Step 7: Machine Learning Modeling
====================================

🎯 Target Variable
------------------

*   Placed → 1 (Job Accepted)
    
*   Not Placed → 0 (Job Rejected)
    

🧠 Models Implemented
---------------------

*   Logistic Regression
    
*   Random Forest Classifier
    
*   Decision Tree Classifier
    

📈 Evaluation Metrics
---------------------

*   Accuracy Score
    
*   Classification Report
    
*   ROC-AUC Score
    
*   Confusion Matrix
    
*   Feature Importance Analysis
    

Random Forest achieved strong predictive performance and provided clear feature importance rankings.

📊 Streamlit Dashboard Features
===============================

The interactive dashboard includes:

🔢 Key KPIs
-----------

*   👥 Total Candidates
    
*   📈 Placement Rate (%)
    
*   ✅ Job Acceptance Rate (%)
    
*   🎤 Average Interview Score
    
*   💡 Average Skills Match (%)
    
*   ⚠️ Offer Dropout Rate (%)
    
*   🚨 High-Risk Candidate Percentage
    

📊 Visual Insights
------------------

*   Acceptance Rate by Company Tier
    
*   Skills Match vs Interview Score
    
*   Experience vs Technical Score
    
*   Correlation Heatmap
    

🤖 Live Prediction Module
-------------------------

Users can input:

*   Years of Experience
    
*   Technical Score
    
*   Aptitude Score
    
*   Communication Score
    
*   Skills Match %
    
*   Company Tier
    
*   Gender
    

The model predicts:

*   Placement Outcome
    
*   Probability Score
    

🛠 Tech Stack
=============

CategoryTools UsedProgrammingPythonData AnalysisPandas, NumPyVisualizationMatplotlib, SeabornMachine LearningScikit-learnDashboardStreamlitDatabaseMySQLORMSQLAlchemy

📈 Business Impact
==================

This system enables HR teams to:

*   Identify high-risk candidates early
    
*   Improve placement success rate
    
*   Reduce offer dropouts
    
*   Optimize interview evaluation strategy
    
*   Make data-driven hiring decisions
    
*   Monitor recruitment performance in real time
    

📦 Project Structure
====================

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   HR-Job-Placement-Project/│├── HR_Job_Placement_Dataset.csv├── model_training.py├── app.py (Streamlit Dashboard)├── requirements.txt└── README.md   `

▶️ How to Run the Project
=========================

### 1️⃣ Install Dependencies

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

### 2️⃣ Run Streamlit App

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   streamlit run app.py   `

🎯 Results
==========

*   Cleaned and normalized dataset
    
*   Structured analytical dataset with engineered features
    
*   High-performing machine learning models
    
*   Explainable feature importance
    
*   Interactive HR dashboard
    
*   Actionable recruitment insights
    

📌 Conclusion
=============

This project demonstrates a complete **Data Science lifecycle**:

✔ Data Cleaning✔ Feature Engineering✔ Machine Learning Modeling✔ Model Evaluation✔ Dashboard Deployment✔ Business Insight Generation

It showcases strong skills in data analytics, ML modeling, database integration, and dashboard development.