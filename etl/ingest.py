import pandas as pd
from pathlib import Path

# Base path
BASE_DIR = Path(__file__).resolve().parent.parent
BRONZE_DIR = BASE_DIR / "data" / "bronze"

FILES = {
    "patients": "patients_raw.csv",
    "visits": "visits_raw.csv",
    "diagnosis": "diagnosis_raw.csv"
}

def ingest_file(name, filename):
    file_path = BRONZE_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(f"{filename} not found in bronze layer")

    df = pd.read_csv(file_path)
    print(f"\n{name.upper()} DATA")
    print("-" * 40)
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("Column Names:", list(df.columns))

    return df


if __name__ == "__main__":
    for name, file in FILES.items():
        ingest_file(name, file)

    print("\nBronze ingestion check completed successfully.")
