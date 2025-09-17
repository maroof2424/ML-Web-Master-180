# 📘 Day 4 – Overfitting vs Underfitting

---

## **1. What is Underfitting?**

* Model is **too simple** → cannot capture the patterns in data.
* Symptoms:

  * Both **train** and **test accuracy are low**.
  * High **bias** (wrong assumptions about data).
* Example: Using a straight line to fit a curved dataset.

---

## **2. What is Overfitting?**

* Model is **too complex** → learns noise & memorizes training data.
* Symptoms:

  * **Train accuracy = very high (≈100%)**
  * **Test accuracy = low** → poor generalization.
  * High **variance** (model changes drastically with small data changes).

---

## **3. The Bias–Variance Tradeoff**

* **Bias** = error from wrong assumptions (underfitting).
* **Variance** = error from model being too sensitive to training data (overfitting).
* Goal = **balance** bias & variance → “just right” model.

---

## **4. Mini Experiment: Decision Tree Depth**

1. Use a dataset (Iris or Titanic).
2. Train **Decision Tree Classifier** with:

   * Very shallow depth (e.g., `max_depth=1`) → **underfit**.
   * Very deep tree (e.g., `max_depth=None`) → **overfit**.
3. Compare:

   * Training Accuracy
   * Test Accuracy
   * Plot both vs depth.

---

## **5. Visualization**

* **Underfit curve** → both train & test accuracy low.
* **Overfit curve** → train accuracy high, test accuracy drops.
* ✅ Best depth = where **train & test accuracies are closest** and both are reasonably high.

---

### ✅ Notebook Flow (`04_overfit_underfit.ipynb`)

* Section 1: Explain concepts (bias, variance).
* Section 2: Load dataset (Iris/Titanic).
* Section 3: Train Decision Trees with different depths.
* Section 4: Plot train vs test accuracy curve.
* Section 5: Conclude where model is balanced.

---