

## ✅ Day 4 → `04_decision_tree.ipynb`

### 🔑 Concepts:

* **Decision Tree** ek supervised ML algorithm hai jo **classification** aur **regression** dono ke liye use hota hai.
* Ye data ko **if/else rules** me todta hai (nodes → branches → leaves).
* **Splitting criteria:**

  * **Gini Index**
  * **Entropy / Information Gain**
  * For regression → **MSE / MAE**
* Pros:

  * Easy to visualize & interpret
  * Non-linear data handle kar sakta hai
* Cons:

  * Overfitting (tree bahut deep ho jaye)

---

### 🐍 Code Example

#### 1️⃣ Decision Tree on Titanic Dataset

```python
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

# Titanic dataset
titanic = sns.load_dataset("titanic")
df = titanic[["sex", "age", "fare", "class", "survived"]].dropna()

# Encode categorical
df["sex"] = df["sex"].map({"male": 0, "female": 1})
df["class"] = df["class"].map({"First": 1, "Second": 2, "Third": 3})

X = df[["sex", "age", "fare", "class"]]
y = df["survived"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Decision Tree
tree_clf = DecisionTreeClassifier(max_depth=3, random_state=42)
tree_clf.fit(X_train, y_train)

# Predict
y_pred = tree_clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Visualize tree
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
plot_tree(tree_clf, feature_names=X.columns, class_names=["Died","Survived"], filled=True)
plt.show()
```

---

#### 2️⃣ Change `max_depth` → See Underfitting vs Overfitting

```python
for depth in [2, 3, 5, None]:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    print(f"Max Depth = {depth}, Accuracy = {acc:.3f}")
```

---
 