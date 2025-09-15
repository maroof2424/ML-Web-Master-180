# 📅 **Week 8 – ML Concepts & Preprocessing Pipeline**

### ✅ **Day 1 → `01_linear_regression.ipynb`**

* Concept: Regression (continuous prediction)
* Simple Linear Regression formula: $y = mx + c$
* Code on small dataset (e.g., sklearn `make_regression`)
* Visualize regression line.

---

### ✅ **Day 2 → `02_logistic_regression.ipynb`**

* Concept: Classification (0/1 prediction)
* Logistic function (Sigmoid curve)
* Apply Logistic Regression on Titanic dataset (Survived = target).
* Compare accuracy vs linear regression.

---

### ✅ **Day 3 → `03_classification.ipynb`**

* Different classifiers intro: Decision Tree, Random Forest, KNN.
* Compare classifiers on small dataset (`sklearn.datasets.load_iris`).
* Visualize decision boundaries (if possible).

---

### ✅ **Day 4 → `04_overfit_underfit.ipynb`**

* Concept: Overfitting (low bias, high variance) vs Underfitting (high bias).
* Train Decision Tree with low depth (underfit) vs high depth (overfit).
* Plot train vs test accuracy.

---

### ✅ **Day 5 → `05_train_test.ipynb`**

* Use `train_test_split` on Titanic dataset.
* Train model on train data → Test on test data.
* Compare accuracy on both sets.

---

### ✅ **Day 6 → `06_cross_validation.ipynb`**

* Concept: Why single split may mislead.
* Perform K-Fold Cross Validation (k=5).
* Show average accuracy.
* Compare Logistic Regression vs Random Forest.

---

### ✅ **Day 7 → `07_titanic_pipeline.ipynb`**

* Build **full preprocessing + ML pipeline**:

  * Handle missing values.
  * Scale numeric features.
  * Encode categorical features.
  * Train Logistic Regression model.
* Save pipeline using `joblib`.
* Load and test with sample input.

---

👉 End of **Week 8** you will have:

* Clear concepts: Regression, Classification, Overfitting, Underfitting.
* Hands-on: Train/Test split, Cross-validation.
* A **reusable Titanic pipeline** that you can load anytime.

---
