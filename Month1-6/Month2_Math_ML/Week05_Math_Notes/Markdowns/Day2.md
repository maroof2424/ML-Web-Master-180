
## 📘 Week 5 – Day 2: Matrices

### 📝 What is a Matrix?

A **matrix** is a rectangular array of numbers arranged in rows and columns.

$$
A = \begin{bmatrix}  
1 & 2 & 3 \\  
4 & 5 & 6  
\end{bmatrix}
$$

* Rows = horizontal entries
* Columns = vertical entries

---

### 🔹 Basic Operations with Matrices

```python
import numpy as np

# Define matrices
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8, 9],
              [1, 2, 3]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Addition & Subtraction
print("\nA + B =\n", A + B)
print("\nA - B =\n", A - B)

# Scalar Multiplication
print("\n2 * A =\n", 2 * A)
```

---

### 🔹 Transpose of a Matrix

$$
A^T_{ij} = A_{ji}
$$

```python
print("\nTranspose of A:\n", A.T)
```

---

### 🔹 Matrix Multiplication

$$
(A \times C)_{ij} = \sum_{k=1}^{n} A_{ik}C_{kj}
$$

```python
C = np.array([[1, 2],
              [3, 4],
              [5, 6]])

print("Matrix C:\n", C)
print("\nA (2x3) * C (3x2) =\n", A.dot(C))   # or A @ C
```

---

### 🔹 Identity Matrix

$$
I = \begin{bmatrix}  
1 & 0 & 0 \\  
0 & 1 & 0 \\  
0 & 0 & 1  
\end{bmatrix}
$$

```python
I = np.eye(3)
print("\nIdentity Matrix (3x3):\n", I)
```

---

### 🔹 Determinant & Inverse

$$
det(M) = ad - bc \quad \text{for }  
M = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
$$

```python
M = np.array([[4, 7],
              [2, 6]])
print("\nMatrix M:\n", M)

# Determinant
det_M = np.linalg.det(M)
print("Determinant of M:", det_M)

# Inverse
if det_M != 0:
    inv_M = np.linalg.inv(M)
    print("\nInverse of M:\n", inv_M)
    print("\nM * M^-1 =\n", M.dot(inv_M))
```

---

✅ **Mini Task for You:**

1. Create two $3 \times 3$ matrices of your choice.
2. Perform: Addition, Subtraction, Multiplication.
3. Compute determinant & check if inverse exists.

--