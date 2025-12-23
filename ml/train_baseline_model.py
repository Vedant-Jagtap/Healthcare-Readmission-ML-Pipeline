import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

BASE_DIR = Path(__file__).resolve().parent.parent
ML_DIR = BASE_DIR / "ml"

DATA_FILE = ML_DIR / "ml_dataset.csv"


def train_baseline():
    # Load ML dataset
    df = pd.read_csv(DATA_FILE)

    # Split features and target
    X = df.drop(columns=["readmitted_30_days"])
    y = df["readmitted_30_days"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Train Logistic Regression
    model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)

    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluation
    print("\n--- BASELINE MODEL RESULTS (LOGISTIC REGRESSION) ---")
    print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
        # Feature importance (coefficients)
    importance = pd.DataFrame({
        "feature": X.columns,
        "coefficient": model.coef_[0]
    }).sort_values(by="coefficient", ascending=False)

    print("\n--- FEATURE IMPORTANCE (LOGISTIC REGRESSION) ---")
    print(importance)
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

def train_random_forest(X_train, X_test, y_train, y_test):
    rf = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        class_weight="balanced",
        random_state=42
    )

    rf.fit(X_train, y_train)

    y_pred = rf.predict(X_test)
    y_proba = rf.predict_proba(X_test)[:, 1]

    print("\n--- RANDOM FOREST RESULTS ---")
    print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
    print("ROC-AUC:", round(roc_auc_score(y_test, y_proba), 4))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # Feature importance
    importance = pd.DataFrame({
        "feature": X_train.columns,
        "importance": rf.feature_importances_
    }).sort_values(by="importance", ascending=False)

    print("\n--- FEATURE IMPORTANCE (RANDOM FOREST) ---")
    print(importance)
if __name__ == "__main__":
    # Load ML dataset
    df = pd.read_csv(DATA_FILE)

    X = df.drop(columns=["readmitted_30_days"])
    y = df["readmitted_30_days"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Logistic Regression (balanced)
    model = LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("\n--- LOGISTIC REGRESSION (BALANCED) ---")
    print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    # Random Forest
    train_random_forest(X_train, X_test, y_train, y_test)
