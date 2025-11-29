
# Day 7 — ML UI + FastAPI Integration

This is the final mini-project of **Week 18** (JavaScript + API Fetching).  
Aaj tumne complete pipeline build ki:

**HTML Form → JavaScript → FastAPI → ML Model → Result UI**

Is project ke baad tum real-world ML web apps build kar sakte ho.

---

## 🎯 What This Project Does

- User se 8 medical inputs leta hai  
- JavaScript un values ko collect karta hai  
- JSON format mein FastAPI ko POST karta hai  
- FastAPI trained ML model ko use karke prediction deta hai  
- JS UI result ko card me show karta hai:  
  - **Diabetic 😔**  
  - **Not Diabetic 😄**

Smooth loader, clean UI, proper error handling — everything included.

---

## 📁 Folder Structure

```

Day07_ML_UI_Integration/
│── index.html      # Diabetes form UI
│── style.css       # Loader + result card + basic UI styling
│── script.js       # API call + loader + result handling
└── README.md

```

---

## 🚀 How to Run the Project

### 1️⃣ Start FastAPI Backend

Your FastAPI `main.py` should contain a prediction endpoint:

```

POST /predict

````

Run server:

```bash
uvicorn main:app --reload
````

FastAPI must be available at:

```
http://127.0.0.1:8000/predict
```

---

### 2️⃣ Open Frontend

Simply open:

```
index.html
```

Chrome/Edge/Firefox sab chalega.

---

## 📦 Data Sent to FastAPI

JavaScript yeh body send karta hai:

```json
{
  "pregnancies": 2,
  "glucose": 130,
  "bp": 72,
  "skin": 20,
  "insulin": 85,
  "bmi": 28.5,
  "dpf": 0.35,
  "age": 33
}
```

Backend must return:

```json
{
  "prediction": 0
}
```

(0 = Not Diabetic, 1 = Diabetic)

---

## 💡 Features You Built

* ✔ HTML form with 8 inputs
* ✔ Input → JS value extraction
* ✔ Loader animation
* ✔ POST request to FastAPI
* ✔ JSON handling
* ✔ Error messages
* ✔ Beautiful result card
* ✔ Clean and simple UX

Real-world polish — exactly what companies expect.

---

## 🧠 Concepts Covered

* DOM form handling
* `fetch()` POST request
* Async/await
* Error handling (`try/catch`)
* Loader show/hide pattern
* UI update based on API response

---
