import pandas as pd
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
BRONZE_DIR = BASE_DIR / "data" / "bronze"
SILVER_DIR = BASE_DIR / "data" / "silver"

INPUT_FILE = BRONZE_DIR / "diagnosis_raw.csv"
OUTPUT_FILE = SILVER_DIR / "diagnosis_clean.csv"


def clean_diagnosis():
    df = pd.read_csv(INPUT_FILE)

    # Standardize column names
    df.columns = [c.strip().lower() for c in df.columns]

    # Rename columns
    df = df.rename(columns={
        "sex": "gender",
        "chestpaintype": "chest_pain_type",
        "restingbp": "resting_bp",
        "fastingbs": "fasting_bs",
        "restingecg": "resting_ecg",
        "maxhr": "max_hr",
        "exerciseangina": "exercise_angina",
        "st_slope": "st_slope",
        "heartdisease": "heart_disease"
    })

    # Convert gender
    df["gender"] = df["gender"].map({"M": "male", "F": "female"})

    # Heart disease target
    df["heart_disease"] = df["heart_disease"].astype(int)

    # Severity score (simple medical proxy)
    df["severity_score"] = (
        df["oldpeak"].fillna(0) +
        df["exercise_angina"].map({"Y": 1, "N": 0}) +
        df["st_slope"].map({"Down": 2, "Flat": 1, "Up": 0})
    )

    # Categorize severity
    df["severity_level"] = pd.cut(
        df["severity_score"],
        bins=[-1, 1, 3, 10],
        labels=["low", "medium", "high"]
    )

    # Keep relevant columns
    df = df[
        [
            "age",
            "gender",
            "chest_pain_type",
            "resting_bp",
            "cholesterol",
            "max_hr",
            "heart_disease",
            "severity_level"
        ]
    ]

    # Validation
       # Handle missing values (medical-safe defaults)
    df["cholesterol"] = df["cholesterol"].fillna(df["cholesterol"].median())
    df["resting_bp"] = df["resting_bp"].fillna(df["resting_bp"].median())
    df["max_hr"] = df["max_hr"].fillna(df["max_hr"].median())

    # Final validation (critical columns only)
    # Fix missing severity levels (safe medical default)
    df["severity_level"] = df["severity_level"].fillna("low")

    # Final validation (critical columns only)
    critical_cols = ["age", "gender", "heart_disease", "severity_level"]
    for col in critical_cols:
        assert df[col].isnull().sum() == 0


    # Save to silver layer
    SILVER_DIR.mkdir(exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    print("Diagnosis data cleaned and saved to Silver layer.")
    print("Rows after cleaning:", df.shape[0])


if __name__ == "__main__":
    clean_diagnosis()
