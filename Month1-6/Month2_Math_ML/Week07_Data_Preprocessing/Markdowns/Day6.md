# Week7 Day6
---

## 🛠️ What is a **Pipeline** in ML?

👉 A **Pipeline** in scikit-learn is a **sequence of steps** (like a factory assembly line) where **data flows through preprocessing → feature transformation → model training**.

It’s like a conveyor belt:

* Raw data goes in 🚪
* Each step (cleaning, scaling, encoding, model) happens in order ⚙️
* Final predictions come out 📊

---

### 🎯 Why use a Pipeline?

Without a pipeline:

* You separately **impute, scale, encode**, then train your model.
* You risk mistakes (e.g., forgetting to apply the same scaler on test data).
* Your code becomes messy.

With a pipeline:

* All steps are **chained together**.
* Training and test data go through the **exact same transformations**.
* You can **cross-validate** the *entire process* in one go.
* Makes deployment easy → single object (`clf.predict(new_data)`).

---

### ⚡ Example Analogy

Imagine making **tea** 🍵:

1. Boil water
2. Add tea leaves
3. Add milk/sugar
4. Pour into cup

Each step must happen **in the right order**.
That’s exactly how a pipeline works with data.

---

### ✅ In Code

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer

# Example: Pipeline for numeric features + model
pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),   # Handle missing values
    ("scaler", StandardScaler()),                    # Scale data
    ("classifier", LogisticRegression())             # Train model
])
```

Here:

1. Missing values → filled
2. Data → scaled
3. Logistic Regression → trained

You can now call:

```python
pipeline.fit(X_train, y_train)  
pipeline.predict(X_test)  
```

---

### 🚀 What it *does*

* Ensures **consistency** between train/test preprocessing
* **Reduces boilerplate code**
* Supports **cross-validation & grid search** automatically
* Makes your workflow **production-ready**

---
