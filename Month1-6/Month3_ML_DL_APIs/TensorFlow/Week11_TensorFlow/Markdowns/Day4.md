
## 📘 **Day 4: Binary Classification ANN**

### 🎯 **Goal**

Build and evaluate a **Binary Classification Artificial Neural Network (ANN)** using **TensorFlow/Keras**.
We’ll classify data into **two categories** (e.g., Titanic Survival, Spam Detection, or Loan Approval).

---

### 🧠 **1. Concept Overview**

A **binary classifier** outputs either:

* `1` → positive class (e.g., survived / spam / approved)
* `0` → negative class (e.g., didn’t survive / not spam / rejected)

ANN Flow:
**Input Layer → Hidden Layer(s) with ReLU → Output Layer with Sigmoid**

---

### ⚙️ **2. Model Architecture**

| Layer                   | Description                        | Activation |
| ----------------------- | ---------------------------------- | ---------- |
| **Input**               | Features (e.g., Age, Income, etc.) | –          |
| **Hidden 1**            | Learns complex relationships       | ReLU       |
| **Hidden 2 (optional)** | Adds depth                         | ReLU       |
| **Output**              | Predicts probability (0–1)         | Sigmoid    |

---

### 💻 **3. Code Example (Titanic Dataset)**

```python
# Day 4: Binary Classification ANN
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.metrics import Precision, Recall

# 1️⃣ Load dataset
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# 2️⃣ Preprocess data
df = df[["Pclass", "Sex", "Age", "Fare", "Survived"]]
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df = df.dropna()

X = df.drop("Survived", axis=1)
y = df["Survived"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3️⃣ Build ANN model
model = Sequential([
    Dense(16, input_dim=X_train.shape[1], activation='relu'),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')   # Binary output
])

# 4️⃣ Compile
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy', Precision(name='precision'), Recall(name='recall')]
)

# 5️⃣ Train
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=25, batch_size=16, verbose=1)

# 6️⃣ Evaluate
results = model.evaluate(X_test, y_test, verbose=0)
print(f"Accuracy: {results[1]:.3f}, Precision: {results[2]:.3f}, Recall: {results[3]:.3f}")
```

---

### 📊 **4. Visualize Training**

```python
import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title("Model Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.show()
```

---

### 🧮 **5. Metrics Explanation**

| Metric        | Meaning                                    |
| ------------- | ------------------------------------------ |
| **Accuracy**  | % of correct predictions                   |
| **Precision** | % of predicted positives that were correct |
| **Recall**    | % of actual positives correctly predicted  |

🧠 *Use precision for spam detection, recall for medical/fraud detection.*

---

### 🧩 **6. Mini Tasks**

1. Change optimizer from `adam` → `sgd` → `rmsprop` and compare accuracy.
2. Try adding another hidden layer — does accuracy improve?
3. Change dataset (Spam or Loan) and rebuild.

---

### 🏁 **Outcome**

By end of Day 4, you’ll:
✅ Understand binary ANN structure
✅ Train & evaluate using Keras
✅ Interpret accuracy, precision, and recall

---
