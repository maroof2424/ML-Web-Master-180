

# 📘 Day 5 – GridSearchCV + RandomizedSearchCV

## 🔹 Concept

### 1. **GridSearchCV**

* Sabhi possible combinations of hyperparameters ko try karta hai.
* Har combination ke liye **cross-validation** run hoti hai.
* Best parameters + best score return karta hai.
* ❌ Downside: Bahut **slow** agar parameters ke values bohot zyada ho.

---

### 2. **RandomizedSearchCV**

* Har parameter ke liye ek **distribution/range** define karte hain.
* Random combinations pick karta hai (e.g., 20 random trials).
* ✅ Faster than GridSearchCV, specially jab parameter space bada ho.

---

## 🔹 Example 1: GridSearchCV (Random Forest on Titanic)

```python
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Titanic dataset
titanic = sns.load_dataset("titanic")
titanic = titanic[["pclass", "sex", "age", "fare", "survived"]].dropna()
titanic["sex"] = titanic["sex"].map({"male": 0, "female": 1})

X = titanic.drop("survived", axis=1)
y = titanic["survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
rf = RandomForestClassifier(random_state=42)

# Hyperparameter grid
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 5, 10],
    "min_samples_split": [2, 5, 10]
}

grid_search = GridSearchCV(rf, param_grid, cv=5, scoring="accuracy", n_jobs=-1)
grid_search.fit(X_train, y_train)

print("✅ Best Params:", grid_search.best_params_)
print("✅ Best Accuracy:", grid_search.best_score_)
```

---

## 🔹 Example 2: RandomizedSearchCV (SVM on Iris)

```python
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import RandomizedSearchCV
import numpy as np

iris = load_iris()
X, y = iris.data, iris.target

svm = SVC()

# Parameter distributions
param_dist = {
    "C": np.logspace(-3, 3, 7),   # [0.001, 0.01, 0.1, 1, 10, 100, 1000]
    "kernel": ["linear", "rbf", "poly"],
    "gamma": ["scale", "auto"]
}

random_search = RandomizedSearchCV(svm, param_dist, n_iter=10, cv=5, scoring="accuracy", random_state=42, n_jobs=-1)
random_search.fit(X, y)

print("✅ Best Params:", random_search.best_params_)
print("✅ Best Accuracy:", random_search.best_score_)
```

---

## 🔹 Summary

| Method             | Try All              | Faster   | Good for              |
| ------------------ | -------------------- | -------- | --------------------- |
| GridSearchCV       | ✅ Yes                | ❌ Slow   | Small parameter space |
| RandomizedSearchCV | ❌ No (Random Trials) | ✅ Faster | Large parameter space |

---

## 🎯 Mini Task for You

1. Titanic dataset → GridSearchCV with RandomForest.
2. Iris dataset → RandomizedSearchCV with SVM.
3. Compare results: GridSearch vs RandomizedSearch.

---

