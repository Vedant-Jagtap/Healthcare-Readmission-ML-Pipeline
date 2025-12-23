import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
GOLD_DIR = BASE_DIR / "data" / "gold"
ML_DIR = BASE_DIR / "ml"

FACT = GOLD_DIR / "fact_patient_visits.csv"
PATIENTS = GOLD_DIR / "dim_patient.csv"
DIAGNOSIS = GOLD_DIR / "dim_diagnosis.csv"

OUTPUT_FILE = ML_DIR / "ml_dataset.csv"


def prepare_ml_data():
    # Load gold tables
    fact = pd.read_csv(FACT)
    patients = pd.read_csv(PATIENTS)
    diagnosis = pd.read_csv(DIAGNOSIS)

    # Join fact with dimensions
    df = fact.merge(patients, on="patient_id", how="left")
    df = df.merge(diagnosis, on="diagnosis_id", how="left")

    # Feature selection (ML-safe)
    df_ml = df[
        [
            "age",
            "gender",
            "severity_level",
            "length_of_stay",
            "heart_disease",
            "readmitted_30_days"
        ]
    ]

    # Encode categorical features
    df_ml["gender"] = df_ml["gender"].map(
        {"male": 0, "female": 1}
    )

    df_ml["severity_level"] = df_ml["severity_level"].map(
        {"low": 0, "medium": 1, "high": 2}
    )

    # Drop rows with encoding issues
    df_ml = df_ml.dropna()

    # Save ML dataset
    df_ml.to_csv(OUTPUT_FILE, index=False)

    print("ML dataset prepared successfully.")
    print("Shape:", df_ml.shape)
    print("Target distribution:")
    print(df_ml["readmitted_30_days"].value_counts())


if __name__ == "__main__":
    prepare_ml_data()
