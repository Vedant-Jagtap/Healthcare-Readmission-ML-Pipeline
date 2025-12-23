import pandas as pd
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
BRONZE_DIR = BASE_DIR / "data" / "bronze"
SILVER_DIR = BASE_DIR / "data" / "silver"

INPUT_FILE = BRONZE_DIR / "patients_raw.csv"
OUTPUT_FILE = SILVER_DIR / "patients_clean.csv"


def clean_patients():
    df = pd.read_csv(INPUT_FILE)

    # Standardize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Remove duplicate patients
    if "patient_id" in df.columns:
        df = df.drop_duplicates(subset="patient_id")
    else:
        df = df.drop_duplicates()

    # Age cleaning
    if "age" in df.columns:
        df = df[(df["age"] > 0) & (df["age"] < 120)]

    # Gender standardization
    if "gender" in df.columns:
        df["gender"] = df["gender"].astype(str).str.lower()
        df["gender"] = df["gender"].replace({
            "m": "male",
            "f": "female"
        })
        df["gender"] = df["gender"].fillna("other")

    # Region handling
    if "region" in df.columns:
        df["region"] = df["region"].fillna("unknown")

    # Final validation
    if "patient_id" in df.columns:
        assert df["patient_id"].isnull().sum() == 0

    # Save to silver layer
    SILVER_DIR.mkdir(exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    print("Patients data cleaned and saved to Silver layer.")
    print("Rows after cleaning:", df.shape[0])


if __name__ == "__main__":
    clean_patients()
