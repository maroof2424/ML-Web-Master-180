# 📅 **Day 6 – Charts, Graphs & Storytelling (Power BI)**

## 🎯 Objective

* Data ko **insightful visual story** mein convert karna
* Charts aur graphs select karna situation ke hisaab se
* Interactive dashboard ready karna

> Rule: *“Number se story banao, boss ko impress karo”*

---

## 🧠 Step 1: Choose the Right Chart

| Visual       | Use Case                                    |
| ------------ | ------------------------------------------- |
| Column / Bar | Compare categories (Region, Product)        |
| Line         | Trends over time (Sales vs Date)            |
| Area         | Trend + magnitude                           |
| Pie / Donut  | Share of total (small number of categories) |
| Combo        | Line + Column (e.g., Sales + Profit)        |
| Card         | Single KPI (Total Sales, Total Profit)      |
| KPI Visual   | Target vs Actual                            |

---

## 🖌 Step 2: Add Charts in Report View

1. **Column Chart – Sales by Product**

   * Axis → `Dim_Product[Product]`
   * Values → `Total Sales`
   * Optional → Add `Profit` as tooltip

2. **Line Chart – Sales Over Time**

   * Axis → `Dim_Date[Date]`
   * Values → `Total Sales`
   * Add **Profit line** if needed (combo chart)

3. **Pie Chart – Sales by Region**

   * Legend → `Dim_Region[Region]`
   * Values → `Total Sales`
   * Small categories → combine as “Other”

---

## 🔄 Step 3: Conditional Formatting in Charts

* Column / Bar chart → `Data Colors → By Rules`
* Example:

  * Profit > 0 → Green
  * Profit < 0 → Red

> Ye visual cue boss ko immediately bata deta hai profit/loss

---

## 📊 Step 4: Tooltip & Drill-Down

* Tooltip → Extra info (Profit, Sales Category)
* Drill-down → Date → Month → Week
* Drill-through → Click on Product → see region-wise details

---

## 🗂 Step 5: Storytelling Tips

1. **Top KPIs first** → Total Sales, Profit, Margin
2. **Trends** → Line chart in center
3. **Breakdown** → Column / Pie for category comparison
4. **Filters / Slicers** → Side panel for interaction
5. **Title + Annotation** → Make insights readable

> Boss should get insights **within 5 seconds**

---

## ⚠️ Step 6: Common Mistakes

❌ Too many charts = confusing
❌ Pie chart with > 6 categories
❌ Ignoring filters + slicers
❌ Bad color scheme (clashing colors)

✔️ Rule: **Less is more, clear colors, interactive**

---

## 🧠 Simple Example

Socho:

* Column chart = “Which product is top?”
* Line chart = “How did sales trend over month?”
* Pie chart = “Which region is contributing?”
* Card = “Total KPI”
* Together = story in 1 page

---

## 📝 Mini Task (Practice)

1. Column chart → Product vs Sales
2. Line chart → Date vs Total Sales
3. Pie chart → Region vs Total Profit
4. Add **Profit Status slicer** → see how visuals change
5. Conditional formatting → Profit < 0 = Red

---

## ✅ Day 6 Summary

* Charts = story-telling tool
* Visuals should **match question**
* Conditional formatting = quick insight
* Drill-down & tooltips = pro-level dashboard