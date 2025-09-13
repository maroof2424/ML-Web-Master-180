
# 📘 Day 7 → Export Pipeline with `joblib`

### 🔎 Concept

1. **Pipeline Export** ka matlab hai trained preprocessing + model ko save karna.

   * Har baar dataset clean + scale + encode + train karna time-consuming hota hai.
   * Ek baar pipeline bana ke save kar lo, aur baad me directly load karke use kar lo.

2. **Why?**

   * Reusability → Same pipeline dusre dataset parts par apply ho sakti hai.
   * Deployment → Web apps (FastAPI, Streamlit, Flask) me trained pipeline load hoti hai.
   * Consistency → Preprocessing steps bar-bar likhne ki zarurat nahi hoti.

3. **Tools**

   * `joblib` (preferred for sklearn objects, fast & efficient)
   * `pickle` (general-purpose python serialization)

---

# ✅ Example with Titanic Dataset

```python
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

# 1️⃣ Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

X = df[['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']]
y = df['Survived']

# 2️⃣ Define numeric & categorical features
numeric_features = ['Age', 'Fare']
categorical_features = ['Pclass', 'Sex', 'Embarked']

# 3️⃣ Preprocessing steps
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

# 4️⃣ Full pipeline
clf = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

# 5️⃣ Train-test split & model training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf.fit(X_train, y_train)
print(f"✅ Model Accuracy: {clf.score(X_test, y_test):.2f}")

# 6️⃣ Save pipeline
joblib.dump(clf, "titanic_pipeline.pkl")
print("📦 Pipeline saved as titanic_pipeline.pkl")

# 7️⃣ Load pipeline
loaded_model = joblib.load("titanic_pipeline.pkl")

# 8️⃣ Predict on new sample
sample = pd.DataFrame({
    "Pclass": [3],
    "Sex": ["male"],
    "Age": [22],
    "Fare": [7.25],
    "Embarked": ["S"]
})
prediction = loaded_model.predict(sample)
print("🎯 Prediction for new passenger:", prediction[0])  # 0 = not survived, 1 = survived
```

---

# 📒 Summary (Day 7 Notes)

* **Pipeline** = Preprocessing + Model combined.
* **Export** = Save trained pipeline (avoid retraining).
* **joblib** is best for scikit-learn pipelines.
* **Use case** → Deployment in APIs, Streamlit dashboards, production ML apps.

---
