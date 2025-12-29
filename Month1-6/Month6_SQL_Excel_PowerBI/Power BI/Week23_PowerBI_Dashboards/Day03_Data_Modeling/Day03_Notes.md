# 📅 **Day 3 – Data Modeling & Relationships (Power BI)**

## 🎯 Objective

Data ko **proper structure** dena so that:

* Measures sahi calculate hon
* Filters ka effect har chart pe ho
* Dashboard scalable ho

> Rule: *“Visualization se pehle, model sahi hona chahiye.”*

---

## 🧠 Step 1: What is Data Modeling?

Data Modeling ka matlab:

* Tables ke darmiyan **relationships define karna**
* Fact table vs Dimension table samajhna

### Simple terms:

* **Fact Table** → Numbers (Sales, Profit)
* **Dimension Table** → Categories (Date, Product, Region)

---

## 🗂 Step 2: Our Current Situation

Abhi tumhare paas:

* `Sales_Data_Clean` (Fact Table)

Isko professional banane ke liye hum **dimension tables** banayenge:

* Date Table
* Product Table
* Region Table

---

## 🛠 Step 3: Create Dimension Tables (Power Query)

### 🔹 Product Table

1. `Transform Data`
2. Right-click `Sales_Data_Clean` → **Reference**
3. Keep only `Product`
4. Remove duplicates
5. Rename query → `Dim_Product`

---

### 🔹 Region Table

1. Reference `Sales_Data_Clean`
2. Keep `Region`
3. Remove duplicates
4. Rename → `Dim_Region`

---

### 🔹 Date Table (Basic Version)

1. Reference `Sales_Data_Clean`
2. Keep `Date`
3. Remove duplicates
4. Rename → `Dim_Date`

📌 (Advanced date table hum baad mein DAX se banayenge)

---

## 🔄 Step 4: Close & Apply

`Home → Close & Apply`

---

## 🔗 Step 5: Create Relationships (Model View)

1. Go to **Model View**
2. Drag relationships:

| From                      | To                   |
| ------------------------- | -------------------- |
| Sales_Data_Clean[Product] | Dim_Product[Product] |
| Sales_Data_Clean[Region]  | Dim_Region[Region]   |
| Sales_Data_Clean[Date]    | Dim_Date[Date]       |

### Relationship Type:

* **Many-to-One**
* **Single Direction**

✔️ Ye **star schema** kehlata hai (industry standard)

---

## ⭐ Step 6: Star Schema (Important Concept)

```
        Dim_Product
             |
Dim_Date — Sales_Data_Clean — Dim_Region
```

💡 Why star schema?

* Fast performance
* Easy DAX
* Clean filters

---

## ⚠️ Common Mistakes (Avoid This)

❌ Many-to-many relationships
❌ Bi-directional filters (unless needed)
❌ Using text columns as measures

✔️ Always numbers → Fact table
✔️ Always categories → Dimensions

---

## 🧠 Simple Example

Socho:

* Fact table = **Cash register**
* Dimension tables = **labels**
* Relationship = **connecting wires**

---

## 📝 Mini Task (Practice)

Try this:

* Add `Sales Category` from Fact table
* Create relationship with Product
* Test filter: Product → Sales

---

## ✅ Day 3 Summary (Yaad Rakhna)

* Data model = foundation
* Star schema = best practice
* Relationships control filters
* Clean model = easy DAX later
