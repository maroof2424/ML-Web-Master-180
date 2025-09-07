
# 📅 Week 7 – Day 1: Handling Null Values

## 🔹 Why Handle Missing Data?
Real-world datasets often contain missing values (`NaN`, `None`).  
If not treated, models may produce biased or invalid results.

---

## 🔹 Techniques

### 1. Drop Missing Values
Remove rows or columns that contain nulls.
```python
df.dropna()         # drop rows with any null
df.dropna(axis=1)   # drop columns with any null
````

---

### 2. Fill with Fixed Value

Replace missing values with a constant.

```python
df.fillna(0)   # replace nulls with 0
```

---

### 3. Mean/Median/Mode Imputation

Replace missing values with summary statistics.

```python
df["Age"].fillna(df["Age"].mean(), inplace=True)     # mean
df["Age"].fillna(df["Age"].median(), inplace=True)   # median
df["Age"].fillna(df["Age"].mode()[0], inplace=True)  # mode
```

---

### 4. Forward Fill & Backward Fill

Fill values using neighbors.

```python
df.fillna(method="ffill")   # forward fill
df.fillna(method="bfill")   # backward fill
```

---

## ✅ Mini Task

1. Create a small dataset with missing values.
2. Try: **drop**, **fill with mean**, **ffill**, **bfill**.
3. Save results in **`01_nulls.ipynb`**.

---

