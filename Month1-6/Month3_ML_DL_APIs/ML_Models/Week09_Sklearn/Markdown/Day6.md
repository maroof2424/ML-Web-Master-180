

# ✅ Day 6 – Build Models & Compare Metrics

## 1️⃣ Regression Example – Boston Housing Dataset 🏠

### Steps:

1. Load dataset
2. Train **Linear Regression** & **Decision Tree Regressor**
3. Compare **MAE** & **RMSE**

```python
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Load dataset
data = fetch_california_housing()
X, y = data.data, data.target

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Models
lr = LinearRegression()
dt = DecisionTreeRegressor(max_depth=5, random_state=42)

# Fit models
lr.fit(X_train, y_train)
dt.fit(X_train, y_train)

# Predictions
y_pred_lr = lr.predict(X_test)
y_pred_dt = dt.predict(X_test)

# Metrics
def evaluate(y_true, y_pred, name):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    print(f"📊 {name} → MAE: {mae:.4f}, RMSE: {rmse:.4f}")

evaluate(y_test, y_pred_lr, "Linear Regression")
evaluate(y_test, y_pred_dt, "Decision Tree Regressor")
```

---

## 2️⃣ Classification Example – Titanic Dataset 🚢

### Steps:

1. Load Titanic dataset (from seaborn or CSV)
2. Train **Logistic Regression** & **Random Forest**
3. Compare using **Accuracy, Confusion Matrix, F1-score**

```python
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load Titanic dataset
titanic = sns.load_dataset("titanic").dropna(subset=["age", "fare", "sex", "class", "survived"])
X = titanic[["age", "fare"]]
X["sex"] = titanic["sex"].map({"male": 0, "female": 1})  # encode sex
y = titanic["survived"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Models
log_reg = LogisticRegression(max_iter=200)
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Fit models
log_reg.fit(X_train, y_train)
rf.fit(X_train, y_train)

# Predictions
y_pred_log = log_reg.predict(X_test)
y_pred_rf = rf.predict(X_test)

# Metrics
def evaluate_clf(y_true, y_pred, name):
    print(f"\n🔎 {name}")
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_true, y_pred))
    print("Classification Report:\n", classification_report(y_true, y_pred))

evaluate_clf(y_test, y_pred_log, "Logistic Regression")
evaluate_clf(y_test, y_pred_rf, "Random Forest")
```

---

## 🔑 Key Notes:

* Regression → Compare **MAE & RMSE** across models.
* Classification → Compare **Accuracy + Confusion Matrix + Precision/Recall/F1**.
* Sometimes simpler models (like Logistic Regression) can perform **close to complex models**.

---


