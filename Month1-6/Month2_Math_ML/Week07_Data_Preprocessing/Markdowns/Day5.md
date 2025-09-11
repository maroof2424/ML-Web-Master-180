# 📘 Day 5 – Feature Engineering 

```python
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import SelectKBest, f_classif

# Load Titanic dataset (Seaborn version)
df = sns.load_dataset("titanic")

# Select useful columns
df = df[["survived", "pclass", "sex", "age", "fare", "sibsp", "parch", "embarked"]]

print(df.head())
```

---

## 🔹 1. Create New Features

### ➡️ Family Size

```python
df["family_size"] = df["sibsp"] + df["parch"] + 1
```

### ➡️ Is Alone

```python
df["is_alone"] = (df["family_size"] == 1).astype(int)
```

### ➡️ Age Bins

```python
df["age_bin"] = pd.cut(df["age"], bins=[0, 12, 18, 35, 60, 80],
                       labels=["Child", "Teen", "Young", "Adult", "Senior"])
```

### ➡️ Fare per Person

```python
df["fare_per_person"] = df["fare"] / df["family_size"]
```

---

## 🔹 2. Feature Interactions (Polynomial)

Example: age × pclass → maybe richer younger passengers survived more.

```python
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(df[["age", "fare"]].fillna(0))

poly_df = pd.DataFrame(X_poly, columns=poly.get_feature_names_out(["age", "fare"]))
print(poly_df.head())
```

This generates features like:

* `age^2`
* `fare^2`
* `age * fare`

---

## 🔹 3. Feature Selection

### ➡️ Correlation Heatmap

```python
import matplotlib.pyplot as plt

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()
```

---

### ➡️ Select Best Features (ANOVA F-test)

```python
X = df.drop(columns=["survived", "sex", "embarked", "age_bin"])  # numeric only
y = df["survived"]

selector = SelectKBest(score_func=f_classif, k=5)
X_new = selector.fit_transform(X.fillna(0), y)

print("Selected features:", X.columns[selector.get_support()])
```

---

## ✅ Insights

* Features like **fare**, **pclass**, **age**, **family\_size**, and **is\_alone** are often strong predictors.
* **Polynomial features** may help capture non-linear survival patterns.
* **Feature selection** ensures we only keep the most useful ones.

---
