

## ✅ Day 3 → `03_knn.ipynb`

### 🔑 Concepts:

**K-Nearest Neighbors (KNN)** ek **lazy learner** hai:

* Prediction ke liye training data store karta hai.
* Naya point predict karne ke liye **distance (Euclidean/Manhattan)** measure karta hai aur **k nearest neighbors** ko dekhta hai.
* Classification → **majority vote** (sabse zyada class neighbors ki).
* Regression → **average value** of neighbors.

---

### 🧮 Formula (Euclidean Distance):

$$
d(p,q) = \sqrt{ \sum (p_i - q_i)^2 }
$$

---

## 🐍 Code Example

### 1️⃣ KNN Classification (Iris dataset)

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
knn_clf = KNeighborsClassifier(n_neighbors=5)
knn_clf.fit(X_train, y_train)

# Predict
y_pred = knn_clf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
```

---

### 2️⃣ KNN Regression (Tips dataset)

```python
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

# Load dataset
df = sns.load_dataset("tips")

X = df[["total_bill"]]
y = df["tip"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
knn_reg = KNeighborsRegressor(n_neighbors=5)
knn_reg.fit(X_train, y_train)

# Predict
y_pred = knn_reg.predict(X_test)

# Metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("MSE:", mse)
print("RMSE:", rmse)
```

---
