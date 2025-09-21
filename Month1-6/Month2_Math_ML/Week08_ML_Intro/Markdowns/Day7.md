

# 📘 Day 7 – Titanic ML Pipeline

### 🔹 Concept

By now, we have learned:

* Handling nulls / scaling / encoding (Week 7)
* Train-test split, CV (Week 8)

Now we combine everything into a **single sklearn Pipeline** so that:

1. Preprocessing (imputation, encoding, scaling)
2. Model training (LogReg / RandomForest)

… all happen in one pipeline ✅

---

## 🔹 Steps

### 1. Import & Load Titanic Dataset

```python
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Load Titanic dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

df.head()
```

---

### 2. Define Features & Target

```python
X = df.drop("Survived", axis=1)
y = df["Survived"]

# Select useful features
categorical = ["Sex", "Embarked", "Pclass"]
numerical = ["Age", "Fare"]
```

---

### 3. Build Preprocessor

```python
# Preprocessing for numerical features
num_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

# Preprocessing for categorical features
cat_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

# Combine both
preprocessor = ColumnTransformer(
    transformers=[
        ("num", num_transformer, numerical),
        ("cat", cat_transformer, categorical)
    ])
```

---

### 4. Create Final Pipeline with Model

```python
# Logistic Regression pipeline
log_reg_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Random Forest pipeline
rf_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42))
])
```

---

### 5. Train & Evaluate

```python
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression
log_reg_pipeline.fit(X_train, y_train)
print("Logistic Regression Accuracy:", log_reg_pipeline.score(X_test, y_test))

# Random Forest
rf_pipeline.fit(X_train, y_train)
print("Random Forest Accuracy:", rf_pipeline.score(X_test, y_test))
```

---

### 6. Cross Validation

```python
scores_lr = cross_val_score(log_reg_pipeline, X, y, cv=5)
scores_rf = cross_val_score(rf_pipeline, X, y, cv=5)

print("LogReg CV Avg:", scores_lr.mean())
print("RandomForest CV Avg:", scores_rf.mean())
```

---

### ✅ Key Takeaway

* Pipeline keeps all preprocessing + model training steps together.
* Easy to save/load later with `joblib`.
* Prevents **data leakage** (test set never leaks into preprocessing).

---