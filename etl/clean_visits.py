import pandas as pd
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
BRONZE_DIR = BASE_DIR / "data" / "bronze"
SILVER_DIR = BASE_DIR / "data" / "silver"

INPUT_FILE = BRONZE_DIR / "visits_raw.csv"
OUTPUT_FILE = SILVER_DIR / "visits_clean.csv"


def clean_visits():
    df = pd.read_csv(INPUT_FILE)

    # Standardize column names
    df.columns = [c.strip().lower().replace(" ", "_").replace(".", "") for c in df.columns]

    # Rename important columns
    df = df.rename(columns={
        "sno": "visit_id",
        "mrd_no": "patient_id",
        "doa": "admission_date",
        "dod": "discharge_date",
        "duration_of_stay": "length_of_stay",
        "outcome": "outcome"
    })

    # Remove duplicates
    df = df.drop_duplicates(subset="visit_id")

    # Convert dates
    df["admission_date"] = pd.to_datetime(df["admission_date"], errors="coerce")
    df["discharge_date"] = pd.to_datetime(df["discharge_date"], errors="coerce")

    # Drop invalid dates
    df = df.dropna(subset=["admission_date", "discharge_date"])

    # If length_of_stay missing, calculate it
    if "length_of_stay" not in df.columns or df["length_of_stay"].isnull().all():
        df["length_of_stay"] = (df["discharge_date"] - df["admission_date"]).dt.days

    # Remove invalid stays
    df = df[df["length_of_stay"] > 0]

    # Create readmission proxy (binary target)
    df["readmitted_30_days"] = df["outcome"].astype(str).str.lower().apply(
        lambda x: 0 if "discharge" in x else 1
    )

    # Keep only useful columns for pipeline
    df = df[
        [
            "visit_id",
            "patient_id",
            "admission_date",
            "discharge_date",
            "length_of_stay",
            "readmitted_30_days"
        ]
    ]

    # Validation
    assert df["visit_id"].isnull().sum() == 0
    assert df["patient_id"].isnull().sum() == 0
    assert df["length_of_stay"].min() > 0

    # Save
    SILVER_DIR.mkdir(exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    print("Visits data cleaned and saved to Silver layer.")
    print("Rows after cleaning:", df.shape[0])


if __name__ == "__main__":
    clean_visits()
