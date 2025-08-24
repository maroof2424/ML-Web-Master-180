### ✅ Day 1 – Vectors Basics

📄 File: `01_vectors.ipynb`

**Topics:**

* Introduction to Vectors
* Vector addition & subtraction
* Scalar multiplication
* Magnitude of a vector
* Unit vectors
* Visualization (2D/3D plots)

---

Here’s the **starter content** for `01_vectors.ipynb`:

```python
# 📘 Week 5 - Day 1: Vectors

# --- Imports ---
import numpy as np
import matplotlib.pyplot as plt

# --- Basics ---
# Define vectors
v1 = np.array([2, 3])
v2 = np.array([1, -1])

print("Vector v1:", v1)
print("Vector v2:", v2)

# Addition
print("v1 + v2 =", v1 + v2)

# Scalar multiplication
print("2 * v1 =", 2 * v1)

# Magnitude
magnitude_v1 = np.linalg.norm(v1)
print("|v1| =", magnitude_v1)

# Unit vector
unit_v1 = v1 / magnitude_v1
print("Unit vector of v1:", unit_v1)

# --- Visualization ---
plt.figure(figsize=(6,6))
plt.quiver(0,0,v1[0],v1[1],angles='xy',scale_units='xy',scale=1,color='r',label='v1')
plt.quiver(0,0,v2[0],v2[1],angles='xy',scale_units='xy',scale=1,color='b',label='v2')
plt.xlim(-3,3)
plt.ylim(-3,4)
plt.axhline(0,color='black',linewidth=0.5)
plt.axvline(0,color='black',linewidth=0.5)
plt.legend()
plt.title("Vectors in 2D")
plt.grid()
plt.show()
```

---
