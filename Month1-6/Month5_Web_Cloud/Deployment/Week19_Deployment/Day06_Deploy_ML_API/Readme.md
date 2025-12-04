
# **📌 Day 6 — Deploying a Full ML API (FastAPI + Model) on Railway**


# **🎯 Day 6 Goals**

Tumhare TODAY ke clear goals:

* Local ML API banana (FastAPI + pickle model)
* Requirements.txt + Procfile (Railway ke liye required)
* Railway par new project create karna
* Repo connect → deploy → verify
* Live URL test karna

---

# **📂 Recommended Folder Structure**

```
Day06_Deploy_ML_API/
│── app/
│   ├── __init__.py
│   ├── main.py
│   ├── model.pkl
│   └── predictor.py
│
├── requirements.txt
└── Procfile
```

---

# **🧠 Step-by-Step Workflow**

### **1) Train a simple model (local)**

Example: Iris dataset
Pickle file save kar do:

```python
import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

X, y = load_iris(return_X_y=True)
clf = RandomForestClassifier().fit(X, y)

pickle.dump(clf, open("model.pkl", "wb"))
```

---

### **2) predictor.py**

```python
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

def predict_flower(data):
    arr = np.array(data).reshape(1, -1)
    return int(model.predict(arr)[0])
```

---

### **3) main.py (FastAPI)**

```python
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
```

---

### **4) requirements.txt**

Railway tabhi build karega jab dependencies sahi hon:

```
fastapi
uvicorn
numpy
scikit-learn
```

---

### **5) Procfile**

Railway ko batata hai run kya karna hai:

```
web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

# **🌐 Deployment on Railway**

### **Step 1 — Go to Railway**

[https://railway.app](https://railway.app)
Login via GitHub.

---

### **Step 2 — Create New Project**

**→ Deploy from GitHub Repo**

Tum GitHub Desktop use karte ho, so steps:

1. Apni folder ko GitHub Desktop me open
2. New private repo bana do
3. “Push origin”
4. Railway → “New Project” → “Deploy from GitHub repo”

---

### **Step 3 — Railway Build Process**

* Automatically Python detect ho jata hai
* Uvicorn command Procfile se read hoti hai
* Dependencies install hoti hain
* Deploy ho jata hai

---

### **Step 4 — Test the API**

Railway tumhe ek **Production URL** dega:

Example:
`https://ml-api-production.up.railway.app/predict`

Request test via Postman:

JSON body:

```json
[5.1, 3.5, 1.4, 0.2]
```

Output:

```json
{"prediction": 0}
```

---
