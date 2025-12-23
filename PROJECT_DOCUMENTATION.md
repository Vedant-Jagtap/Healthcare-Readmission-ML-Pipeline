\# End-to-End Healthcare Data Pipeline with ML-Based Readmission Risk Prediction



\## 1. Introduction



Healthcare systems generate large volumes of heterogeneous data such as patient demographics, hospital visits, and diagnosis records. Efficiently processing this data and extracting actionable insights is critical for improving patient outcomes and optimizing hospital resources.



This project implements an \*\*end-to-end healthcare data pipeline\*\* followed by a \*\*machine learning system\*\* to predict the risk of hospital readmission within 30 days. The system follows industry-style data engineering practices and produces analytics-ready data for modeling and inference.



---



\## 2. Project Objectives



\- Build a scalable data pipeline using layered architecture (Bronze, Silver, Gold)

\- Clean, validate, and standardize raw healthcare data

\- Design an analytics-ready star schema

\- Perform exploratory analytics and KPI generation

\- Train and evaluate machine learning models for readmission prediction

\- Save the trained model and enable inference on new patient data



---



\## 3. Dataset Description



The project uses multiple healthcare datasets representing different aspects of hospital data:



\### 3.1 Patient Demographics

Contains patient-level attributes such as:

\- Age

\- Gender

\- Blood type

\- Medical condition

\- Insurance provider



\### 3.2 Hospital Visits

Contains visit-level information such as:

\- Admission date

\- Discharge date

\- Length of stay

\- Readmission indicator (target variable)



\### 3.3 Diagnosis Data

Contains clinical indicators related to heart disease, including:

\- Chest pain type

\- Severity indicators

\- Heart disease outcome



These datasets are intentionally heterogeneous to simulate real-world hospital data systems.



---



\## 4. System Architecture Overview



The system follows a \*\*layered data architecture\*\*:



Bronze Layer → Silver Layer → Gold Layer → Analytics \& ML



Each layer has a well-defined responsibility, ensuring data quality, traceability, and scalability.



---



\## 5. Data Pipeline Design



\### 5.1 Bronze Layer (Raw Data)



\- Stores raw CSV files exactly as received

\- No cleaning or transformations

\- Ensures data lineage and auditability



\### 5.2 Silver Layer (Cleaned \& Standardized Data)



\- Handles missing values and invalid records

\- Standardizes column names and formats

\- Applies domain-specific cleaning rules

\- Produces clean datasets ready for analytics



Silver datasets:

\- patients\_clean.csv

\- visits\_clean.csv

\- diagnosis\_clean.csv



\### 5.3 Gold Layer (Analytics-Ready Data)



The Gold layer is modeled using a \*\*star schema\*\*:



\#### Dimension Tables

\- dim\_patient

\- dim\_diagnosis



\#### Fact Table

\- fact\_patient\_visits



This layer supports efficient analytics, ML feature extraction, and business reporting.



---



\## 6. Data Validation \& Quality Checks



To ensure correctness, the pipeline includes:

\- Row count verification

\- Null value checks

\- Foreign key integrity validation

\- Logical consistency checks



Sanity checks confirm that the Gold layer is reliable and ready for downstream use.



---



\## 7. Exploratory Analytics \& KPIs



Basic analytics were performed on the Gold layer to extract insights such as:

\- Total number of hospital visits

\- Average length of stay

\- Readmission rate

\- Severity-wise visit distribution



These KPIs validate the usefulness of the processed data.



---



\## 8. Machine Learning Pipeline



\### 8.1 ML Dataset Preparation



The ML dataset is created by joining Gold-layer tables and selecting relevant features:



Features used:

\- Age

\- Gender

\- Severity level

\- Length of stay

\- Heart disease indicator



Target variable:

\- Readmitted within 30 days (binary)



Categorical features are encoded, and the dataset is cleaned for modeling.



---



\## 9. Model Training \& Evaluation



\### 9.1 Baseline Model – Logistic Regression



\- Logistic Regression used as baseline

\- Class imbalance handled using class weights

\- Evaluation performed using confusion matrix and recall



\### 9.2 Random Forest Model



\- Non-linear model to capture feature interactions

\- Improved overall accuracy and ROC-AUC

\- Feature importance extracted for interpretability



---



\## 10. Model Interpretability



Feature importance analysis revealed that:

\- Length of stay is the strongest predictor

\- Age significantly influences readmission risk

\- Disease severity and heart condition contribute to risk



This aligns with real-world clinical expectations.



---



\## 11. Model Saving \& Inference



The final Random Forest model is saved using `joblib` and reused for inference.



The inference pipeline:

\- Loads the trained model

\- Accepts new patient data

\- Returns readmission prediction and probability



This enables real-world deployment readiness.



---



\## 12. Current Project Status



✔ Data pipeline implemented  

✔ Analytics validated  

✔ Machine learning models trained and evaluated  

✔ Model saved for inference  



---



\## 13. Future Enhancements



The following extensions are planned:

\- REST API using FastAPI for real-time prediction

\- Interactive dashboard for analytics visualization

\- Threshold tuning for optimized recall

\- Model monitoring and retraining strategies



