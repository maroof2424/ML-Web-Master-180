

## ✅ Day 1 → `01_linear_regression.ipynb`

**Concepts:**

* Linear Regression ka math:

  $$
  y = m x + c
  $$

  Yaha $m$ slope aur $c$ intercept hota hai.
* Model ko train karna matlab best-fit line find karna jisme error (residuals) sabse kam ho.
* Loss function: **MSE (Mean Squared Error)**

  $$
  MSE = \frac{1}{n} \sum (y_{true} - y_{pred})^2
  $$

---

### 🔑 Key Points

* Regression = continuous value prediction (like house price, salary, tips).
* Train data → model coefficients (slope, intercept).
* Evaluate with metrics: **MAE, MSE, RMSE**.

---

### 📘 Sample Code (on `tips` dataset from seaborn)

```python
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

# Load dataset
df = sns.load_dataset("tips")

# Features & Target
X = df[["total_bill"]]   # independent variable
y = df["tip"]            # dependent variable

# Train model
model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Metrics
mse = mean_squared_error(y, y_pred)
mae = mean_absolute_error(y, y_pred)
rmse = np.sqrt(mse)

print("Intercept (c):", model.intercept_)
print("Slope (m):", model.coef_[0])
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
```

---
