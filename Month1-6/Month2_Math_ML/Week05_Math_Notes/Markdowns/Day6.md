
## 📘 Week 5 – Day 6: Practice Problems

---

### 📝 Problem Set

#### ✅ Problem 1 – Vectors

* Given two vectors:

  $$
  u = [2, 3], \quad v = [1, 4]
  $$

  * Compute:

    1. $u + v$
    2. $3u - 2v$
    3. Dot product $u \cdot v$

```python
import numpy as np

u = np.array([2, 3])
v = np.array([1, 4])

print("u + v =", u + v)
print("3u - 2v =", 3*u - 2*v)
print("Dot product u·v =", np.dot(u, v))
```

---

#### ✅ Problem 2 – Matrix Operations

* Given:

$$
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad 
B = \begin{bmatrix} 2 & 0 \\ 1 & 3 \end{bmatrix}
$$

Compute:

1. $A + B$
2. $AB$
3. $A^T$

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 3]])

print("A + B =\n", A + B)
print("A·B =\n", np.dot(A, B))
print("Transpose of A =\n", A.T)
```

---

#### ✅ Problem 3 – Determinants

Find the determinant of:

$$
C = \begin{bmatrix}
2 & -1 & 0 \\
1 & 3 & 4 \\
0 & -2 & 5
\end{bmatrix}
$$

```python
C = np.array([[2, -1, 0],
              [1,  3, 4],
              [0, -2, 5]])

print("Determinant of C =", np.linalg.det(C))
```

---

#### ✅ Problem 4 – Eigenvalues & Eigenvectors

For the matrix:

$$
D = \begin{bmatrix}
4 & 1 \\
2 & 3
\end{bmatrix}
$$

Find eigenvalues and eigenvectors.

```python
D = np.array([[4, 1],
              [2, 3]])

eigvals, eigvecs = np.linalg.eig(D)
print("Eigenvalues:", eigvals)
print("Eigenvectors:\n", eigvecs)
```

---

#### ✅ Problem 5 – Challenge 🚀

Let

$$
M = \begin{bmatrix}
3 & 1 & 2 \\
4 & 0 & -1 \\
2 & 5 & 3
\end{bmatrix}
$$

1. Compute determinant.
2. Compute eigenvalues.
3. Verify property: $\det(M^T) = \det(M)$.

```python
M = np.array([[3, 1, 2],
              [4, 0, -1],
              [2, 5, 3]])

print("Determinant:", np.linalg.det(M))

eigvals, eigvecs = np.linalg.eig(M)
print("Eigenvalues:", eigvals)

print("det(M^T):", np.linalg.det(M.T))
print("det(M):", np.linalg.det(M))
```

---

### ✅ Summary

This notebook covers **all key topics of Week 5** with hands-on problems.

---