
# 📘 Day 6 – Hyperparameter Tuning on Real Dataset

Aaj hum **end-to-end tuning** karenge:

* Dataset → Titanic (classification problem)
* Preprocessing → Encode categorical, handle nulls
* Model → RandomForest + LogisticRegression
* Tuning → `GridSearchCV` & `RandomizedSearchCV`
* Compare results

---

## 🔹 Step 1: Load & Preprocess Titanic

```python
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Dataset
titanic = sns.load_dataset("titanic")

# Select useful features
df = titanic[["pclass", "sex", "age", "fare", "embarked", "survived"]].dropna()

# Encode categorical
le = LabelEncoder()
df["sex"] = le.fit_transform(df["sex"])
df["embarked"] = le.fit_transform(df["embarked"])

X = df.drop("survived", axis=1)
y = df["survived"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

---

## 🔹 Step 2: Logistic Regression Tuning (GridSearchCV)

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

log_reg = LogisticRegression(max_iter=1000)

param_grid = {
    "C": [0.01, 0.1, 1, 10, 100],
    "penalty": ["l1", "l2", "elasticnet", None],
    "solver": ["lbfgs", "liblinear", "saga"]
}

grid_search_lr = GridSearchCV(log_reg, param_grid, cv=5, scoring="accuracy", n_jobs=-1)
grid_search_lr.fit(X_train, y_train)

print("✅ Logistic Regression Best Params:", grid_search_lr.best_params_)
print("✅ Logistic Regression Best Accuracy:", grid_search_lr.best_score_)
```

---

## 🔹 Step 3: RandomForest Tuning (RandomizedSearchCV)

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
import numpy as np

rf = RandomForestClassifier(random_state=42)

param_dist = {
    "n_estimators": [50, 100, 200, 500],
    "max_depth": [None, 5, 10, 20],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4],
    "bootstrap": [True, False]
}

random_search_rf = RandomizedSearchCV(
    rf, param_dist, n_iter=10, cv=5, scoring="accuracy", random_state=42, n_jobs=-1
)
random_search_rf.fit(X_train, y_train)

print("✅ RandomForest Best Params:", random_search_rf.best_params_)
print("✅ RandomForest Best Accuracy:", random_search_rf.best_score_)
```

---

## 🔹 Step 4: Evaluate on Test Set

```python
from sklearn.metrics import accuracy_score

# Logistic Regression test accuracy
y_pred_lr = grid_search_lr.best_estimator_.predict(X_test)
print("Logistic Regression Test Accuracy:", accuracy_score(y_test, y_pred_lr))

# RandomForest test accuracy
y_pred_rf = random_search_rf.best_estimator_.predict(X_test)
print("RandomForest Test Accuracy:", accuracy_score(y_test, y_pred_rf))
```

---

## 🔹 Summary

* **Logistic Regression** → Simple model, interpretable, good baseline.
* **Random Forest** → More powerful, captures complex relations, better accuracy usually.
* **Tuning** helps in selecting **best parameters** → improves test performance.

---

## 🎯 Mini Task for You

1. Run tuning on **Loan dataset** (binary classification: approved / not approved).
2. Compare **Logistic Regression vs Random Forest**.
3. Plot confusion matrix for both.

---
