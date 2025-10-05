

### 🧠 Week 11 – Deep Learning Intro (TensorFlow / Keras)

**📁 Directory:** `Month3_ML_DL/Week11_TensorFlow`

#### 🗂 Files:

```
01_setup_tensorflow.ipynb
02_first_ann.ipynb
03_loss_activation.ipynb
04_binary_classification_ann.ipynb
05_multiclass_ann.ipynb
06_mini_project_ann.ipynb
README.md
```

---

## 🎯 Learning Objective

This week, you’ll understand the **core concepts of Artificial Neural Networks (ANN)** and learn to **build and train neural models using TensorFlow & Keras** — even without a GPU (by using Google Colab).

---

## 🧩 Day-wise Plan

### **Day 1: TensorFlow / Keras Setup**

* Install TensorFlow and Keras.
* Run a test model to confirm setup.
* Check GPU availability in Colab using:

  ```python
  import tensorflow as tf
  print("TensorFlow version:", tf.__version__)
  print("GPU Available:", tf.config.list_physical_devices('GPU'))
  ```
* ✅ Tip: If GPU isn’t listed, go to **Runtime → Change runtime type → GPU**.

---

### **Day 2: ANN Basics**

* Learn about:

  * Neurons, layers, weights, biases.
  * Forward propagation & backpropagation (conceptually).
* Build your **first manual ANN** with dense layers using Keras.

---

### **Day 3: Loss & Activation Functions**

* Understand:

  * **Activation functions:** `sigmoid`, `relu`, `softmax`, `tanh`.
  * **Loss functions:** `binary_crossentropy`, `categorical_crossentropy`, `mse`.
* Experiment with different activation + loss combinations.

---

### **Day 4: Binary Classification ANN**

* Dataset ideas: **Titanic**, **Spam detection**, or **Loan Approval**.
* Build an ANN with:

  * Input → Hidden (ReLU) → Output (Sigmoid)
* Evaluate accuracy, precision, recall.

---

### **Day 5: Multi-Class ANN**

* Use **small MNIST / Fashion MNIST** dataset.
* Implement:

  * Output layer → `Softmax`
  * Loss → `categorical_crossentropy`
* Plot training/validation accuracy.

---

### **Day 6: Mini Project – Binary Classification**

* Choose dataset:

  * Fake News detection
  * Customer churn prediction
  * Loan default prediction
* Train → Evaluate → Save model using:

  ```python
  model.save('my_ann_model.h5')
  ```

---

### **Day 7: Review & Wrap-Up**

* Compare ANN vs classical ML (SVM, RF).
* Summarize:

  * Why activation matters
  * Gradient descent concept
  * When to use ANN over ML
* Backup notebooks to GitHub or Google Drive.

---

## ⚙️ Environment Notes

| Platform           | Recommended                | Notes                 |
| ------------------ | -------------------------- | --------------------- |
| 💻 Local PC        | ❌ Not recommended (no GPU) | Training will be slow |
| ☁️ Google Colab    | ✅ Recommended              | Free GPU available    |
| 🧮 Kaggle Notebook | ✅ Optional                 | Also provides GPU     |

---

## 🧰 Dependencies

Install inside Colab cell:

```bash
!pip install tensorflow numpy pandas scikit-learn matplotlib
```

---

## 🧠 Key Concepts Recap

* ANN = layers of neurons (input → hidden → output)
* Weights adjust via **backpropagation**
* Optimization via **Gradient Descent**
* Loss + Activation determine model learning
* GPU = faster matrix operations (optional but ideal)

---

## 💡 Bonus Challenge

Try converting your sklearn model (e.g., Logistic Regression) into a **Keras Sequential ANN** and compare:

* Accuracy
* Training time
* Model size

---