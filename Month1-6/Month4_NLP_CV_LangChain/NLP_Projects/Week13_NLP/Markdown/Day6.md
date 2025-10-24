## **Day 6 — NLP Mini Project
### 🎯 **Goal**

Build a **text sentiment classifier** that predicts **positive** or **negative** sentiment using:

* **TF-IDF vectorization** (text → numbers)
* **Naive Bayes** or **Logistic Regression**
* **Accuracy, precision, recall evaluation**

---

## 🧠 **Concept Recap**

| Step | Concept        | Description                                             |
| ---- | -------------- | ------------------------------------------------------- |
| 1️⃣  | Text Cleaning  | Remove unwanted characters, lowercase, etc.             |
| 2️⃣  | Tokenization   | Split sentences into words                              |
| 3️⃣  | TF-IDF         | Convert text into numeric vectors                       |
| 4️⃣  | Model Training | Train a classifier (Naive Bayes or Logistic Regression) |
| 5️⃣  | Evaluation     | Measure accuracy, precision, recall                     |

---

## ⚙️ **Setup**

```bash
!pip install scikit-learn pandas nltk
```

---

## 📂 **1. Import Libraries**

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
```

---

## 📄 **2. Sample Dataset (Custom or Built-in)**

Let’s create a **small sample dataset** for testing:

```python
data = {
    'text': [
        'I love this product, it is amazing!',
        'Worst experience ever, totally disappointed',
        'Great quality and fast delivery',
        'Horrible, I will never buy this again',
        'Excellent value for money!',
        'Terrible customer service',
        'I am happy with the purchase',
        'I hate this so much'
    ],
    'label': [1, 0, 1, 0, 1, 0, 1, 0]  # 1=Positive, 0=Negative
}

df = pd.DataFrame(data)
df
```

---

## ✂️ **3. Split into Train & Test**

```python
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.3, random_state=42)
```

---

## 🔢 **4. TF-IDF Vectorization**

```python
tfidf = TfidfVectorizer(stop_words='english', max_features=1000)
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)
```

---

## 🤖 **5. Train the Model**

### Option 1 — Naive Bayes

```python
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)
```

### Option 2 — Logistic Regression (optional)

```python
from sklearn.linear_model import LogisticRegression
# model = LogisticRegression()
# model.fit(X_train_tfidf, y_train)
```

---

## 📈 **6. Evaluate the Model**

```python
y_pred = model.predict(X_test_tfidf)

print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
```

---

## 🧠 **7. Test on New Sentences**

```python
new_texts = [
    "I really liked this movie!",
    "It was a waste of money",
    "Not bad but could be better"
]

new_vecs = tfidf.transform(new_texts)
preds = model.predict(new_vecs)

for text, p in zip(new_texts, preds):
    sentiment = "😊 Positive" if p == 1 else "😡 Negative"
    print(f"{text} → {sentiment}")
```

---

## 💾 **8. Save Model & Vectorizer**

```python
import joblib

joblib.dump(model, "sentiment_model.pkl")
joblib.dump(tfidf, "tfidf_vectorizer.pkl")
print("✅ Model and vectorizer saved!")
```

---

## 🧩 **9. Reload and Predict Later**

```python
model = joblib.load("sentiment_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

sample = ["The service was excellent and staff were friendly"]
vec = tfidf.transform(sample)
print("Prediction:", model.predict(vec))
```

---

## ✅ **Summary Table**

| Step | Concept          | Function                                 |
| ---- | ---------------- | ---------------------------------------- |
| 1    | TF-IDF           | `TfidfVectorizer()`                      |
| 2    | Train/Test Split | `train_test_split()`                     |
| 3    | Model Training   | `MultinomialNB().fit()`                  |
| 4    | Evaluation       | `accuracy_score()`, `confusion_matrix()` |
| 5    | Save Model       | `joblib.dump()`                          |

---