# 📘 Day 2 – KNN Tuning (n_neighbors, metrics)

## 🔹 Recap of KNN

* **K-Nearest Neighbors (KNN)** ek **lazy learner** algorithm hai.
* Jab prediction karna hota hai → ye query point ke **k nearest neighbors** dekhta hai, phir **majority vote (classification)** ya **average (regression)** se result nikalta hai.

---

## 🔹 Hyperparameters to Tune

1. **`n_neighbors`** → Kitne neighbors lene hain (default=5).

   * Chhota `k` → model zyada sensitive (overfit ho sakta hai).
   * Bada `k` → smooth decision boundary (underfit ho sakta hai).

2. **`metric`** → Distance measure.

   * `"euclidean"` (default)
   * `"manhattan"`
   * `"minkowski"`
   * `"chebyshev"`

3. **`weights`**

   * `"uniform"` → sab neighbors equal vote dete hain.
   * `"distance"` → near neighbors ka vote zyada weight rakhta hai.

---

## 🔹 Example Code (Classification with Tuning)

```python
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Dataset
iris = sns.load_dataset("iris")
X = iris.drop("species", axis=1)
y = iris["species"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Base KNN
knn = KNeighborsClassifier()

# Hyperparameter grid
param_grid = {
    "n_neighbors": [3, 5, 7, 9, 11],
    "metric": ["euclidean", "manhattan", "chebyshev"],
    "weights": ["uniform", "distance"]
}

# GridSearchCV for tuning
grid = GridSearchCV(knn, param_grid, cv=5, scoring="accuracy")
grid.fit(X_train, y_train)

# Best parameters
print("Best Params:", grid.best_params_)
print("Best CV Accuracy:", grid.best_score_)

# Evaluate on test set
y_pred = grid.best_estimator_.predict(X_test)
print("Test Accuracy:", accuracy_score(y_test, y_pred))
```

---

## 🔹 Mini Task for You

1. Run the above code.
2. Check **best parameters** for your dataset.
3. Plot **accuracy vs n_neighbors** (line graph).

---