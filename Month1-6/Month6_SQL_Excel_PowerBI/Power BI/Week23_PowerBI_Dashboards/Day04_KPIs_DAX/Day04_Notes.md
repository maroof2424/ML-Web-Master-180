# 📅 **Day 4 – KPIs & DAX Measures (Power BI)**

## 🎯 Objective

* KPIs banana (Sales, Profit, Margin)
* **DAX measures** samajhna
* Numbers ko **business meaning** dena

> Rule: *“Columns = data, Measures = logic”*

---

## 🧠 Step 1: What is DAX?

**DAX (Data Analysis Expressions)** = Power BI ka formula language.

### Simple difference:

| Calculated Column       | Measure          |
| ----------------------- | ---------------- |
| Row by row              | Dynamic          |
| Fixed value             | Filter dependent |
| Power Query / Data View | Report View      |

📌 **Best practice:**

> KPIs **hamesha Measure** honi chahiye.

---

## 🧾 Step 2: Create Basic Measures

Go to:
`Report View → Modeling → New Measure`

### 🔹 Total Sales

```DAX
Total Sales = SUM(Sales_Data_Clean[Sales])
```

### 🔹 Total Profit

```DAX
Total Profit = SUM(Sales_Data_Clean[Profit])
```

---

## 📊 Step 3: KPI – Profit Margin

```DAX
Profit Margin = 
DIVIDE(
    [Total Profit],
    [Total Sales],
    0
)
```

📌 `DIVIDE()` use karo → error safe hota hai.

---

## 🎯 Step 4: Sales Target KPI

### Create Target Measure

```DAX
Sales Target = 5000
```

### Difference from Target

```DAX
Target Gap = [Total Sales] - [Sales Target]
```

---

## 🚦 Step 5: KPI Status (Green / Red Logic)

```DAX
Sales Status =
IF(
    [Total Sales] >= [Sales Target],
    "Achieved",
    "Not Achieved"
)
```

👉 Isko KPI visual ya Card ke sath use karo.

---

## 📈 Step 6: Use Measures in Visuals

Best visuals:

* **Card** → Total Sales, Profit
* **KPI Visual** → Sales vs Target
* **Bar Chart** → Product vs Sales
* **Table** → Region + Profit

📌 Measures auto update hon gi jab filter lagay ga.

---

## ⚠️ Common DAX Mistakes (Avoid)

❌ Calculated column use karna KPIs ke liye
❌ Division with `/` instead of `DIVIDE()`
❌ Measure names unclear

✔️ Clear naming: `Total Sales`, `Total Profit`

---

## 🧠 Simple Example

Socho:

* Column = calculator ki history
* Measure = calculator ka **current result**

---

## 📝 Mini Task (Practice)

Try this:

* Create **Average Sales**

```DAX
Average Sales = AVERAGE(Sales_Data_Clean[Sales])
```

* Create **Max Sale**

```DAX
Max Sale = MAX(Sales_Data_Clean[Sales])
```
