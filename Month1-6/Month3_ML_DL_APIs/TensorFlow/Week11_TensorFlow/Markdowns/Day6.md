
## 🧠 **Day 6 – Mini Project: Binary Classification ANN**

### 🎯 **Goal**

Build and train a **complete ANN model** for a **real-world binary classification** problem such as:

* 📰 **Fake News Detection**
* 💳 **Customer Churn Prediction**
* 💰 **Loan Default Prediction**

---

## ⚙️ **1. Problem Setup**

We’ll demonstrate with the **Loan Default Prediction** dataset (you can replace it with any binary dataset).
**Target column:** `Loan_Status` (1 = Approved, 0 = Not Approved)

---

### 🧩 **2. Steps Overview**

1️⃣ Load and clean dataset
2️⃣ Encode categorical features
3️⃣ Split train/test
4️⃣ Scale numerical columns
5️⃣ Build ANN
6️⃣ Train, evaluate, and save model

---

## 💻 **3. Implementation**

```python
# Day 6: Mini Project – Binary Classification ANN

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import load_model

# Load dataset
url = "https://raw.githubusercontent.com/ybifoundation/Dataset/main/Loan%20Approval.csv"
df = pd.read_csv(url)
df.head()
```

---

### 🔍 4️⃣ **Preprocessing**

```python
# Encode categorical features
le = LabelEncoder()
for col in df.select_dtypes('object').columns:
    df[col] = le.fit_transform(df[col])

# Separate features and target
X = df.drop('Loan_Status', axis=1)
y = df['Loan_Status']

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

---

### 🧠 5️⃣ **Build ANN Model**

```python
from tensorflow.keras.optimizers import Adam

model = Sequential([
    Dense(16, input_dim=X_train.shape[1], activation='relu'),
    Dropout(0.3),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')  # Binary output
])

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.summary()
```

---

### ⚡ 6️⃣ **Train Model**

```python
history = model.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    epochs=50,
    batch_size=16,
    verbose=1
)
```

---

### 📊 7️⃣ **Evaluate Performance**

```python
import matplotlib.pyplot as plt

# Plot accuracy
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.legend()
plt.title("Model Accuracy")
plt.show()

# Evaluate on test data
loss, acc = model.evaluate(X_test, y_test, verbose=0)
print(f"✅ Test Accuracy: {acc:.3f}")
```

---

### 📈 8️⃣ **Confusion Matrix**

```python
from sklearn.metrics import confusion_matrix, classification_report

y_pred = (model.predict(X_test) > 0.5).astype("int32")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

---

### 💾 9️⃣ **Save & Load Model**

```python
# Save model
model.save('my_ann_model.h5')
print("✅ Model saved successfully!")

# Load model
loaded_model = load_model('my_ann_model.h5')

# Verify loaded model
loss, acc = loaded_model.evaluate(X_test, y_test, verbose=0)
print(f"🔁 Loaded Model Accuracy: {acc:.3f}")
```

---

## 🧩 **Mini Challenges**

* Add **Dropout layers** to prevent overfitting.
* Tune **learning rate**, **epochs**, and **batch size**.
* Add more layers to see if accuracy improves.
* Test with **Churn** or **Fake News dataset**.

---

## 🏁 **Outcome**

By the end of Day 6, you’ll:
✅ Build a real ANN model for binary classification
✅ Evaluate with real metrics
✅ Save + reload the trained model

---