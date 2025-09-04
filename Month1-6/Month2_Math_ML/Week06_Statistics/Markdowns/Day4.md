

# 📘 Day 4 – Normal Distribution

---

## 1. Gaussian Distribution Curve

The **normal distribution** is one of the most important probability distributions in statistics.

* It is also called the **Gaussian distribution**.
* It has a **bell-shaped curve**.

Mathematical formula:

$$
f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{ -\frac{1}{2} \left(\frac{x - \mu}{\sigma}\right)^2 }
$$

Where:

* $\mu$ = Mean (center of the distribution)
* $\sigma$ = Standard deviation (spread)

---

## 2. Properties of Normal Distribution

1. Symmetrical around the mean ($\mu$).
2. Mean = Median = Mode.
3. The total area under the curve = 1.
4. **68-95-99.7 Rule (Empirical Rule):**

   * 68% of data within 1σ of mean
   * 95% within 2σ
   * 99.7% within 3σ

---

## 3. Applications in Real Datasets

* **Human heights, exam scores, errors in measurement** often follow normal distribution.
* **Machine Learning:** Used in statistical inference, hypothesis testing, and algorithms (e.g., Naive Bayes).
* **Finance:** Stock returns are often modeled as normal distribution.

---

## 4. Python Example

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate data
mu, sigma = 0, 1  # mean and std dev
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, mu, sigma)

# Plot
plt.plot(x, y, label="Normal Distribution")
plt.title("Gaussian Distribution Curve")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.grid(True)
plt.legend()
plt.show()
```

---

✅ **Mini Task:**

1. Plot a normal distribution with μ = 50, σ = 10.
2. Verify the **68-95-99.7 rule** using random samples in NumPy.

