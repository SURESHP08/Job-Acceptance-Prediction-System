# -------------------------------
# KPI Calculations (REFINED)
# -------------------------------
total_candidates = len(df)

if total_candidates > 0:
    # Placement Rate (Acceptance)
    placement_rate = df["status"].mean() * 100
    job_acceptance_rate = placement_rate
    
    # Offer Dropout Rate: (Total - Placed) / Total * 100
    # This represents candidates who did not result in a '1' (Placed) status
    offer_dropout_rate = (1 - df["status"].mean()) * 100
    
    avg_interview_score = df["Interview_Score"].mean()
    avg_skills_match = df["Skills_Match_Percentage"].mean()
    high_risk_percentage = df["High_Risk"].mean() * 100
else:
    placement_rate = job_acceptance_rate = offer_dropout_rate = 0
    avg_interview_score = avg_skills_match = high_risk_percentage = 0

# -------------------------------
# Display KPIs (Existing layout)
# -------------------------------
col1, col2, col3 = st.columns(3)
col1.metric("👥 Total Candidates", f"{total_candidates:,}")
col2.metric("📈 Placement Rate (%)", f"{placement_rate:.2f}%")
col3.metric("✅ Job Acceptance Rate (%)", f"{job_acceptance_rate:.2f}%")

col4, col5, col6 = st.columns(3)
col4.metric("🎤 Avg Interview Score", f"{avg_interview_score:.2f}")
col5.metric("💡 Avg Skills Match (%)", f"{avg_skills_match:.2f}%")
col6.metric("⚠️ Offer Dropout Rate (%)", f"{offer_dropout_rate:.2f}%", delta=f"-{offer_dropout_rate:.1f}%", delta_color="inverse")

st.markdown("---")

# -------------------------------
# New Visualization: Dropout Analysis
# -------------------------------
st.subheader("📊 Dropout & Risk Analysis")

c1, c2 = st.columns(2)

with c1:
    st.write("### Placement vs. Dropout Distribution")
    # Creating a pie chart for visual clarity on dropouts
    dropout_counts = df['status'].value_counts().rename(index={1: 'Placed', 0: 'Dropped Out'})
    fig2, ax2 = plt.subplots()
    ax2.pie(dropout_counts, labels=dropout_counts.index, autopct='%1.1f%%', colors=['#2ecc71', '#e74c3c'], startangle=90)
    ax2.axis('equal') 
    st.pyplot(fig2)

with c2:
    if "relocation_willingness" in df.columns:
        st.write("### Dropout Rate by Relocation Willingness")
        # Calculating dropout rate per category
        reloc_dropout = df.groupby("relocation_willingness")["status"].apply(lambda x: (1 - x.mean()) * 100)
        st.bar_chart(reloc_dropout)

# ... [Rest of your existing charts: Skills Match, Experience, Correlation] ...