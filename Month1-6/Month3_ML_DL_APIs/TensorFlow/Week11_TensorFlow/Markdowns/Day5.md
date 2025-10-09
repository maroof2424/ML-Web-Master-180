

## 📘 **Day 5: Multi-Class ANN**

### 🎯 **Goal**

Build a **Neural Network** that can classify data into **more than 2 categories**, e.g.:

* 🪷 Iris dataset → 3 flower types
* 🧮 Digits (MNIST small subset) → 10 digits (0–9)

---

### 🧠 **1. Concept Overview**

In **multi-class classification**, model predicts **one class among many**.
The **output layer** has **one neuron per class**, with:

* **Activation** → `softmax`
* **Loss** → `categorical_crossentropy`

---

### ⚙️ **2. Architecture Summary**

| Layer      | Description               | Activation |
| ---------- | ------------------------- | ---------- |
| **Input**  | Features (numeric values) | —          |
| **Hidden** | Learns representations    | ReLU       |
| **Output** | One neuron per class      | Softmax    |

---

### 💡 **Softmax Function**

Softmax converts raw output (logits) into probabilities that **sum to 1**:
[
P(y_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}
]

---

### 💻 **3. Code Example – Iris Dataset**

```python
# Day 5: Multi-Class ANN
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# 1️⃣ Load Dataset
iris = load_iris()
X = iris.data
y = iris.target  # 0,1,2

# 2️⃣ One-hot encode labels
y_encoded = to_categorical(y)

# 3️⃣ Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# 4️⃣ Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5️⃣ Build Model
model = Sequential([
    Dense(16, input_dim=4, activation='relu'),
    Dense(8, activation='relu'),
    Dense(3, activation='softmax')   # 3 output classes
])

# 6️⃣ Compile Model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 7️⃣ Train Model
history = model.fit(X_train, y_train, validation_data=(X_test, y_test),
                    epochs=50, batch_size=8, verbose=1)

# 8️⃣ Evaluate
loss, acc = model.evaluate(X_test, y_test, verbose=0)
print(f"✅ Test Accuracy: {acc:.3f}")
```

---

### 📊 **4. Visualize Accuracy/Loss**

```python
import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title("Model Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title("Model Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.show()
```

---

### 🧮 **5. Predictions**

```python
# Predict one sample
sample = X_test[0].reshape(1, -1)
pred = model.predict(sample)
print("Predicted Probabilities:", pred)
print("Predicted Class:", np.argmax(pred))
```

---

### 🧩 **6. Mini Tasks**

1. Change activation of hidden layers (`relu`, `tanh`, `leakyrelu`).
2. Try `optimizer='rmsprop'` or `sgd`.
3. Increase hidden neurons — does accuracy improve?
4. Use `digits` dataset from sklearn for 10-class classification.

---

### 🏁 **Outcome**

By end of Day 5, you’ll:
✅ Understand Softmax & multi-class logic
✅ Train a 3-class ANN from scratch
✅ Visualize training performance

---