from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

model = joblib.load("model.pkl")

app = FastAPI()

class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float

@app.post("/predict")
def predict(data: InputData):
    arr = np.array([[data.feature1, data.feature2, data.feature3]])
    pred = model.predict(arr)
    logger.info(f"Received: {data.dict()}")
    return {"prediction": float(pred[0])}

@app.get("/")
def home():
    return {"message": "Backend is live!"}

@app.get("/health")
def health():
    return {"status": "ok"}
