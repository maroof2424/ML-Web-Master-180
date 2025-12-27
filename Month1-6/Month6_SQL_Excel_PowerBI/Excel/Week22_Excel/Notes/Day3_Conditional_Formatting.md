s# **Day 3 – Conditional Formatting (Concept & Guide)**

## **Objective**

Use **visual rules** to highlight important insights in data **without writing complex formulas**.

👉 Goal is:
**“Let Excel show patterns automatically”**

---

## **1️⃣ What is Conditional Formatting?**

### Concept

Conditional Formatting changes **cell appearance** (color, icon, bars) **based on conditions**.

Example:

* High sales → Green
* Low sales → Red
* Negative profit → Highlighted

📌 Instead of *reading numbers*, you *see insights*.

---

## **2️⃣ Why It’s Important (Industry Perspective)**

* Used heavily in **dashboards**
* Makes reports **executive-friendly**
* Helps detect:

  * Outliers
  * Trends
  * Risk areas
  * Top / Bottom performers

👉 Analysts who know Conditional Formatting = faster insights.

---

## **3️⃣ Demo Data (Use This First)**

Paste this in Excel:

| Product    | Region | Sales | Profit |
| ---------- | ------ | ----- | ------ |
| Laptop     | North  | 1200  | 300    |
| Mouse      | South  | 200   | -20    |
| Chair      | East   | 450   | 80     |
| Desk       | West   | 800   | 150    |
| Headphones | North  | 600   | -50    |

---

## **4️⃣ Basic Conditional Formatting Rules**

### A) Highlight Cells Greater Than

**Task:** Highlight Sales > 700

**Steps:**

1. Select **Sales column**
2. Home → Conditional Formatting
3. Highlight Cells Rules → Greater Than
4. Enter `700`
5. Choose Green Fill

📌 Use case: High-performing products

---

### B) Highlight Negative Values

**Task:** Highlight Profit < 0

**Steps:**

1. Select **Profit column**
2. Conditional Formatting → Highlight Cells Rules
3. Less Than → `0`
4. Choose Red Fill

📌 Use case: Loss detection

---

## **5️⃣ Color Scales (Trend Visualization)**

### Concept

Color scales show **relative performance**.

**Steps:**

1. Select Sales column
2. Conditional Formatting → Color Scales
3. Choose Green–Yellow–Red

📌 Higher sales = darker green
📌 Lower sales = red

Best for **trend spotting**, not exact values.

---

## **6️⃣ Data Bars (Quick Comparison)**

### Concept

Adds horizontal bars inside cells.

**Steps:**

1. Select Sales
2. Conditional Formatting → Data Bars

📌 Great for:

* Comparing values
* Compact dashboards

---

## **7️⃣ Formula-Based Conditional Formatting (MOST IMPORTANT)**

### Concept

Apply formatting using **custom logic**.

### Example: Highlight Loss Products

**Condition:** Profit < 0

**Formula Rule:**

```excel
=D2<0
```

(D2 = first profit cell)

**Steps:**

1. Select full table
2. Conditional Formatting → New Rule
3. Use a formula
4. Enter formula
5. Apply Red Fill

📌 This is how **real dashboards** are built.

---

## **8️⃣ Real-World Scenarios**

| Scenario           | Rule           |
| ------------------ | -------------- |
| Sales below target | `< target`     |
| Profit margin low  | `< 10%`        |
| Top performers     | `Top 10%`      |
| Risk customers     | Custom formula |

---

## **9️⃣ Best Practices (Very Important)**

✅ Keep colors meaningful (Red = bad, Green = good)
✅ Avoid too many colors
✅ Prefer formula-based rules
❌ Don’t over-format (noise)

---

## **Key Takeaways**

* Conditional Formatting = Visual analytics
* Faster insights than raw numbers
* Formula-based rules are powerful
* Essential for dashboards & reports

---
