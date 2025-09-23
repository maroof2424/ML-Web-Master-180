## ✅ Day 2 → `02_logistic_regression.ipynb`

### 🔑 Concepts:

* **Linear Regression vs Logistic Regression**

  * Linear regression → continuous output (e.g. house price).
  * Logistic regression → categorical output (mostly **binary 0/1**).
* Logistic regression uses the **Sigmoid function** to squash predictions between **0 and 1**:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

* **Threshold** (default 0.5):

  * If $p > 0.5$ → class = 1
  * If $p \leq 0.5$ → class = 0

---

### 🐍 Code Example

#### 1️⃣ Titanic Dataset → Logistic Regression

```python
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load Titanic dataset
titanic = sns.load_dataset("titanic")

# Select features & drop missing values
df = titanic[["sex", "age", "fare", "class", "survived"]].dropna()

# Convert categorical → numeric
df["sex"] = df["sex"].map({"male": 0, "female": 1})
df["class"] = df["class"].map({"First": 1, "Second": 2, "Third": 3})

X = df[["sex", "age", "fare", "class"]]
y = df["survived"]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression
log_reg = LogisticRegression(max_iter=200)
log_reg.fit(X_train, y_train)

# Prediction
y_pred = log_reg.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
```

---

#### 2️⃣ Compare with Linear Regression (wrong for classification ⚠️)

```python
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

y_pred_lin = lin_reg.predict(X_test)

# Convert predictions to 0/1 by thresholding
y_pred_class = (y_pred_lin > 0.5).astype(int)

print("Linear Regression Accuracy:", accuracy_score(y_test, y_pred_class))
```

--- 