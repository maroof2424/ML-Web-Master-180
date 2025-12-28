
# 📅 **Day 2 – Data Cleaning with Power Query**

## 🎯 Objective

Raw sales data ko **clean, structured aur analysis-ready** banana using **Power Query Editor**.

> Rule: *“Bad data → Bad dashboard”*
> Is liye Day 2 ko lightly mat lena.

---

## 🧾 Step 0: Open Power Query

1. Power BI Desktop open karo
2. `Home → Transform Data`
3. **Power Query Editor** open ho jayega

---

## 🧠 Step 1: Understand Your Data

Tumhara data:

| Date | Region | Product | Sales | Profit |
| ---- | ------ | ------- | ----- | ------ |

Check karo:

* Data types correct hain?
* Spelling consistent hai?
* Negative profit kahaan aa raha hai?

---

## 🔧 Step 2: Fix Data Types (MOST IMPORTANT)

### How:

* Date → **Date**
* Region → **Text**
* Product → **Text**
* Sales → **Whole Number**
* Profit → **Whole Number**

📌 Power Query mein column header ke icon par click karke type set karo.

💡 **Why important?**
Agar data type ghalat ho:

* Charts break ho jaate hain
* DAX errors aate hain

---

## ✂️ Step 3: Remove Duplicates (If Any)

1. `Region + Product + Date` select karo
2. `Home → Remove Rows → Remove Duplicates`

👉 Real datasets mein duplicate entries common hoti hain.

---

## 🧹 Step 4: Clean Text (Professional Touch)

### For Region & Product:

1. Select column
2. `Transform → Format`

   * **Trim**
   * **Clean**
   * **Capitalize Each Word**

📌 Example:

* `north` → `North`
* `laptop` → `Laptop`

---

## ⚠️ Step 5: Handle Negative Profit

### Create New Column (Best Practice)

1. `Add Column → Conditional Column`
2. Name: `Profit Status`

Conditions:

* If Profit < 0 → `Loss`
* Else → `Profit`

👉 Ye KPIs aur visuals ke liye bohot useful hota hai.

---

## ➕ Step 6: Create Calculated Column (Revenue Category)

1. `Add Column → Conditional Column`
2. Name: `Sales Category`

Rules:

* Sales >= 1000 → High
* Sales >= 500 → Medium
* Else → Low

💡 Ye segmentation dashboards mein shine karta hai.

---

## 🔄 Step 7: Rename Query & Columns

* Query name: `Sales_Data_Clean`
* Short & meaningful column names

❌ `Column1`
✔️ `Sales`

---

## ✅ Step 8: Close & Apply

1. `Home → Close & Apply`
2. Data Report view mein load ho jayega

---

## 📌 Best Practices (Real Advice)

✔️ Cleaning Power Query mein karo
❌ Report view mein manual fixes mat karo

✔️ Conditional columns use karo
✔️ Data types hamesha pehle fix karo

---

## 🧠 Simple Example

Socho:

* Raw data = ganday kapray
* Power Query = washing machine
* Dashboard = clean outfit 😄

---

## 📝 Mini Task (Tumhare Liye)

Try this:

* Profit < 0 ko **red color flag** ke liye column banao
* Date se **Month column** extract karo

(`Transform → Date → Month → Name`)

---

## ✅ Day 2 Summary (Yaad Rakhna)

* Power Query = backbone of Power BI
* Data types sab se pehle
* Conditional columns = smart analysis
* Clean data = strong dashboard