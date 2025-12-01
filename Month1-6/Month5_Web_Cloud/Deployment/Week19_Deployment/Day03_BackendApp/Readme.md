
# **Day03_BackendApp**


---

# 🧱 **main.py (FastAPI Example)**

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Week19 FastAPI Backend Demo")

# Example input for prediction
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
```

---

# 📦 **requirements.txt**

```
fastapi
uvicorn
pydantic
```

---

# ⚡ **Procfile** (for Render/Railway deployment)

```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

# ✅ **Run Locally**

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

* Backend will run on `http://127.0.0.1:8000/`
* POST request example: `/predict` with JSON body:

```json
{
  "pregnancies": 2,
  "glucose": 130,
  "bp": 72,
  "bmi": 28.5,
  "age": 33
}
```

Response:

```json
{
  "prediction": 1
}
```

---

