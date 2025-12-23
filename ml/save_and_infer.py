import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
ML_DIR = BASE_DIR / "ml"

DATA_FILE = ML_DIR / "ml_dataset.csv"
MODEL_FILE = ML_DIR / "readmission_model.pkl"


def train_and_save_model():
    # Load dataset
    df = pd.read_csv(DATA_FILE)

    X = df.drop(columns=["readmitted_30_days"])
    y = df["readmitted_30_days"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Train Random Forest
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        class_weight="balanced",
        random_state=42
    )

    model.fit(X_train, y_train)

    # Save model
    joblib.dump(model, MODEL_FILE)

    print("Model trained and saved successfully.")
    print("Saved at:", MODEL_FILE)


def load_and_predict(sample):
    # Load model
    model = joblib.load(MODEL_FILE)

    # Convert sample to DataFrame
    sample_df = pd.DataFrame([sample])

    # Predict
    prediction = model.predict(sample_df)[0]
    probability = model.predict_proba(sample_df)[0][1]

    return prediction, probability


if __name__ == "__main__":
    train_and_save_model()

    # Example inference
    sample_patient = {
        "age": 65,
        "gender": 1,              # female=1, male=0
        "severity_level": 2,      # high=2, medium=1, low=0
        "length_of_stay": 7,
        "heart_disease": 1
    }

    pred, prob = load_and_predict(sample_patient)

    print("\n--- INFERENCE RESULT ---")
    print("Predicted Readmission:", pred)
    print("Readmission Probability:", round(prob, 3))
