# 📘 Day 3 – Classification

---

## **1. What is Classification?**

* **Definition**: Classification is a **supervised learning task** where the goal is to predict a **category (label)** instead of a number.
* Example:

  * Spam vs Not Spam (Binary Classification)
  * Type of flower (Setosa, Versicolor, Virginica → Multi-class Classification)

---

## **2. Difference from Regression**

* **Regression** → predicts continuous values (e.g., house price).
* **Classification** → predicts discrete classes (e.g., cat 🐱 or dog 🐶).

---

## **3. Popular Classification Algorithms**

1. **Decision Tree**

   * Splits dataset into smaller groups using “if/else” rules.
   * Easy to interpret.
   * Problem: can overfit if tree is too deep.

2. **Random Forest**

   * An **ensemble** of many decision trees.
   * Each tree is trained on a random subset of data.
   * Improves accuracy & reduces overfitting.

3. **K-Nearest Neighbors (KNN)**

   * Looks at the “k” closest points to decide class.
   * Simple, but slower for large datasets.

---

## **4. Model Evaluation Metrics**

* **Accuracy** = (Correct Predictions) ÷ (Total Predictions).
* **Precision** = True Positives ÷ (True Positives + False Positives).
* **Recall** = True Positives ÷ (True Positives + False Negatives).
* **F1 Score** = Harmonic mean of Precision & Recall.
* **Confusion Matrix** = Table showing correct vs incorrect predictions.

---

## **5. Decision Boundaries**

* Visual representation of how the classifier separates different classes in feature space.
* Example: If using Iris dataset with Sepal length & width:

  * **KNN** → boundaries look “curvy” (depends on neighbors).
  * **Decision Tree** → sharp rectangular boundaries.
  * **Random Forest** → smoother but still step-like boundaries.

---

✅ **Key Takeaway**:

* Classification helps predict **labels**.
* Different models → different strengths (trees = interpretable, forests = strong performance, KNN = simple & intuitive).
* Always evaluate using accuracy, precision, recall, and visualization.

---