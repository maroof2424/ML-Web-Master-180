
# 🧠 Week 12 – FastAPI Basics + ML Serving

📁 **Directory:** `Month3_ML_DL/Week12_FastAPI`

---

## 🎯 **Goal**

Learn to **serve ML and Deep Learning models** through REST APIs using **FastAPI**.
By the end of this week, you’ll deploy your **trained Scikit-learn or TensorFlow model** as a working backend API that takes JSON input and returns predictions.

---

## 📂 **Project Structure**

```
Month3_ML_DL/
└── Week12_FastAPI/
    ├── app/
    │   ├── main.py              # FastAPI entry point
    │   ├── routes.py            # All routes & endpoints
    │   ├── schemas.py           # Pydantic data models
    │   ├── model.pkl / model.h5 # Trained ML/DL model
    │   └── requirements.txt     # Dependencies
    ├── tests/
    │   └── test_api.py          # Test API endpoints
    ├── README.md
```

---

## 🗓️ **Day Plan**

| Day       | Topic                            | Description                                             |
| --------- | -------------------------------- | ------------------------------------------------------- |
| **Day 1** | **FastAPI Basics**               | Intro to FastAPI, routes, JSON request/response         |
| **Day 2** | **Serve ML Model**               | Load and serve a Scikit-learn Logistic Regression model |
| **Day 3** | **Input Validation (Pydantic)**  | Validate JSON input schemas                             |
| **Day 4** | **Save & Load Model**            | Use `joblib` or `.h5` to persist models                 |
| **Day 5** | **TensorFlow Model Integration** | Serve TensorFlow/Keras ANN via FastAPI                  |
| **Day 6** | **Build ML API (End-to-End)**    | Full pipeline from preprocessing → model → API          |
| **Day 7** | **🎯 Final Project**             | Deploy ML API with FastAPI + TensorFlow model           |

---

## ⚙️ **Setup Instructions**

### 🧩 1. Install Dependencies

```bash
pip install fastapi uvicorn scikit-learn joblib tensorflow
```

Or install from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 🚀 2. Run Server

```bash
uvicorn app.main:app --reload
```

Then open your browser at:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**
(You’ll see the interactive Swagger UI)

---

### 💡 3. Example Endpoint

**POST** `/predict`
**Request Body:**

```json
{
  "age": 35,
  "income": 45000,
  "loan_amount": 12000
}
```

**Response:**

```json
{
  "prediction": 1,
  "message": "Loan Approved ✅"
}
```

---

## 🧠 Concepts Covered

* FastAPI Routing & Request Handling
* Pydantic Models (Input Validation)
* Model Loading (joblib / h5)
* JSON Input → Model Prediction → JSON Output
* TensorFlow ANN Integration
* End-to-End ML API Deployment

---

## 🔥 Final Project Idea (Day 7)

> 🎯 **"Loan Approval Prediction API"**
>
> * Preprocess data using `scikit-learn` pipeline
> * Train & save model as `model.pkl` or `model.h5`
> * Create `/predict` API endpoint
> * Input: JSON payload with applicant details
> * Output: Prediction + Confidence

---

## 🧩 Bonus (Optional)

* Add Swagger documentation & tags
* Deploy to Render / Railway.app
* Use environment variables (`.env`) for model paths

---

## 🏁 Outcome

By the end of Week 12, you will:
✅ Understand how to deploy ML models as APIs
✅ Build scalable REST APIs with FastAPI
✅ Integrate Deep Learning models in production-style apps

---
