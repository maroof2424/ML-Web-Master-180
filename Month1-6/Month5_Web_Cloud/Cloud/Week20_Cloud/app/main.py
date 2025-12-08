from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model.pkl")

class InputData(BaseModel):
    feature1: float
    feature2: float
    feature3: float

@app.post("/predict")
def predict(data: InputData):
    arr = np.array([[data.feature1, data.feature2, data.feature3]])
    pred = model.predict(arr)
    return {"prediction": int(pred[0])}

@app.get("/")
def home():
    return {"status": "backend running!"}
