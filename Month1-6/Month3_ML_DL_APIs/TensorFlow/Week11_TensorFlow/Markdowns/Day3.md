

## 📘 **Day 3: Loss & Activation Functions**

### 🎯 **Goal**

Understand how **loss functions** and **activation functions** shape how an Artificial Neural Network (ANN)** learns** and **makes predictions**.

---

### 🧠 **1. Concept Overview**

#### 🔹 **Activation Functions**

They decide whether a neuron should “fire” or not.
Without them, your ANN would just be a *linear regression model* — unable to learn complex patterns.

| Activation                       | Equation / Logic                                | Use Case                                   |
| -------------------------------- | ----------------------------------------------- | ------------------------------------------ |
| **ReLU (Rectified Linear Unit)** | `f(x) = max(0, x)`                              | Hidden layers, prevents vanishing gradient |
| **Sigmoid**                      | `f(x) = 1 / (1 + e^-x)`                         | Binary classification (output 0–1)         |
| **Tanh**                         | `f(x) = (e^x - e^-x) / (e^x + e^-x)`            | Hidden layers, output between -1 and 1     |
| **Softmax**                      | Converts outputs to probabilities that sum to 1 | Multi-class classification                 |

---

#### 🔹 **Loss Functions**

They measure **how far predictions are from actual values**, guiding weight updates.

| Problem Type                   | Common Loss Function     | Formula (simplified)         |
| ------------------------------ | ------------------------ | ---------------------------- |
| **Regression**                 | Mean Squared Error (MSE) | avg((y_pred - y_true)²)      |
| **Binary Classification**      | Binary Crossentropy      | −[y log(p) + (1−y) log(1−p)] |
| **Multi-Class Classification** | Categorical Crossentropy | −Σ yᵢ log(pᵢ)                |

---

### ⚙️ **2. Code Example: Activation + Loss**

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import BinaryCrossentropy

# Example ANN with activation functions
model = Sequential([
    Dense(8, input_dim=4, activation='relu'),    # hidden layer 1
    Dense(4, activation='relu'),                 # hidden layer 2
    Dense(1, activation='sigmoid')               # output layer (binary classification)
])

# Compile model with loss + optimizer + metrics
model.compile(
    optimizer='adam',
    loss=BinaryCrossentropy(),  # or 'binary_crossentropy'
    metrics=['accuracy']
)

model.summary()
```

---

### 🧩 **3. Visual Intuition**

* **ReLU:** passes positive values, cuts off negatives → faster convergence.
* **Sigmoid:** squashes outputs to (0,1), but can cause vanishing gradients.
* **Tanh:** centered around 0 (better than sigmoid for hidden layers).
* **Softmax:** for multi-class outputs — normalizes probabilities.

---

### 🧮 **4. Practical Tip**

* For **hidden layers:** mostly use `ReLU`.
* For **binary output:** use `sigmoid` + `binary_crossentropy`.
* For **multi-class output:** use `softmax` + `categorical_crossentropy`.

---

### 🧠 **5. Mini Task**

1. Build a small ANN for binary classification using `sigmoid` activation.
2. Change to `tanh` and compare accuracy/loss.
3. Note how learning rate or activation changes learning behavior.

---

### 🏁 **Outcome**

By the end of Day 3, you should:
✅ Understand what activations and loss functions do.
✅ Know which ones to use for regression vs. classification.
✅ Be able to modify and test them in Keras.

---