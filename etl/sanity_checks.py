import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
GOLD_DIR = BASE_DIR / "data" / "gold"

PATIENTS = GOLD_DIR / "dim_patient.csv"
DIAGNOSIS = GOLD_DIR / "dim_diagnosis.csv"
FACT = GOLD_DIR / "fact_patient_visits.csv"


def sanity_checks():
    patients = pd.read_csv(PATIENTS)
    diagnosis = pd.read_csv(DIAGNOSIS)
    fact = pd.read_csv(FACT)

    print("\n--- ROW COUNTS ---")
    print("Patients:", patients.shape[0])
    print("Diagnosis:", diagnosis.shape[0])
    print("Visits (Fact):", fact.shape[0])

    print("\n--- NULL CHECKS (FACT TABLE) ---")
    print(fact.isnull().sum())

    print("\n--- FOREIGN KEY CHECKS ---")
    invalid_patients = fact[~fact["patient_id"].isin(patients["patient_id"])]
    invalid_diagnosis = fact[~fact["diagnosis_id"].isin(diagnosis["diagnosis_id"])]

    print("Invalid patient_id rows:", invalid_patients.shape[0])
    print("Invalid diagnosis_id rows:", invalid_diagnosis.shape[0])

    assert invalid_patients.shape[0] == 0
    assert invalid_diagnosis.shape[0] == 0

    print("\nSanity checks PASSED ✅")


if __name__ == "__main__":
    sanity_checks()
