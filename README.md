## 🏥 Healthcare Readmission Prediction & Analytics Platform

An **end-to-end healthcare data analytics and machine learning project** that builds a full pipeline from raw data ingestion to interactive dashboards and real-time ML predictions via an API and frontend.

---

## 🚀 Project Overview

Hospital readmissions are a critical indicator of healthcare quality and operational efficiency.
This project analyzes patient visit data to:

* Understand **readmission patterns**
* Identify **high-risk patient groups**
* Predict **30-day readmission risk** using machine learning
* Provide **interactive dashboards** and a **live prediction interface**

The project follows **industry-style architecture**, separating analytics, ML, and deployment layers.

---

## 🧱 Architecture (High Level)

```
Raw Data
   ↓
Bronze Layer (Raw CSVs)
   ↓
Silver Layer (Cleaned & Validated Data)
   ↓
Gold Layer (Fact & Dimension Tables)
   ↓
-------------------------------------
| Analytics (Power BI Dashboard)     |
| Machine Learning Models            |
| FastAPI Inference Service          |
| Web Frontend (HTML + JS)           |
-------------------------------------
```

---

## 📂 Project Structure

```
healthcare-data-pipeline/
│
├── data/
│   ├── bronze/        # Raw data
│   ├── silver/        # Cleaned data
│   └── gold/          # Fact & dimension tables
│
├── etl/               # Data cleaning & transformations
├── ml/                # Model training & inference
│
├── api.py             # FastAPI ML inference API
├── dashboard.py       # Streamlit analytics dashboard
├── index.html         # Simple frontend for predictions
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📊 Analytics Dashboard (Power BI)

A **professional, enterprise-style Power BI dashboard** built on the Gold layer.

### Key Insights Provided:

* Overall **Readmission Rate**
* Readmission by **Severity Level**
* **Average Length of Stay** analysis
* Distribution of **Readmitted vs Non-Readmitted visits**
* Interactive filters (severity, readmission status, gender)

📌 The dashboard follows **star schema modeling** and uses **DAX measures** for KPIs.



## 🤖 Machine Learning

### Problem Statement

Predict whether a patient will be **readmitted within 30 days**.

### Models Implemented

* Logistic Regression (baseline & class-balanced)
* Random Forest (final model)

### Key Features

* Age
* Gender
* Severity Level
* Length of Stay
* Heart Disease indicator

### Model Highlights

* Handled class imbalance
* Feature importance analysis
* Saved trained model for inference
* Evaluated using accuracy, recall, ROC-AUC

---

## 🚀 Deployment & Inference

### 🔹 FastAPI

* `/predict` endpoint for real-time inference
* JSON input → prediction + probability
* CORS enabled for frontend integration

### 🔹 Frontend

* Simple **HTML + JavaScript** interface
* Form-based input
* Displays:

  * Prediction (Readmitted / Not Readmitted)
  * Probability
  * Risk level (Low / Medium / High)

---

## 🛠️ Technologies Used

| Category         | Tools               |
| ---------------- | ------------------- |
| Data Processing  | Python, Pandas      |
| Data Modeling    | Star Schema         |
| Analytics        | Power BI            |
| Machine Learning | scikit-learn        |
| Visualization    | Power BI, Streamlit |
| API              | FastAPI             |
| Frontend         | HTML, JavaScript    |
| Version Control  | Git, GitHub         |

---

## ▶️ How to Run Locally

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run API

```bash
python -m uvicorn api:app --reload
```

### 3️⃣ Run Streamlit dashboard

```bash
python -m streamlit run dashboard.py
```

### 4️⃣ Open frontend

Open `index.html` in a browser.

---

## 🎯 Key Learning Outcomes

* Built a **production-style data pipeline**
* Designed **enterprise analytics dashboards**
* Trained & evaluated ML models on real data
* Deployed ML models via API
* Integrated analytics, ML, and frontend systems
* Used Git & GitHub for version control

---

## 📌 Future Enhancements

* Time-series readmission analysis
* Model monitoring & retraining
* SQL-based warehouse (PostgreSQL / BigQuery)
* Authentication for API
* Cloud deployment (AWS / GCP)

---

## 👤 Author

**Vedant Jagtap**
B.Tech (AI & Data Science)
Healthcare Analytics & Machine Learning Project

---

## ⭐ If you find this project useful

Feel free to ⭐ the repository or connect with me on GitHub.

---
