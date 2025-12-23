import streamlit as st
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(page_title="Healthcare Readmission Dashboard", layout="wide")

# Paths
BASE_DIR = Path(__file__).resolve().parent
GOLD_DIR = BASE_DIR / "data" / "gold"

FACT = GOLD_DIR / "fact_patient_visits.csv"
PATIENTS = GOLD_DIR / "dim_patient.csv"
DIAGNOSIS = GOLD_DIR / "dim_diagnosis.csv"

# Load data
fact = pd.read_csv(FACT)
patients = pd.read_csv(PATIENTS)
diagnosis = pd.read_csv(DIAGNOSIS)

st.title("🏥 Healthcare Readmission Dashboard")

# ---------------- KPI SECTION ----------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Patients", patients.shape[0])
col2.metric("Total Visits", fact.shape[0])
col3.metric(
    "Readmission Rate",
    f"{round(fact['readmitted_30_days'].mean()*100, 2)} %"
)

# ---------------- READMISSION DISTRIBUTION ----------------
st.subheader("🔁 Readmission Distribution")

fig1, ax1 = plt.subplots()
fact["readmitted_30_days"].value_counts().plot(
    kind="bar",
    ax=ax1
)
ax1.set_xticklabels(["Not Readmitted", "Readmitted"], rotation=0)
ax1.set_ylabel("Count")
st.pyplot(fig1)

# ---------------- SEVERITY VS READMISSION ----------------
st.subheader("⚠️ Severity vs Readmission")

merged = fact.merge(diagnosis, on="diagnosis_id")

fig2, ax2 = plt.subplots()
sns.countplot(
    data=merged,
    x="severity_level",
    hue="readmitted_30_days",
    ax=ax2
)
ax2.set_xlabel("Severity Level")
ax2.set_ylabel("Count")
ax2.legend(title="Readmitted")
st.pyplot(fig2)

# ---------------- LENGTH OF STAY ----------------
st.subheader("🛏️ Length of Stay Analysis")

fig3, ax3 = plt.subplots()
sns.boxplot(
    data=merged,
    x="severity_level",
    y="length_of_stay",
    ax=ax3
)
ax3.set_xlabel("Severity Level")
ax3.set_ylabel("Length of Stay (days)")
st.pyplot(fig3)
