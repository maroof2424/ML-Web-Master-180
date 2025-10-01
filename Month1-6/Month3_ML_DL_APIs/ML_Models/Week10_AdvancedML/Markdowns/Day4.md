# 📘 Day 4 – Feature Importance Visualization

## 🔹 Concept

* **Feature importance** batata hai ki model ke liye kaunsa feature prediction me zyada contribute kar raha hai.
* Mostly use hota hai **Tree-based models** (Decision Tree, Random Forest, XGBoost).
* Visualization ke liye bar charts, horizontal bars, aur sorted plots use karte hain.

---

## 🔹 Example 1: Random Forest (Titanic Dataset)

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load Titanic dataset
titanic = sns.load_dataset("titanic")
titanic = titanic[["pclass", "sex", "age", "fare", "survived"]].dropna()

# Encode categorical
titanic["sex"] = titanic["sex"].map({"male": 0, "female": 1})

X = titanic.drop("survived", axis=1)
y = titanic["survived"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Feature importance
importances = rf.feature_importances_
features = X.columns

# Visualization
feat_df = pd.DataFrame({"Feature": features, "Importance": importances}).sort_values(by="Importance", ascending=True)

plt.figure(figsize=(7,4))
plt.barh(feat_df["Feature"], feat_df["Importance"], color="skyblue")
plt.xlabel("Importance Score")
plt.title("Feature Importance (Random Forest - Titanic)")
plt.show()
```

---

## 🔹 Example 2: Decision Tree (Tips Dataset - Regression)

```python
from sklearn.tree import DecisionTreeRegressor

# Load dataset
tips = sns.load_dataset("tips").dropna()

X = tips[["total_bill", "size"]]
y = tips["tip"]

# Train model
dt = DecisionTreeRegressor(max_depth=4, random_state=42)
dt.fit(X, y)

# Feature importance
importances = dt.feature_importances_
features = X.columns

plt.figure(figsize=(5,3))
plt.bar(features, importances, color="orange")
plt.ylabel("Importance")
plt.title("Feature Importance (Decision Tree - Tips)")
plt.show()
```

---

## 🔹 Mini Task for You

1. Titanic dataset → Random Forest importance.
2. Tips dataset → Decision Tree regression importance.
3. Compare: kis dataset me **feature ka weight** zyada hai?

---