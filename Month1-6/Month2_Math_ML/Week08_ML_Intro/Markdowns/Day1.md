
# ✅ **Day 1 – Linear Regression**

**Notebook:** `01_linear_regression.ipynb`

### **Concepts**

1. **Regression:** Predict a continuous target variable `y` from input `X`.
2. **Simple Linear Regression:**

   $$
   y = mX + c
   $$

   * `m` = slope
   * `c` = intercept
3. **Goal:** Find `m` and `c` that minimize the difference between predicted and actual `y`.
4. **Loss Function:** Mean Squared Error (MSE):

   $$
   MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
   $$

---

### **Code Example (Using Sklearn & Sample Data)**

```python
# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Sample dataset: House prices (simplified)
data = {
    'Area_sqft': [750, 800, 850, 900, 950, 1000, 1050, 1100],
    'Price_k': [150, 160, 165, 175, 180, 190, 200, 210]
}

df = pd.DataFrame(data)

# Features and target
X = df[['Area_sqft']]  # Input must be 2D
y = df['Price_k']

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Create linear regression model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Predict
y_pred = lr.predict(X_test)

# Metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Slope (m): {lr.coef_[0]:.2f}")
print(f"Intercept (c): {lr.intercept_:.2f}")
print(f"MSE: {mse:.2f}, R2 Score: {r2:.2f}")

# Plot regression line
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, lr.predict(X), color='red', label='Predicted')
plt.xlabel('Area (sqft)')
plt.ylabel('Price (k)')
plt.title('Linear Regression: House Price Prediction')
plt.legend()
plt.show()
```

---

### **Explanation**

1. We create a **simple dataset** of house area vs price.
2. We split data into **train/test** sets to evaluate performance.
3. `LinearRegression()` automatically calculates **slope and intercept**.
4. Predictions are made with `lr.predict(X_test)`.
5. Metrics:

   * **MSE**: how close predictions are to actual values.
   * **R² Score**: proportion of variance explained by the model.
6. Plot shows **actual points vs predicted line**.

---
