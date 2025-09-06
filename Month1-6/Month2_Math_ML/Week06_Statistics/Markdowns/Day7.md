

# 📘 Day 7 – Mini Project: Statistical Analysis

### 🎯 Objective

Perform a **statistical analysis** on a real dataset (Titanic example, but you can use Netflix, FIFA, etc.).

---

## 🔹 Steps

### 1. Load Dataset

* Example: `sns.load_dataset("titanic")`
* Focus on relevant columns (e.g., `age`, `fare`, `sex`, `class`)

---

### 2. Central Tendency & Spread

* **Mean (average):** Sensitive to outliers.
* **Median:** Middle value, robust to outliers.
* **Mode:** Most frequent value.
* **Variance & Standard Deviation:** Spread of data.
* **Range:** `max - min`

✅ Example:

* Mean Age = 29.7
* Median Age = 28.0
* Mode Age = 24

---

### 3. Distribution & Normality

* Plot histogram with **KDE curve**
* Check if data looks Gaussian (bell curve)
* **Shapiro-Wilk Test:**

  * H₀: Data is normally distributed
  * If *p < 0.05* → reject H₀ (data not normal)

---

### 4. Hypothesis Testing (t-test)

* **Question:** Do males and females pay different fares?
* **Null Hypothesis (H₀):** No difference in average fares.
* **Alternate Hypothesis (H₁):** There is a significant difference.
* **t-test result:**

  * If *p < 0.05* → reject H₀ (significant difference).
  * If *p ≥ 0.05* → fail to reject H₀ (no difference).

---

### 5. ANOVA (F-test)

* Compare mean ages across 3 Titanic classes (First, Second, Third).
* **H₀:** All class means are equal.
* **H₁:** At least one class mean is different.
* If *p < 0.05* → significant difference in mean ages.

---

## ✅ Summary

* Computed **central tendency & spread**
* Checked **distribution & normality**
* Ran **t-test (male vs female fares)**
* Ran **ANOVA (age across classes)**

📘 Notebook: `07_mini_project.ipynb`

---
