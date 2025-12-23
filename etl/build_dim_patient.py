import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SILVER_DIR = BASE_DIR / "data" / "silver"
GOLD_DIR = BASE_DIR / "data" / "gold"

INPUT_FILE = SILVER_DIR / "patients_clean.csv"
OUTPUT_FILE = GOLD_DIR / "dim_patient.csv"


def build_dim_patient():
    df = pd.read_csv(INPUT_FILE)

    # Select core patient identity columns
    df = df[
        [
            "name",
            "age",
            "gender",
            "blood_type",
            "medical_condition",
            "insurance_provider"
        ]
    ]

    # Remove duplicates (same patient profile)
    df = df.drop_duplicates().reset_index(drop=True)

    # Create surrogate patient_id
    df.insert(0, "patient_id", df.index + 1)

    # Save to gold layer
    GOLD_DIR.mkdir(exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    print("dim_patient built successfully.")
    print("Rows:", df.shape[0])


if __name__ == "__main__":
    build_dim_patient()
