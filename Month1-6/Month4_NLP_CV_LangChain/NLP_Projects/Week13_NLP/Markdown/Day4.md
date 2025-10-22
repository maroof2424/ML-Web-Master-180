# **Day 4: Sentiment Analysis**

## 🧠 Objective

Build a **Sentiment Analysis model** (Positive / Negative) using:

* Preprocessing
* TF-IDF vectorization
* **Naive Bayes** or **Logistic Regression**

---

## 📂 Directory

`Month4_NLP/Week13_NLP/04_sentiment_model.ipynb`

---

## 🧾 Step-by-Step Tutorial

### **1️⃣ Import Libraries**

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
```

---

### **2️⃣ Load Dataset**

You can use:

* `nltk.corpus.movie_reviews`
* or your own dataset like IMDB or Twitter Sentiment

Example using custom data 👇

```python
data = {
    'text': [
        "I love this movie, it was fantastic!",
        "This film is terrible and boring.",
        "Amazing experience, great acting!",
        "Not good, very disappointing.",
        "Loved it! The direction was brilliant.",
        "Worst movie ever made."
    ],
    'sentiment': ['positive', 'negative', 'positive', 'negative', 'positive', 'negative']
}

df = pd.DataFrame(data)
df.head()
```

---

### **3️⃣ Preprocess Data**

(Optional but important for real projects)

```python
import re
import string

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = re.sub(r"\d+", "", text)
    text = text.strip()
    return text

df['clean_text'] = df['text'].apply(clean_text)
df.head()
```

---

### **4️⃣ Split Train/Test**

```python
X_train, X_test, y_train, y_test = train_test_split(
    df['clean_text'], df['sentiment'], test_size=0.3, random_state=42
)
```

---

### **5️⃣ Convert Text → TF-IDF Features**

```python
vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print("Feature vector shape:", X_train_tfidf.shape)
```

---

### **6️⃣ Train Models**

#### Option 1: Naive Bayes

```python
nb_model = MultinomialNB()
nb_model.fit(X_train_tfidf, y_train)
y_pred_nb = nb_model.predict(X_test_tfidf)
```

#### Option 2: Logistic Regression

```python
lr_model = LogisticRegression(max_iter=500)
lr_model.fit(X_train_tfidf, y_train)
y_pred_lr = lr_model.predict(X_test_tfidf)
```

---

### **7️⃣ Evaluate Models**

```python
def evaluate_model(y_true, y_pred, model_name):
    print(f"\n🔹 Model: {model_name}")
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("\nClassification Report:\n", classification_report(y_true, y_pred))
    sns.heatmap(confusion_matrix(y_true, y_pred), annot=True, fmt='d', cmap='Blues')
    plt.title(f"{model_name} - Confusion Matrix")
    plt.show()

evaluate_model(y_test, y_pred_nb, "Naive Bayes")
evaluate_model(y_test, y_pred_lr, "Logistic Regression")
```

---

### **8️⃣ Save Model for Reuse**

```python
import joblib

joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
joblib.dump(lr_model, "sentiment_model.pkl")

# Load later with:
# vectorizer = joblib.load("tfidf_vectorizer.pkl")
# model = joblib.load("sentiment_model.pkl")
```

---

### **9️⃣ Test with New Input**

```python
sample = ["This product is really good!", "I hated the movie, waste of time."]
sample_tfidf = vectorizer.transform(sample)
predictions = lr_model.predict(sample_tfidf)

for text, sentiment in zip(sample, predictions):
    print(f"{text} → {sentiment}")
```

---

## 🧩 Summary Table

| Step | Task             | Key Concept              |
| ---- | ---------------- | ------------------------ |
| 1    | Import libraries | Setup                    |
| 2    | Load dataset     | Raw text                 |
| 3    | Clean text       | Preprocessing            |
| 4    | Split data       | Train/Test               |
| 5    | TF-IDF           | Text → Numbers           |
| 6    | Train models     | NB / Logistic Regression |
| 7    | Evaluate         | Accuracy, F1-score       |
| 8    | Save model       | joblib                   |
| 9    | Predict new text | Inference                |

---

### 🎯 **Mini Challenge**

Try training both models (Naive Bayes + Logistic Regression) and compare:

* Accuracy
* Precision, Recall, F1-score
  Plot their results on the same chart 📊

---
