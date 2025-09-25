# ✅ Day 5 – Evaluation Metrics

Decision Trees, Regression, or Classification models ki **accuracy aur performance** check karna bahut zaroori hai. Different metrics use hote hain depending on the task:

---

## 1️⃣ Regression Metrics

### a) **MAE (Mean Absolute Error)**

* Average of absolute differences between predicted & actual values.
* Simple, interpretable.

$$
\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
$$

### b) **RMSE (Root Mean Squared Error)**

* Square root of average squared differences.
* Penalizes large errors more than MAE.

$$
\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
$$

### 🐍 Python Code Example (Regression):

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# y_test = actual, y_pred = predicted
y_test = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("✅ MAE:", mae)
print("✅ RMSE:", rmse)
```

---

## 2️⃣ Classification Metrics

### a) **Accuracy**

* Percentage of correct predictions.

$$
\text{Accuracy} = \frac{\text{Correct Predictions}}{\text{Total Predictions}}
$$

### b) **Confusion Matrix**

* True Positive (TP), True Negative (TN), False Positive (FP), False Negative (FN)
* Helps visualize performance per class.

### c) **Precision, Recall, F1-Score**

* **Precision:** Correct positive predictions out of all predicted positives.
* **Recall:** Correct positive predictions out of all actual positives.
* **F1-Score:** Harmonic mean of Precision & Recall.

### 🐍 Python Code Example (Classification):

```python
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Dataset
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Train model
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# Predictions
y_pred = clf.predict(X_test)

# Metrics
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("✅ Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("✅ Classification Report:\n", classification_report(y_test, y_pred))
```

---

## 🔑 Key Notes:

* **Regression:** MAE & RMSE most common. RMSE penalizes bigger errors more.
* **Classification:** Accuracy is simple, but confusion matrix + precision/recall/F1 gives deeper insight.
* Always **visualize predictions** with scatter or bar plots to see model fit.

---
