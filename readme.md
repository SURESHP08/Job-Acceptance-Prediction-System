HR Job Placement Analytics & Prediction Dashboard
=================================================

📌 Project Overview
-------------------

This project is an end-to-end data science solution designed to help HR departments analyze candidate data and predict job placement success. It combines a rigorous **Machine Learning pipeline** with an **interactive Streamlit dashboard** to provide actionable insights into hiring trends, candidate performance, and placement probability.

🚀 Features
-----------

*   **Data Cleaning & Preprocessing:** Handles missing values (median/mode imputation), removes duplicates, and standardizes categorical text.
    
*   **Advanced Feature Engineering:** - Academic\_Band: Categorizes candidates based on aggregate scores (SSC, HSC, Degree).
    
    *   Interview\_Score: Combines technical, aptitude, and communication scores.
        
    *   Experience\_Category: Segments candidates into Fresher, Junior, and Senior levels.
        
    *   Skills\_Match\_Level: Categorizes the alignment between candidate skills and job requirements.
        
*   **Predictive Modeling:** - Implements **Logistic Regression** and **Random Forest** classifiers.
    
    *   Includes a full preprocessing pipeline using ColumnTransformer and StandardScaler.
        
    *   Evaluates performance using Accuracy, ROC-AUC, and Classification Reports.
        
*   **Interactive Dashboard:** - Real-time KPI tracking (Placement Rate, Avg Interview Score, etc.).
    
    *   Visual analysis of Dropout Rates and Relocation Willingness.
        
    *   Feature importance and correlation heatmaps.
        

🛠️ Tech Stack
--------------

*   **Language:** Python
    
*   **Libraries:** Pandas, NumPy, Scikit-Learn
    
*   **Visualization:** Matplotlib, Seaborn
    
*   **Web Framework:** Streamlit
    

📊 Dataset Description
----------------------

The model utilizes the HR\_Job\_Placement\_Dataset.csv, which includes:

*   **Demographics:** Age, Gender.
    
*   **Academic Scores:** SSC, HSC, and Degree percentages.
    
*   **Technical Skills:** Technical score, Aptitude score, Communication score, and Skills match percentage.
    
*   **Experience:** Years of experience, Internship experience, and Certifications.
    
*   **Placement Status:** Target variable (Placed / Not Placed).
    

⚙️ Installation & Setup
-----------------------

1.  Bashgit clone https://github.com/your-username/hr-placement-dashboard.gitcd hr-placement-dashboard
    
2.  Bashpip install -r requirements.txt_(Ensure your requirements.txt includes: pandas, numpy, matplotlib, seaborn, scikit-learn, and streamlit)_
    
3.  **Prepare the data:**Ensure HR\_Job\_Placement\_Dataset.csv is in the root directory.
    

🖥️ How to Run
--------------

### 1\. Run the Analysis & ML Model

To train the models and see the initial analysis:

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python analysis_script.py   `

### 2\. Launch the Dashboard

To start the interactive Streamlit interface:

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   streamlit run app.py   `

📈 Key Insights from the Dashboard
----------------------------------

*   **Placement Rate:** Overall percentage of candidates successfully placed.
    
*   **Interview Performance:** Correlation between technical scores and final placement.
    
*   **Dropout Analysis:** Visualization of candidates who were not placed or dropped out of the funnel.
    
*   **Experience Impact:** How different experience levels affect hiring outcomes.