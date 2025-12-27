# **Day 5 – PivotTables Basics**

## **Objective**

Learn how to **summarize large datasets in seconds** without writing formulas.

👉 Goal:
**“Raw data → meaningful summary”**

---

## **1️⃣ What is a PivotTable? (Concept)**

### Simple Definition

A PivotTable is a **dynamic summary table** that lets you:

* Group data
* Calculate totals, averages, counts
* Slice data from different angles

📌 Think of it as:

> **SQL GROUP BY inside Excel**

---

## **2️⃣ Why PivotTables Are So Powerful**

Without PivotTable:

* Many formulas
* Manual updates
* Error-prone

With PivotTable:

* Drag & drop
* Auto-updates
* Fast analysis

👉 This is why analysts love PivotTables.

---

## **3️⃣ Demo Dataset (Use This)**

Paste this into Excel (raw data format):

| Date   | Region | Product    | Sales | Profit |
| ------ | ------ | ---------- | ----- | ------ |
| 01-Jan | North  | Laptop     | 1200  | 300    |
| 02-Jan | South  | Mouse      | 200   | -20    |
| 03-Jan | East   | Chair      | 450   | 80     |
| 04-Jan | West   | Desk       | 800   | 150    |
| 05-Jan | North  | Headphones | 600   | -50    |
| 06-Jan | East   | Laptop     | 1300  | 350    |
| 07-Jan | South  | Desk       | 750   | 120    |

⚠️ **Rule:** No blank rows, no merged cells.

---

## **4️⃣ Creating Your First PivotTable**

### Steps

1. Click anywhere in the dataset
2. Insert → PivotTable
3. Choose **New Worksheet**
4. Click OK

You’ll see:

* PivotTable area
* Field List (right side)

---

## **5️⃣ Understanding Pivot Areas (VERY IMPORTANT)**

| Area    | Purpose                      |
| ------- | ---------------------------- |
| Rows    | Categories (Region, Product) |
| Columns | Sub-categories               |
| Values  | Calculations (Sum, Avg)      |
| Filters | High-level filtering         |

---

## **6️⃣ First Pivot Example – Sales by Region**

### Drag & Drop

* **Rows:** Region
* **Values:** Sales (Sum)

### Result

You get total sales per region instantly.

📌 No formula needed.

---

## **7️⃣ Second Pivot – Sales by Product**

* **Rows:** Product
* **Values:** Sales (Sum)

👉 Compare which product performs best.

---

## **8️⃣ Changing Calculations**

Click dropdown on **Sum of Sales** →

* Sum
* Average
* Count
* Max / Min

Example:

* Average Profit by Region

---

## **9️⃣ Sorting & Filtering**

### Sorting

* Right-click value → Sort Largest to Smallest

### Filtering

* Use dropdowns on Row Labels

📌 Helps focus on **top or bottom performers**.

---

## **10️⃣ Refreshing PivotTable (Important)**

If raw data changes:

* Right-click PivotTable → Refresh

❌ Pivot does NOT auto-update by default.

---

## **11️⃣ Common Beginner Mistakes**

❌ Formatting raw data
❌ Using merged cells
❌ Forgetting to refresh
❌ Editing pivot values manually

---

## **Key Takeaways**

* PivotTables summarize data fast
* Drag & drop logic
* Rows = categories
* Values = calculations
* Always refresh after data change

---
