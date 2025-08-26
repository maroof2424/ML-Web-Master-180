## 📘 Week 5 – Day 3: Dot Product & Transpose

---

### 📝 Dot Product (Vectors)

The **dot product** of two vectors:

$$
\vec{a} \cdot \vec{b} = \sum_{i=1}^n a_i b_i = a_1b_1 + a_2b_2 + \dots + a_n b_n
$$

It also has a geometric meaning:

$$
\vec{a} \cdot \vec{b} = \|\vec{a}\| \|\vec{b}\| \cos \theta
$$

```python
import numpy as np

# Define two vectors
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Vector a:", a)
print("Vector b:", b)

# Dot product
dot_ab = np.dot(a, b)
print("\nDot Product (a · b) =", dot_ab)
```

---

### 📝 Dot Product (Matrix Multiplication Form)

For matrices:

$$
C = A \cdot B
$$

where

$$
C_{ij} = \sum_k A_{ik}B_{kj}
$$

```python
# Define matrices
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Dot product (matrix multiplication)
C = np.dot(A, B)   # same as A @ B
print("\nA · B =\n", C)
```

---

### 📝 Transpose of a Matrix

The **transpose** swaps rows with columns:

$$
(A^T)_{ij} = A_{ji}
$$

```python
# Transpose
print("\nTranspose of A:\n", A.T)

# Double transpose = original
print("\n(A^T)^T =\n", (A.T).T)
```

---

### ✅ Mini Task for You

1. Take vectors:
   $\vec{u} = [2, -1, 3]$, $\vec{v} = [0, 4, 2]$
   Compute $u \cdot v$.
2. Take a 3×2 matrix $M$ and compute $M^T \cdot M$.

---

