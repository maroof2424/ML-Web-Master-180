# 📘 Day 1 – Support Vector Machine (SVM) Introduction

## 🔹 What is SVM?

* **Support Vector Machine (SVM)** ek **supervised ML algorithm** hai.
* Mainly **classification** ke liye use hota hai (lekin regression ke liye bhi use ho sakta hai).
* Idea: Data ko **line (2D), plane (3D), hyperplane (nD)** se alag karna.

---

## 🔹 Key Concepts

1. **Hyperplane**

   * Decision boundary jo classes ko alag karta hai.
   * 2D me line, 3D me plane.

2. **Support Vectors**

   * Data points jo hyperplane ke sabse kareeb hote hain.
   * Ye boundary define karte hain.

3. **Margin**

   * Distance between hyperplane and nearest data points.
   * SVM tries to maximize this margin → better generalization.

---

## 🔹 Types of SVM

1. **Linear SVM** – Jab data linearly separable ho.
2. **Non-Linear SVM** – Jab data linearly separable na ho → use **Kernels** (e.g., RBF, polynomial).

---

## 🔹 Example Code (Classification with Linear SVM)

```python
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset (Iris)
iris = sns.load_dataset("iris")
X = iris.drop("species", axis=1)
y = iris["species"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train SVM
svm_model = SVC(kernel="linear")
svm_model.fit(X_train, y_train)

# Predictions
y_pred = svm_model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
```

---

## 🎯 Task for You

* Run the above code.
* Try different kernels:

  * `"linear"`, `"poly"`, `"rbf"`, `"sigmoid"`.
* Compare accuracy.

---
