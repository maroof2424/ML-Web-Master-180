

# 🗓️ **Day 4 — Frontend + Backend Integration**

**Goal:**
Aaj tum apni **HTML + JavaScript** UI ko **FastAPI backend** ke saath connect karoge.
Yeh real-world ML apps ka sabse important step hota hai.

---

## ⭐ **Concepts You Learn Today**

### **1. Fetch API (POST Request)**

Frontend se backend ko data bhejna:

* `fetch(url, options)`
* `method: "POST"`
* `headers: { "Content-Type": "application/json" }`
* `body: JSON.stringify(data)`
* `await response.json()` → prediction receive

### **2. Taking Input from Form**

HTML se values read karna using:

* `document.getElementById().value`

### **3. Updating the UI**

Prediction ko:

* `<p id="result">`
  mein display karna

### **4. Error Handling**

Backend down ho → user ko clean error message show karna.

---

## ⭐ **Folder Structure**

```
Day04_FrontendBackendIntegration/
│── index.html       → UI form
│── style.css        → Simple styling
└── script.js        → Fetch API + UI logic
```

---

## ⭐ **Flow of the Entire Day**

### **Step 1: User Inputs**

Form se user data input karta hai:

* pregnancies
* glucose
* bp
* bmi
* age

JS ye values collect karta hai.

---

### **Step 2: Data → Backend (FastAPI)**

JS JSON banata hai:

```js
{
  pregnancies: 2,
  glucose: 123,
  bp: 70,
  bmi: 28,
  age: 35
}
```

Aur fetch API se POST request send karta hai:

```js
await fetch("https://maroofiums.herokuapp.com/predict")
```

---

### **Step 3: Backend Model Predicts**

FastAPI tumhare ML model ko data deta hai →
Model returns:

```json
{"prediction": 1}
```

* `1` → Diabetic
* `0` → Not Diabetic

---

### **Step 4: UI Update**

JS result ko UI par show karta hai:

* Green → Not Diabetic
* Red → Diabetic

---

## ⭐ **Important Notes**

### ✔ Always use `async/await`

Code clean hota hai → samajhna easy.

### ✔ Backend URL change karo after deployment

Temporary localhost:

```
http://127.0.0.1:8000/predict
```

After deployment:

```
https://your-app.herokuapp.com/predict
```

### ✔ CORS errors → common problem

If backend error aaye → first check **CORS settings**.

---

## ⭐ **Mini Task (Today)**

**A complete working system:**

1. Inputs lo
2. JSON banao
3. Backend ko POST request bhejo
4. Prediction ko UI par show karo
5. Error handle karo

*Agar tum ye kar lete ho → tum FASTAPI + JS integration officially samajh gaye.*

---

## ⭐ **Friendly Advice (Important)**

* Data bilkul clean read karo: `Number()` zaroor use karo
* UI ko thoda polish karo → user ko feel acha mile
* Result box ko colors do (green/red) → UX strong hota hai
* Console errors zaroor check karo
* Kabhi bhi API URL hard-code mat rakho future mein → `.env` use karo

---
