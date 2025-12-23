import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SILVER_DIR = BASE_DIR / "data" / "silver"
GOLD_DIR = BASE_DIR / "data" / "gold"

VISITS_FILE = SILVER_DIR / "visits_clean.csv"
PATIENT_DIM = GOLD_DIR / "dim_patient.csv"
DIAG_DIM = GOLD_DIR / "dim_diagnosis.csv"
OUTPUT_FILE = GOLD_DIR / "fact_patient_visits.csv"


def build_fact_visits():
    visits = pd.read_csv(VISITS_FILE)
    patients = pd.read_csv(PATIENT_DIM)
    diagnosis = pd.read_csv(DIAG_DIM)

    # Create surrogate joins (row-based mapping)
    visits = visits.reset_index(drop=True)
    patients = patients.reset_index(drop=True)
    diagnosis = diagnosis.reset_index(drop=True)

    visits["patient_id"] = visits.index % len(patients) + 1
    visits["diagnosis_id"] = visits.index % len(diagnosis) + 1

    # Select final fact columns
    fact = visits[
        [
            "visit_id",
            "patient_id",
            "diagnosis_id",
            "admission_date",
            "discharge_date",
            "length_of_stay",
            "readmitted_30_days"
        ]
    ]

    # Save to gold layer
    GOLD_DIR.mkdir(exist_ok=True)
    fact.to_csv(OUTPUT_FILE, index=False)

    print("fact_patient_visits built successfully.")
    print("Rows:", fact.shape[0])


if __name__ == "__main__":
    build_fact_visits()
