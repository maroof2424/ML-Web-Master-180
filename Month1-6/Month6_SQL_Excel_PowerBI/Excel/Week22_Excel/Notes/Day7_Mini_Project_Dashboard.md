

# 📅 **Day 7 — Pivot Table + Pivot Chart (Complete Practical)**

Aaj ka goal:

* Data ko **summarize**
* **Trends samajhna**
* **Decision-making style reporting**

> Ye skill internships + jobs mein bohot kaam aati hai.

---

## 🧾 **Step 1: Raw Demo Data (Excel Sheet)**

Excel mein **Sheet1** banayo aur ye data paste karo:

| Date   | Region | Product    | Sales | Profit |
| ------ | ------ | ---------- | ----- | ------ |
| 01-Jan | North  | Laptop     | 1200  | 300    |
| 02-Jan | South  | Mouse      | 200   | -20    |
| 03-Jan | East   | Chair      | 450   | 80     |
| 04-Jan | West   | Desk       | 800   | 150    |
| 05-Jan | North  | Headphones | 600   | -50    |
| 06-Jan | East   | Laptop     | 1300  | 350    |
| 07-Jan | South  | Desk       | 750   | 120    |

📌 **Important Rule (Best Practice)**

* No empty rows
* No merged cells
* Har column ka clear heading

---

## 📊 **Step 2: Create Pivot Table**

1. **Poora data select karo**
2. `Insert → PivotTable`
3. New Worksheet select karo → **OK**

---

## 🧠 **Step 3: Pivot Table Layout (Main Logic)**

### 🔹 Case 1: Product-wise Summary

Drag ye fields:

* **Rows** → Product
* **Values** → Sales (Sum)
* **Values** → Profit (Sum)

### Output samajh lo:

* Konsa product **zyada sale** kar raha?
* Konsa product **loss** mein ja raha?

👉 Real-world use: Product decision making

---

## 📅 **Step 4: Date-wise Analysis**

1. Rows mein **Date**
2. Values mein:

   * Sum of Sales
   * Sum of Profit

📌 Date pe right-click → **Group**

* Days / Months select kar sakte ho

👉 Ye monthly / weekly reports ke liye hota hai

---

## 🌍 **Step 5: Region-wise Performance**

Pivot mein set karo:

* **Rows** → Region
* **Values** → Sales
* **Values** → Profit

### Insight:

* Konsa region profitable hai?
* Kahan loss ho raha?

💡 Honest advice:
Managers **region-wise pivot** sabse pehle dekhte hain.

---

## 📈 **Step 6: Pivot Chart (Visual Magic)**

1. Pivot table select karo
2. `Insert → Pivot Chart`
3. Column Chart ya Bar Chart select karo

Best charts:

* Sales → Column Chart
* Profit → Bar Chart

📌 **Golden Rule**

> Chart sirf tab banao jab numbers ka story ho

---

## ⚠️ **Common Mistakes (Avoid This)**

❌ Raw data mein empty rows
❌ Changing data manually inside pivot
❌ Using merged cells
❌ Not refreshing pivot after data change

✔️ **Correct way**
Right click pivot → **Refresh**

---

## 🎯 **Mini Practice Task (Tum khud karo)**

Try this:

* Product = Rows
* Region = Columns
* Values = Sales

👉 Ye **cross-analysis** kehlata hai (Advanced level)

---

## 🧠 **Simple Example Samajhne Ke Liye**

Socho tum shop owner ho:

* Pivot = **summary notebook**
* Raw data = **daily sales register**
* Chart = **visual report for boss**

---

## ✅ **Day 7 Summary (Yaad Rakhne Ke Liye)**

* Pivot Table = **Smart summary tool**
* Rows = kis cheez ka analysis
* Values = numbers (Sales / Profit)
* Chart = story visualization
* Refresh karna mat bhoolna
