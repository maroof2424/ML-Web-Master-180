# 📘 Day 3 – Random Forest + Feature Importance

## 🔹 Concept Recap

* **Random Forest** = Ensemble of **Decision Trees**.
* Har tree random subset of data + features pe train hota hai (Bagging).
* Prediction:

  * **Classification** → majority vote
  * **Regression** → average

✅ Pros:

* Robust, handles noise well
* Works on both classification & regression
* Provides **feature importance**

---

## 🔹 Code Example (Classification – Titanic)

```python
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Titanic dataset
titanic = sns.load_dataset("titanic")
titanic = titanic[["pclass", "sex", "age", "fare", "survived"]].dropna()

# Encode categorical feature
titanic["sex"] = titanic["sex"].map({"male": 0, "female": 1})

X = titanic.drop("survived", axis=1)
y = titanic["survived"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest model
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Predictions
y_pred = rf.predict(X_test)

print("Test Accuracy:", accuracy_score(y_test, y_pred))
```

---

## 🔹 Feature Importance

```python
# Feature importance
importances = rf.feature_importances_
features = X.columns

# Show importance
feat_df = pd.DataFrame({"Feature": features, "Importance": importances})
print(feat_df.sort_values(by="Importance", ascending=False))

# Plot
plt.figure(figsize=(6,4))
plt.barh(features, importances)
plt.xlabel("Importance")
plt.ylabel("Features")
plt.title("Random Forest Feature Importance")
plt.show()
```

---

## 🔹 Mini Task for You

1. Run Random Forest on **Titanic dataset**.
2. Plot **feature importance**.
3. Try regression version on `tips` dataset (predict `tip`).

---
