

# ✅ Day 7 – Review & Summary

## 📌 What We Learned in Week 9:

### 🔹 Regression

* **Linear Regression** → Continuous prediction (e.g., house price).
* **Metrics** → MAE, RMSE, R².

### 🔹 Logistic Regression

* **Binary classification** (0/1, Yes/No).
* Uses **Sigmoid function** for probabilities.

### 🔹 KNN

* Predicts based on **nearest neighbors**.
* **K** choice matters (too small → noisy, too large → underfit).

### 🔹 Decision Trees

* Splits data into **if/else rules**.
* Can be used for **both regression & classification**.

### 🔹 Evaluation Metrics

* **Regression:** MAE, RMSE.
* **Classification:** Accuracy, Confusion Matrix, Precision, Recall, F1.

### 🔹 Model Comparison

* Built **multiple models** and compared results.
* Learned that **no single model is best for all datasets**.

---

## 🎯 Mini Task (Revision):

1. Load **Titanic dataset**.
2. Train **Logistic Regression, Decision Tree, Random Forest**.
3. Compare Accuracy & Confusion Matrix.

```python
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load Titanic dataset
titanic = sns.load_dataset("titanic").dropna(subset=["age","fare","sex","class","survived"])
X = titanic[["age","fare"]]
X["sex"] = titanic["sex"].map({"male":0,"female":1})
y = titanic["survived"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Models
models = {
    "Logistic Regression": LogisticRegression(max_iter=200),
    "Decision Tree": DecisionTreeClassifier(max_depth=5, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
}

# Train & Evaluate
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"\n🔎 {name}")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
```

--- 