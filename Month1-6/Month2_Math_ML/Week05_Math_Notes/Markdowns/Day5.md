## Week5 Day5
### 📘 `05_eigen.ipynb` – Eigenvalues & Eigenvectors

#### 1. Introduction

* What are eigenvalues & eigenvectors?
* Real-life applications (PCA, Google PageRank, quantum mechanics, vibrations).

#### 2. Intuition (Geometric Meaning)

* Show how a matrix **transforms vectors**.
* Explain that eigenvectors are directions that **don’t change direction**, only scale.
* Use a simple 2D transformation (e.g., stretch/rotation example).
* Visual demo: Plot vectors before/after transformation.

#### 3. Definition

* Matrix equation:

  $$
  A \mathbf{v} = \lambda \mathbf{v}
  $$

  * $\mathbf{v}$: eigenvector
  * $\lambda$: eigenvalue

#### 4. Characteristic Equation

* Derivation:

  $$
  \det(A - \lambda I) = 0
  $$
* This polynomial gives eigenvalues.

#### 5. Computation (Step by Step)

* Example 1:
  $A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$

  * Find eigenvalues (solve characteristic polynomial).
  * Find eigenvectors.
* Example 2: Use `numpy.linalg.eig` for larger matrices.

#### 6. Code Examples

```python
import numpy as np

# Example matrix
A = np.array([[2, 1],
              [1, 2]])

# Compute eigenvalues & eigenvectors
eigvals, eigvecs = np.linalg.eig(A)

print("Eigenvalues:", eigvals)
print("Eigenvectors:\n", eigvecs)
```

#### 7. Visualization (Optional but Powerful 🚀)

* Plot original vectors and eigenvectors to show how they scale.
* Use `matplotlib.quiver` for vector arrows.

#### 8. Summary

* Eigenvalues = scale factors.
* Eigenvectors = directions preserved under transformation.
* Computed via solving $\det(A - \lambda I) = 0$.

---
