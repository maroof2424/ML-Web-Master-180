## 📘 Week 5 – Day 4: Determinants

---

### 📝 What is a Determinant?

For a **2×2 matrix**:

$$
A = \begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

The determinant is:

$$
\det(A) = ad - bc
$$

For larger matrices, determinants are computed using **cofactor expansion** or **row-reduction methods**.

---

### 📝 Properties of Determinants

1. $\det(I) = 1$ (Identity matrix).
2. $\det(A^T) = \det(A)$.
3. $\det(AB) = \det(A)\det(B)$.
4. If a row (or column) is multiplied by a scalar $k$, the determinant is multiplied by $k$.
5. If two rows/columns are identical → determinant = 0.
6. If $A$ is invertible, $\det(A) \neq 0$.

---

### 🔢 Example 1: 2×2 Determinant

```python
import numpy as np

# 2x2 matrix
A = np.array([[2, 3],
              [1, 4]])

det_A = np.linalg.det(A)
print("Matrix A:\n", A)
print("Determinant of A =", det_A)
```

---

### 🔢 Example 2: 3×3 Determinant

$$
\det\begin{bmatrix}
1 & 2 & 3 \\
0 & 4 & 5 \\
1 & 0 & 6
\end{bmatrix}
$$

```python
B = np.array([[1, 2, 3],
              [0, 4, 5],
              [1, 0, 6]])

det_B = np.linalg.det(B)
print("Matrix B:\n", B)
print("Determinant of B =", det_B)
```

---

### 🔢 Example 3: Determinant Properties Check

```python
# Property check: det(AB) = det(A)*det(B)
C = np.array([[1, 2],
              [3, 4]])

D = np.array([[2, 0],
              [1, 3]])

lhs = np.linalg.det(np.dot(C, D))
rhs = np.linalg.det(C) * np.linalg.det(D)

print("det(C·D) =", lhs)
print("det(C) * det(D) =", rhs)
```

---

### ✅ Mini Task for You

1. Compute determinant of:

$$
M = \begin{bmatrix}
3 & 1 & 2 \\
4 & 0 & -1 \\
2 & 5 & 3
\end{bmatrix}
$$

2. Verify that $\det(M^T) = \det(M)$.

---
