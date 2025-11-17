# Day 2 – Forms & Buttons

Aaj ka focus simple tha: HTML form banana, uske inputs ko samajhna, aur unko basic CSS se style karna.

## ✔ What I Learned Today

* Form ka basic structure
* Labels ka role and best practice (label + input pairing)
* Input types (number, text, email, password)
* Required attributes
* Submit & Reset buttons
* Form ko center karna using flexbox
* Transparent background using `rgba()` instead of `opacity`

---

## 📄 Mini Project: ML Input Form

A simple diabetes predictor style form containing:

* Age
* Weight
* Glucose Level
* BMI
* Insulin

Buttons:

* **Submit**
* **Clear**

---

## 🧠 Key Concepts

### 🔹 Form Structure

```
<form>
  <label>Age:</label>
  <input type="number">

  <button type="submit">Submit</button>
</form>
```

### 🔹 Transparent Background (Correct Way)

```
background: rgba(255, 255, 255, 0.5);
```

### 🔹 Centering Form

```
display: flex;
justify-content: center;
padding-top: 40px;
```

---
