# ✅ Day 2 – Logistic Regression (Titanic Dataset)

**Notebook:** `02_logistic_regression.ipynb`

---

## **Concept**

* **Logistic Regression** is used for **classification problems** (binary or multi-class).
* Unlike Linear Regression, it predicts probabilities using the **sigmoid function**:

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

* The output lies between **0 and 1** → can be interpreted as probability.
* For Titanic dataset:

  * **Target:** `Survived` (0 = No, 1 = Yes)
  * **Features:** e.g., `Pclass`, `Sex`, `Age`, `Fare`

---

## **Code**

```python
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load Titanic dataset from seaborn
df = sns.load_dataset("titanic")

# Keep only important columns
df = df[['survived', 'pclass', 'sex', 'age', 'fare']]
df.dropna(inplace=True)  # remove missing values

# Encode categorical column 'sex'
le = LabelEncoder()
df['sex'] = le.fit_transform(df['sex'])  # male=1, female=0

# Features and target
X = df[['pclass', 'sex', 'age', 'fare']]
y = df['survived']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression model
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train, y_train)

# Predictions
y_pred = log_reg.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
print(f"✅ Logistic Regression Accuracy: {acc:.4f}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", cm)

# Detailed Report
print("\nClassification Report:\n", classification_report(y_test, y_pred))
```

---

## **Expected Results**

* **Accuracy** \~ 75–80% (depending on preprocessing).
* **Confusion Matrix**: shows true vs predicted survival.
* **Classification Report**: precision, recall, F1-score.

---

## **Comparison vs Linear Regression**

If you use **Linear Regression** on the same dataset:

* Predictions are **continuous values** (not 0/1).
* You’d need to **threshold** (e.g., `>=0.5 = 1 else 0`) to classify.
* Logistic Regression is **better suited** for classification because it directly models probability.

---
