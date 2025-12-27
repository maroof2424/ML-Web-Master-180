# 🟦 DAY 6 – PivotTables Advanced (STEP BY STEP)

## 🎯 Goal

* Same data se **multiple insights**
* **Grouping**
* **Filters**
* **Slicers**
* Dashboard feeling

---

## 🟩 STEP 0: DEMO DATA (PASTE THIS FIRST)

Excel me **Sheet1** me ye data paste karo:

| Date      | Region | Product    | Sales | Profit |
| --------- | ------ | ---------- | ----- | ------ |
| 01-Jan-24 | North  | Laptop     | 1200  | 300    |
| 02-Jan-24 | South  | Mouse      | 200   | -20    |
| 03-Jan-24 | East   | Chair      | 450   | 80     |
| 04-Jan-24 | West   | Desk       | 800   | 150    |
| 05-Jan-24 | North  | Headphones | 600   | -50    |
| 06-Jan-24 | East   | Laptop     | 1300  | 350    |
| 07-Jan-24 | South  | Desk       | 750   | 120    |
| 15-Feb-24 | North  | Laptop     | 1400  | 400    |
| 20-Feb-24 | West   | Chair      | 500   | 100    |

⚠️ RULES:

* No blank row
* No merged cells
* Header must be clear

---

## 🟦 STEP 1: CREATE BASE PIVOT TABLE

1. Click **any cell in data**
2. `Insert → PivotTable`
3. New Worksheet → OK

---

## 🟦 STEP 2: BASIC PIVOT (CHECKPOINT)

### Setup:

* Rows → **Product**
* Values → **Sum of Sales**
* Values → **Sum of Profit**

✔ Output:

```
Product      Sales   Profit
Laptop       3900    1050
Desk         1550    270
Chair        950     180
Headphones   600     -50
Mouse        200     -20
```

👉 Agar yahan tak clear hai → good 👍

---

## 🟦 STEP 3: FILTER (GLOBAL CONTROL)

### 🎯 Question: “Sirf North region ka data chahiye”

1. Drag **Region → Filters**
2. Top dropdown → select **North**

📌 Pivot table instantly change ho jayegi
📌 Data delete nahi hota, sirf view change hota hai

---

## 🟦 STEP 4: GROUPING DATES (MOST IMPORTANT)

### 🎯 Question: “Month wise sales chahiye”

### Do this:

1. Remove Product from Rows
2. Drag **Date → Rows**
3. Right-click any date
4. Click **Group**
5. Select:

   * Months
   * Years → OK

✔ Output:

```
Jan 2024
Feb 2024
```

📌 Ab tum time-series analysis kar rahe ho (industry skill)

---

## 🟦 STEP 5: SALES RANGE GROUPING (ADVANCED)

### 🎯 Question: “Low / Medium / High sales”

1. Drag **Sales → Rows**
2. Right-click any number
3. Click **Group**
4. Set:

   * Start: 0
   * End: 2000
   * By: 500

✔ Output:

```
0–500
500–1000
1000–1500
```

📌 Ye classification dashboards me bohot use hoti hai

---

## 🟦 STEP 6: ADD SLICERS (GAME CHANGER)

### 🎯 Interactive buttons

1. Click PivotTable
2. `Insert → Slicer`
3. Select:

   * Region
   * Product
4. OK

✔ Ab tum buttons se filter kar sakte ho
✔ Manager-friendly view

---

## 🟦 STEP 7: MULTIPLE PIVOTS + ONE SLICER

### 🎯 Real dashboard logic

1. Create **2nd PivotTable**

   * Rows → Region
   * Values → Sum of Sales
2. Click slicer
3. Right-click → **Report Connections**
4. Tick both PivotTables → OK

📌 ONE click → ALL pivots update 🔥

---

## 🟦 STEP 8: CALCULATED FIELD (BUSINESS METRIC)

### 🎯 Profit Margin

1. Click PivotTable
2. PivotTable Analyze
3. Fields, Items & Sets → Calculated Field
4. Name: `Profit Margin`
5. Formula:

```excel
= Profit / Sales
```

✔ Ab tum **real KPI** bana rahe ho

---

## 🟦 STEP 9: PIVOT CHART (LIVE VISUAL)

1. Click PivotTable
2. Insert → Column Chart

📌 Chart slicer ke sath change hoga
📌 This = dashboard behavior

---

## ✅ DAY 6 FINAL CHECKLIST

✔ Filters used
✔ Date grouped
✔ Slicers added
✔ Calculated field created
✔ Chart linked

Bas bolo: **“Day 7 project step by step”** 🚀
