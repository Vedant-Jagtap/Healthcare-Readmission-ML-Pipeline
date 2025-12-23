import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
GOLD_DIR = BASE_DIR / "data" / "gold"

FACT = GOLD_DIR / "fact_patient_visits.csv"
PATIENTS = GOLD_DIR / "dim_patient.csv"
DIAGNOSIS = GOLD_DIR / "dim_diagnosis.csv"


def run_analytics():
    fact = pd.read_csv(FACT)
    patients = pd.read_csv(PATIENTS)
    diagnosis = pd.read_csv(DIAGNOSIS)

    print("\n--- BASIC KPIs ---")
    print("Total Visits:", fact.shape[0])
    print("Total Patients:", patients.shape[0])
    print("Average Length of Stay:", round(fact["length_of_stay"].mean(), 2))

    readmission_rate = fact["readmitted_30_days"].mean() * 100
    print("Readmission Rate (%):", round(readmission_rate, 2))

    print("\n--- VISITS BY SEVERITY ---")
    severity_visits = fact.merge(
        diagnosis,
        on="diagnosis_id",
        how="left"
    ).groupby("severity_level").size()

    print(severity_visits)

    print("\n--- TOP 5 LONGEST STAYS ---")
    longest_stays = fact.sort_values(
        by="length_of_stay",
        ascending=False
    ).head(5)

    print(longest_stays)


if __name__ == "__main__":
    run_analytics()
