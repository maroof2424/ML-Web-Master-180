

## 🧠 **Day 2 – Artificial Neural Network (ANN) Basics**

---

### 🎯 **Learning Objectives**

By the end of this lesson, you’ll understand:

1. What **neurons**, **weights**, and **biases** are
2. How data flows through an ANN (**forward propagation**)
3. How the model learns (**backpropagation**)
4. How to build a basic **ANN using Keras (TensorFlow)**

---

## 🪄 **1. The Concept – What is an ANN?**

An **Artificial Neural Network** mimics how the human brain learns.

Each **neuron** receives inputs, multiplies them by **weights**, adds a **bias**, and applies an **activation function** to decide the output.

[
z = w_1x_1 + w_2x_2 + b
]
[
output = f(z)
]

Where:

* ( x_i ) = input features
* ( w_i ) = weights
* ( b ) = bias
* ( f(z) ) = activation (e.g. sigmoid, ReLU)

---

## 🔄 **2. Forward Propagation**

When you pass data into the network:

* Inputs → Hidden Layers → Output Layer
* Each neuron passes its output to the next layer.

It’s basically a chain of math operations.

---

## 🔁 **3. Backpropagation**

When the network makes a wrong prediction:

1. The **loss** (error) is calculated.
2. The network adjusts the **weights & biases** using **gradient descent**.
3. This helps minimize the loss step by step.

---

## ⚙️ **4. Simple ANN using Keras**

Let’s build a small ANN from scratch using dummy data.

```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
```

---

### 🧩 **Step 1: Create Dummy Data**

```python
# 100 samples, 3 input features
X = np.random.rand(100, 3)

# Binary target (0 or 1)
y = np.random.randint(2, size=(100, 1))
```

---

### 🧠 **Step 2: Build ANN Model**

```python
model = Sequential([
    Dense(4, input_dim=3, activation='relu'),  # Hidden layer
    Dense(1, activation='sigmoid')             # Output layer
])

model.summary()
```

📘 **Explanation**

* `input_dim=3`: 3 input features
* `Dense(4)`: 4 neurons (each has its own weights & bias)
* `activation='relu'`: helps network learn nonlinear patterns
* `sigmoid`: gives output between 0–1 for binary classification

---

### 🔧 **Step 3: Compile the Model**

```python
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
```

📗 **Explanation**

* **Optimizer:** How weights update (Adam = adaptive learning rate)
* **Loss:** Binary Crossentropy (for 0/1 targets)
* **Metrics:** Accuracy

---

### 🚀 **Step 4: Train the Model**

```python
history = model.fit(X, y, epochs=20, verbose=1)
```

You’ll see output like:

```
Epoch 1/20
4/4 [==============================] - 0s 3ms/step - loss: 0.69 - accuracy: 0.53
...
```

Each epoch improves accuracy gradually.

---

### 📊 **Step 5: Plot Training Progress**

```python
import matplotlib.pyplot as plt

plt.plot(history.history['loss'], label='Loss')
plt.plot(history.history['accuracy'], label='Accuracy')
plt.xlabel('Epochs')
plt.legend()
plt.title("Training Performance")
plt.show()
```

---

### 🧪 **Step 6: Make Predictions**

```python
sample = np.array([[0.2, 0.8, 0.5]])
pred = model.predict(sample)
print("Predicted output:", pred)
```

You’ll get something like:

```
Predicted output: [[0.72]]
```

👉 It means the model predicts **class 1** with **72% confidence**.

---

## 🧩 **7. Recap**

| Concept                 | Description                                       |
| ----------------------- | ------------------------------------------------- |
| **Neuron**              | Takes input → applies weights & bias → activation |
| **Forward Propagation** | Flow of data through layers                       |
| **Backpropagation**     | Weight adjustment to minimize loss                |
| **Keras Model**         | Sequential layers forming the network             |
| **Loss Function**       | Measures how wrong the model is                   |
| **Optimizer**           | Adjusts weights to reduce loss                    |

---


