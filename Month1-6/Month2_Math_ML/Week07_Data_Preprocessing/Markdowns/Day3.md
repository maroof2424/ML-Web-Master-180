# 📅 Week 7 – Day 3: Feature Scaling

When working with machine learning algorithms, **features with different scales** can distort results. Scaling helps normalize or standardize data so that all features contribute equally.

---

## 🔹 Why Scaling is Important

1. Algorithms like **KNN, SVM, Gradient Descent-based methods** depend on distance calculations.
2. Features with larger magnitudes dominate the objective function if not scaled.
3. Helps in **faster convergence** in optimization algorithms.

---

## 🔹 Scaling Techniques

### 1️⃣ **Min-Max Scaling (Normalization)**

* Scales data to a fixed range, usually **\[0, 1]**.
* Formula:

$$
X_{\text{scaled}} = \frac{X - X_{\min}}{X_{\max} - X_{\min}}
$$

* Good for algorithms that require bounded input.
* Sensitive to outliers.

**Code Example:**

```python
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

data = {"Age": [20, 25, 30, 35, 100]}  # 100 is an outlier
df = pd.DataFrame(data)

scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df)
print(pd.DataFrame(df_scaled, columns=df.columns))
```

---

### 2️⃣ **StandardScaler (Z-score Standardization)**

* Centers data to **mean=0** and **std=1**.
* Formula:

$$
X_{\text{scaled}} = \frac{X - \mu}{\sigma}
$$

* Good for algorithms assuming normally distributed data.
* Less sensitive to outliers than MinMaxScaler (but not completely robust).

**Code Example:**

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df_std = scaler.fit_transform(df)
print(pd.DataFrame(df_std, columns=df.columns))
```

---

### 3️⃣ **RobustScaler**

* Uses **median** and **IQR** instead of mean & std.
* Formula:

$$
X_{\text{scaled}} = \frac{X - \text{Median}}{IQR}
$$

* Best for **datasets with outliers**, because it is robust to extreme values.

**Code Example:**

```python
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
df_robust = scaler.fit_transform(df)
print(pd.DataFrame(df_robust, columns=df.columns))
```

---

## 🔹 How to Choose:

| Scaler         | Use Case                                                               |
| -------------- | ---------------------------------------------------------------------- |
| MinMaxScaler   | When features need \[0,1] range, no outliers                           |
| StandardScaler | When data is roughly normal, ML algorithms like SVM, Linear Regression |
| RobustScaler   | When dataset has outliers                                              |

---

## ✅ Mini Task:

1. Take a dataset (e.g., `Age` and `Salary`).
2. Apply **all three scalers**.
3. Visualize using **boxplots** to see differences.
4. Save as `03_scaling.ipynb`.

---