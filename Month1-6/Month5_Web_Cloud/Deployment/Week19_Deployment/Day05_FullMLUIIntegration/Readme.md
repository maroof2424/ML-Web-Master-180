
# 📘 **Day 5 — (Full ML UI + FastAPI Integration)**

## 🎯 **Goal of Day 5**

Aaj hum complete flow ready karte hain:

**HTML Form → JavaScript → Fetch API → FastAPI Backend → ML Prediction → Result UI**

Yeh foundational skill hai jo aapko full ML Web Apps banane mein help karegi.

---

## 📁 **Folder Structure**

```
Day05_FullMLUIIntegration/
│── index.html
│── style.css
└── script.js
```

---

## 📝 **1. index.html**

Simple UI jisme user inputs deta hai:

* Pregnancies
* Glucose
* Blood Pressure
* BMI
* Age

Aur ek button → *Predict*

UI styling simple rakhi hai taake baad mein aap Tailwind/Bootstrap par upgrade kar sako.

---

## 🎨 **2. style.css**

Basic styling:

* Form alignment
* Button styling
* Loader hide/show
* Output colors
* Clean modern card UI

Yeh CSS minimal hai—sirf UX smooth banane ke liye.

---

## 🧠 **3. script.js — Complete Logic**

### Yeh JavaScript 4 kaam karta hai:

#### ✓ **1. Inputs read karna**

`document.getElementById("...").value`

#### ✓ **2. Validation**

Agar koi field empty ho → user ko friendly message milta hai.

#### ✓ **3. Loader show karna**

Prediction aane tak → “Predicting...” show hota hai.

#### ✓ **4. Fetch API se backend hit karna**

POST request:

```js
fetch("https://your-backend.herokuapp.com/predict", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
})
```

#### ✓ **5. Result display**

* `Diabetic` → red
* `Not Diabetic` → green

#### ✓ **6. Error Handling**

Agar backend down/internet issue:

```
Error: Could not connect to backend!
```

---

## 🔗 **Backend API Requirement**

Tumhara FastAPI backend ye endpoint provide karta ho:

```
POST /predict
```

Body example:

```json
{
  "pregnancies": 2,
  "glucose": 120,
  "bp": 70,
  "bmi": 25,
  "age": 33
}
```

Response:

```json
{"prediction": 1}
```

or

```json
{"prediction": 0}
```

---

## 🧪 **How to Test**

### Step 1 — Local

1. FastAPI run karo
2. Browser mein `index.html` open karo
3. Inputs enter → Predict

### Step 2 — Deployed Backend

`script.js` ke andar:

```
https://your-backend.herokuapp.com/predict
```

→ isko apne backend URL se replace karo.

---
