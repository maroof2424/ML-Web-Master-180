# Day 3 – Flexbox & Grid

Today I learned how to structure the layout using Flexbox and Grid for ML dashboards.

## ✔ What I Learned Today

* Flexbox: horizontal and vertical alignment
* Grid: 2D layouts with columns and rows
* Combining Flex and Grid for dashboard layout
* Styling cards and forms
* Using `flex-wrap` and `gap` for responsive layout

---

## 📄 Mini Project: ML Result Dashboard

* Left side: ML input form
* Right side: Result cards displayed in grid layout
* Flexbox used for main dashboard layout
* Grid used for result cards

---

## 🧠 Key Concepts

### 🔹 Flexbox for form + dashboard container

```
.dashboard {
    display: flex;
    gap: 30px;
    flex-wrap: wrap;
}
```

### 🔹 Grid for results cards

```
.results-grid {
    display: grid;
    grid-template-columns: repeat(2, 150px);
    gap: 20px;
}
```

### 🔹 Card styling

```
.card {
    background: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    text-align: center;
}
```

---

