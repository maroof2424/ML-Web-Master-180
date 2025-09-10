# 📘 Day 4 – Encoding Categorical Features

### 🎯 Goals

* Learn how to **convert categorical features into numerical** form.
* Use **LabelEncoder** for binary features.
* Use **OneHotEncoder** for multi-class features.
* Handle categorical columns in Pandas DataFrames.

---

## 🔹 1. Why Encoding?

Machine learning models **cannot work directly with categorical (string) data**.
We must convert categories → numbers, while preserving meaning.

---

## 🔹 2. Label Encoding (Binary Categories)

* Used when a column has **only 2 unique values**.
* Converts them into **0 and 1**.

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import seaborn as sns

# Example dataset
df = sns.load_dataset("tips")

# Binary categorical column
print(df['sex'].unique())   # ['Female', 'Male']

le = LabelEncoder()
df['sex_encoded'] = le.fit_transform(df['sex'])

print(df[['sex', 'sex_encoded']].head())
```

✅ **"Female" → 0, "Male" → 1**

---

## 🔹 3. One-Hot Encoding (Multi-Class Categories)

* Used when a column has **more than 2 unique values**.
* Creates **new columns** (dummy variables) for each category.

```python
from sklearn.preprocessing import OneHotEncoder

# Multi-class categorical column
print(df['day'].unique())   # ['Sun', 'Sat', 'Thur', 'Fri']

ohe = OneHotEncoder(sparse_output=False, drop='first')  
day_encoded = ohe.fit_transform(df[['day']])

# Convert to DataFrame
day_df = pd.DataFrame(day_encoded, columns=ohe.get_feature_names_out(['day']), index=df.index)

# Join with original df
df = pd.concat([df, day_df], axis=1)
print(df.head())
```

✅ Creates new columns like:

* `day_Fri`, `day_Sat`, `day_Sun` (Thursday dropped to avoid dummy trap).

---

## 🔹 4. Handling Multiple Categorical Features in DataFrames

You can loop through categorical columns:

```python
categorical = df.select_dtypes(include=['object', 'category']).columns.tolist()

# Separate binary and multi-class
label_cols = [col for col in categorical if df[col].nunique() == 2]
onehot_cols = [col for col in categorical if df[col].nunique() > 2]

# Apply Label Encoding
le = LabelEncoder()
for col in label_cols:
    df[col] = le.fit_transform(df[col])

# Apply One-Hot Encoding
ohe = OneHotEncoder(sparse_output=False, drop='first')
ohe_array = ohe.fit_transform(df[onehot_cols])
ohe_df = pd.DataFrame(ohe_array, columns=ohe.get_feature_names_out(onehot_cols), index=df.index)

# Merge and clean
df = df.drop(columns=onehot_cols)
df = pd.concat([df, ohe_df], axis=1)

print(df.head())
```

---

## ✅ Summary

* **LabelEncoder** → Binary categorical features
* **OneHotEncoder** → Multi-class categorical features
* Handle categorical columns systematically with Pandas

---
