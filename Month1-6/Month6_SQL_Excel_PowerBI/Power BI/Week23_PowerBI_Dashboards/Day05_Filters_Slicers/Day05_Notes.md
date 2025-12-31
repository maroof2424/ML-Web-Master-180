

# 📅 **Day 5 – Filters & Slicers (Power BI)**

## 🎯 Objective

* Dashboard ko **user-controlled** banana
* Filters aur slicers ka difference samajhna
* Proper filtering logic use karna

> Rule: *“User ko control do, confusion nahi.”*

---

## 🧠 Step 1: Types of Filters in Power BI

### 🔹 1. Visual Level Filter

* Sirf **ek visual** pe apply hota hai
  Example: Bar chart mein sirf `North` region

### 🔹 2. Page Level Filter

* Poore **page** pe apply hota hai
  Example: Sirf `2024` ka data

### 🔹 3. Report Level Filter

* **Har page** pe apply hota hai
  Example: Sirf `Laptop` product

📌 Ye filters **Filters Pane** mein hote hain.

---

## 🎛 Step 2: Slicer (Most Important)

**Slicer = visual filter**

### How to add:

1. `Report View`
2. `Insert → Slicer`
3. Field drag karo (Region / Product / Date)

Best slicers:

* Region
* Product
* Date (Month / Year)

---

## 🔄 Step 3: Make Slicers Control Multiple Visuals

1. Select slicer
2. `Format → Edit interactions`
3. Ensure all visuals are **filtered**, not ignored

📌 Ye step bohot log miss kar dete hain.

---

## 🗓 Step 4: Date Slicer (Professional Touch)

Use:

* `Dim_Date[Date]`

Change slicer type:

* Dropdown → Between → Relative Date

👉 Managers ko date control bohot pasand hota hai.

---

## ⚙️ Step 5: Sync Slicers (Advanced)

Agar multiple pages hain:

1. Select slicer
2. `View → Sync slicers`
3. Choose pages

💡 Is se **global filter** ban jata hai.

---

## 🚦 Step 6: Filter KPIs with Slicers

Test karo:

* Region slicer change karo
* **Total Sales card** change ho raha?

Agar nahi:

* Model relationship check karo (Day 3)

---

## ⚠️ Common Mistakes (Avoid)

❌ Too many slicers
❌ Same slicer repeated on every page
❌ Filters without labels

✔️ Simple, clear, limited slicers

---

## 🧠 Simple Example

Socho:

* Dashboard = TV
* Slicer = remote control 😄
* Filter = TV ka internal setting

---

## 📝 Mini Task (Practice)

Try this:

* Add slicer → Product
* Add slicer → Region
* Test: Product + Region combined filter

Bonus:

* Profit < 0 filter laga ke **loss products** dikhao

---

## ✅ Day 5 Summary 

* Filters = backend control
* Slicers = frontend control
* Interactions check karna zaroori
* Clean filters = happy user