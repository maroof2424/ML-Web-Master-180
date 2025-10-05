

## 🧠 Day 1 – TensorFlow / Keras Setup

**Goal:** Set up TensorFlow and verify everything works (including GPU).

---

### 🪜 Step 1: Install TensorFlow

> Colab usually has TensorFlow preinstalled, but we’ll upgrade to the latest stable version.

```python
# Install / Upgrade TensorFlow
!pip install -q tensorflow==2.17.0
```

---

### 🧩 Step 2: Import and Check Version

```python
import tensorflow as tf

print("✅ TensorFlow Version:", tf.__version__)
print("✅ Keras Version:", tf.keras.__version__)
```

---

### ⚙️ Step 3: Check GPU Availability

> GPUs make training much faster!
> In Colab, go to **Runtime → Change runtime type → GPU** before running this.

```python
gpu_devices = tf.config.list_physical_devices('GPU')
if gpu_devices:
    print("🚀 GPU is available:", gpu_devices)
else:
    print("⚠️ No GPU found. Go to Runtime → Change runtime type → GPU")
```

---

### 🧠 Step 4: Your First TensorFlow Operation

> Let’s test TensorFlow computation (CPU or GPU).

```python
a = tf.constant(5)
b = tf.constant(7)
c = a * b

print("Result of TensorFlow multiplication:", c.numpy())
```

---

### 🧱 Step 5: Your First Keras Model (Hello ANN 👋)

> A minimal ANN that learns nothing — just for setup verification.

```python
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Build a simple ANN
model = Sequential([
    Dense(8, activation='relu', input_shape=(4,)),  # input layer
    Dense(3, activation='softmax')                  # output layer
])

model.summary()
```

---

### 🧪 Step 6: Dummy Training Test

> Let’s run one quick training loop on random data to confirm it works.

```python
import numpy as np

# Generate random dummy data
X = np.random.rand(100, 4)
y = tf.keras.utils.to_categorical(np.random.randint(3, size=100), num_classes=3)

# Compile and train
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
history = model.fit(X, y, epochs=5, verbose=1)
```

---

### 🏁 Step 7: Save and Load Model

> Check model save/load functionality (will be useful later).

```python
# Save
model.save('test_model.h5')
print("✅ Model saved successfully!")

# Load
loaded_model = tf.keras.models.load_model('test_model.h5')
print("✅ Model loaded successfully!")
```

---

### 🎯 Summary

✅ TensorFlow installed
✅ GPU checked
✅ Model built & trained
✅ Save/Load tested

You’re now ready for **Day 2: ANN Basics** 🚀

---
