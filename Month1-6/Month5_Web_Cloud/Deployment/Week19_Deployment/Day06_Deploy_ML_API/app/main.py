from fastapi import FastAPI
from predictor import predict_flower

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ML Model API Working!"}

@app.post("/predict")
def predict(data: list):
    result = predict_flower(data)
    return {"prediction": result}
