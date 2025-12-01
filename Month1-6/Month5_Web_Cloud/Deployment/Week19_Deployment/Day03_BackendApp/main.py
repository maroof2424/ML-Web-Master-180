from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Week19 FastAPI Backend Demo")

class InputData(BaseModel):
    pregnancies: int
    glucose: float
    bp: float
    bmi: float
    age: int

@app.post("/predict")
def predict(data: InputData):
    """
    Fake ML prediction logic:
    returns 1 if glucose + bmi + age > 200 else 0
    """
    score = data.glucose + data.bmi + data.age
    prediction = 1 if score > 200 else 0
    return {"prediction": prediction}

@app.get("/")
def root():
    return {"msg": "FastAPI backend is running!"}
