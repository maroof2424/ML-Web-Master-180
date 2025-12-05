from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("model.pkl")

class InputData(BaseModel):
    age: int
    bmi: float
    glucose: float

@app.get("/")
def home():
    return {"message": "ML Model API Running Successfully!"}

@app.post("/predict")
def predict(data: InputData):
    values = [[data.age, data.bmi, data.glucose]]
    prediction = model.predict(values)[0]
    return {"prediction": int(prediction)}