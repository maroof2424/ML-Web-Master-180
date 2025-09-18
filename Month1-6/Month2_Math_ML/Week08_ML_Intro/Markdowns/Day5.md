# Day5
## 📘 Concept: `train_test_split`

When we build a machine learning model, our goal is to make it **generalize well** — meaning it should perform well not just on the data it has already seen (training data), but also on new, unseen data.

If we train and test on the same data:

* The model may "memorize" the data (overfit).
* We won’t know how it performs on unseen data.

👉 That’s why we **split our dataset** into two (or sometimes three) parts:

---

### 1. **Training Set**

* Used to **fit the model** (learn patterns).
* The algorithm adjusts weights/parameters from this data.

---

### 2. **Test Set**

* Used **only once at the end** to check performance.
* Simulates new, unseen data.
* Helps estimate how well the model will generalize.

---

### 3. (Optional) Validation Set

* Used during model development to tune hyperparameters.
* But in scikit-learn, we often use **cross-validation** instead of a separate validation set.

---

### 📊 How `train_test_split` Works

In `sklearn.model_selection`, the function works like this:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
```

* `X` = features
* `y` = target
* `test_size=0.3` → 30% data goes to **test set**, 70% to **train set**
* `random_state=42` → ensures reproducibility (same random split every time)

---

### ⚖️ Example Analogy

Think of it like **exams**:

* **Training set** = your class lectures and practice questions (you learn from them).
* **Test set** = final exam questions (new but from the same syllabus).

If you only practice past questions (train data), you might ace them but fail the exam (test data).

---

✅ So, the idea is:

* **Train** → teach the model.
* **Test** → check if the model learned the “concepts” or just memorized data.

---
