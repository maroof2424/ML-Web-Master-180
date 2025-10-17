from fastapi import FastAPI
from .routes import router as predict_router


app = FastAPI(title="ML Model API")

app.include_router(predict_router)

@app.get("/")
def root():
    return {"message":"Wellcome to ML Model API!..."}