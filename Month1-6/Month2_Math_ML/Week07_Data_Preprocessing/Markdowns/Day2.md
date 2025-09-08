
# 📅 Week 7 – Day 2: Handling Outliers

## 🔹 What are Outliers?
Outliers are extreme values in the dataset that deviate significantly from the rest.  
They may be due to:
- Data entry errors
- Natural variations
- Measurement issues

Outliers can **distort mean, variance, and ML models**.

---

## 🔹 1. Visual Detection – Boxplots
```python
import seaborn as sns
sns.boxplot(df["Age"])
````

* The "whiskers" show normal range.
* Points outside are **outliers**.

---

## 🔹 2. IQR Method (Interquartile Range)

```python
Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["Age"] < lower) | (df["Age"] > upper)]
```

---

## 🔹 3. Z-Score Method

```python
from scipy import stats
import numpy as np

z_scores = np.abs(stats.zscore(df["Age"]))
outliers = df[z_scores > 3]   # Z > 3 = outlier
```

---

## ✅ Mini Task

1. Generate a dataset with outliers (e.g., salaries, heights).
2. Detect outliers using:

   * Boxplot
   * IQR method
   * Z-score method
3. Document results in **`02_outliers.ipynb`**.


