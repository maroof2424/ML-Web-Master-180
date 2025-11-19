# 📘 **Day 4 – Bootstrap Basics**

**Folder:** `Week17_WebBasics/Day4_Bootstrap/`
**File:** `bootstrap_demo.html`

---

## 🎯 **Goal of the Day**

Aaj tum Bootstrap ka **core system** samjho ge:

* CDN use karke Bootstrap import karna
* Grid system (container → row → columns)
* Buttons and utilities
* Form design with Bootstrap classes
* Responsive layout

Bootstrap ka kaam simple hai:
👉 *Fast, clean, responsive UI — bina CSS likhe.*

---

## 🧱 **1. What is Bootstrap?**

Bootstrap ek CSS framework hai jo ready-made classes deta hai:

* responsive grid
* buttons
* forms
* spacing utilities
* cards, navbars, alerts

**Tumhe design nahi banana — bas classes lagani hain.**

---

## 🌐 **2. Bootstrap CDN**

Bootstrap ko use karne ka sabse fast tareeqa:

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
```

Is se Bootstrap directly internet se load hota hai —
**no installation required**.

---

## 🏗️ **3. Grid System (Most Important)**

Bootstrap ka layout 12 columns per based hota hai.

```
row → columns (col-*)
```

Example:

```html
<div class="row">
  <div class="col-md-4">Box 1</div>
  <div class="col-md-4">Box 2</div>
  <div class="col-md-4">Box 3</div>
</div>
```

📌 Explanation (simple):

* **col-md-4** = medium screens per 4 column width
* Mobile screens per automatic stacking
* Desktop per 3 boxes side-by-side

---

## 🎨 **4. Buttons**

Bootstrap ready-made button styles deta hai:

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-success">Success</button>
<button class="btn btn-danger">Danger</button>
```

---

## 📝 **5. Forms**

Bootstrap forms super clean hoti hain:

```html
<input type="text" class="form-control" placeholder="Enter name">
```

`form-control` → input ko full width + styling de deta hai.

---

## 📂 **6. Today's Starter File**

Tumhari folder me main file hogi:

`bootstrap_demo.html`

Isme:

* Navbar
* Grid layout
* Buttons
* Form
* Bootstrap stylesheet + JS

Tum is file ko edit karke practice karoge.

---

## 🧪 **7. Your Practice Tasks (Important)**

1. Column boxes me image add karo
2. Ek card component add karo
3. Form me dropdown add karo
4. Buttons ko inline rakho
5. Ek alert add karo (Bootstrap alert class se)

---

## 💡 **8. Best Advice**

Bootstrap sahi lagta tab hai jab tum **structure** clean rakho:

✔ container
✔ row
✔ col
❌ rows ko nested galat mat karo
❌ unnecessary CSS mat likho — Bootstrap pe trust rakho

