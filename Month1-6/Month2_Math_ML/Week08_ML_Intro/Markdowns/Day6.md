# Day6

## 📘 Concept: Cross Validation (CV)

When we use a **single `train_test_split`**, our results may **depend too much on that split**.
👉 Example: If the test split accidentally has more difficult samples, accuracy will look bad (misleading).

That’s where **Cross Validation** helps.

---

### 🔹 1. Idea of Cross Validation

Instead of one split, we split the dataset into **K equal parts (folds)**.

1. Use **K-1 folds for training**, and **1 fold for testing**.
2. Repeat this process **K times**, each time using a different fold as test data.
3. Take the **average accuracy** across all folds.

---

### 🔹 2. K-Fold Example (k=5)

* Suppose you have 100 samples.
* Split into 5 folds of 20 samples each.
* Iterations:

  * Fold 1 → test, folds 2–5 → train
  * Fold 2 → test, folds 1,3–5 → train
  * … until every fold has been test once.

✅ Final performance = mean accuracy of all 5 runs.

---

### 🔹 3. Why is this Better?

* Reduces risk of unlucky splits.
* Uses all data for both **training** and **testing** (fairer estimate).
* Especially important if dataset is small.

---

### 🔹 4. In Scikit-learn

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import numpy as np

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Logistic Regression CV
log_reg = LogisticRegression(max_iter=1000)
scores_lr = cross_val_score(log_reg, X, y, cv=5)
print("Logistic Regression CV scores:", scores_lr)
print("Average Accuracy:", np.mean(scores_lr))

# Random Forest CV
rf = RandomForestClassifier()
scores_rf = cross_val_score(rf, X, y, cv=5)
print("\nRandom Forest CV scores:", scores_rf)
print("Average Accuracy:", np.mean(scores_rf))
```

---

#### 📊 Output (example)

```
Logistic Regression CV scores: [0.97 0.97 0.93 0.97 1.00]
Average Accuracy: 0.968

Random Forest CV scores: [0.97 0.97 0.97 0.97 0.97]
Average Accuracy: 0.97
```

---

✅ You can compare models more **reliably** with cross validation.

---
