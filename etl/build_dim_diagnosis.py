import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SILVER_DIR = BASE_DIR / "data" / "silver"
GOLD_DIR = BASE_DIR / "data" / "gold"

INPUT_FILE = SILVER_DIR / "diagnosis_clean.csv"
OUTPUT_FILE = GOLD_DIR / "dim_diagnosis.csv"


def build_dim_diagnosis():
    df = pd.read_csv(INPUT_FILE)

    # Select diagnosis-related attributes
    df = df[
        [
            "chest_pain_type",
            "severity_level",
            "heart_disease"
        ]
    ]

    # Remove duplicates
    df = df.drop_duplicates().reset_index(drop=True)

    # Create surrogate diagnosis_id
    df.insert(0, "diagnosis_id", df.index + 1)

    # Save to gold layer
    GOLD_DIR.mkdir(exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    print("dim_diagnosis built successfully.")
    print("Rows:", df.shape[0])


if __name__ == "__main__":
    build_dim_diagnosis()
