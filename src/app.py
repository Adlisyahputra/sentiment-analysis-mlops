from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import sys
import os

sys.path.append(os.path.dirname(__file__))
from preprocessing import clean_text

app = FastAPI(title="Sentiment Analysis API", version="1.0")

model_path = os.path.join(os.path.dirname(__file__), "..", "models", "sentiment_pipeline.joblib")
pipeline = joblib.load(model_path)

class ReviewInput(BaseModel):
    text: str

class PredictionOutput(BaseModel):
    text: str
    clean_text: str
    sentiment: str
    confidence: float

@app.get("/")
def root():
    return {"message": "Sentiment Analysis API aktif. Kirim POST ke /predict"}

@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: ReviewInput):
    cleaned = clean_text(input_data.text)
    prediction = pipeline.predict([cleaned])[0]
    probabilities = pipeline.predict_proba([cleaned])[0]
    confidence = max(probabilities)

    return PredictionOutput(
        text=input_data.text,
        clean_text=cleaned,
        sentiment=prediction,
        confidence=round(float(confidence), 4)
    )