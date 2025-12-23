from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware


# Initialize app
app = FastAPI(title="Healthcare Readmission Prediction API")
# Enable CORS (allow frontend to call API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (OK for local/demo)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Paths
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "ml" / "readmission_model.pkl"

# Load model once at startup
model = joblib.load(MODEL_PATH)

# Request schema
class PatientInput(BaseModel):
    age: int
    gender: int              # male=0, female=1
    severity_level: int      # low=0, medium=1, high=2
    length_of_stay: int
    heart_disease: int       # no=0, yes=1


@app.get("/")
def home():
    return {"message": "Healthcare Readmission Prediction API is running"}


@app.post("/predict")
def predict_readmission(data: PatientInput):
    # Convert input to DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Predict
    prediction = int(model.predict(input_df)[0])
    probability = float(model.predict_proba(input_df)[0][1])

    # Risk label
    if probability >= 0.6:
        risk = "High"
    elif probability >= 0.3:
        risk = "Medium"
    else:
        risk = "Low"

    return {
        "prediction": prediction,
        "readmission_probability": round(probability, 3),
        "risk_level": risk
    }
