# 📘 Day 5 – Z-scores & p-values

---

## 1. Z-score (Standardization)

A **Z-score** tells us how many **standard deviations** a data point is away from the mean.

**Formula:**

$$
Z = \frac{X - \mu}{\sigma}
$$

Where:

* $X$ = data point
* $\mu$ = mean
* $\sigma$ = standard deviation

✔️ Z > 0 → above mean
✔️ Z < 0 → below mean
✔️ Z = 0 → exactly at mean

**Example:**
If exam score $X = 85$, mean $\mu = 70$, std $\sigma = 10$:

$$
Z = \frac{85 - 70}{10} = 1.5
$$

👉 The student scored **1.5σ above average**.

---

## 2. p-value (Probability Value)

* The **p-value** is the probability of getting results at least as extreme as the observed results, assuming the **null hypothesis (H₀)** is true.
* It measures **evidence against H₀**.

**Interpretation:**

* p ≤ 0.05 → Strong evidence **against H₀** → Reject null hypothesis
* p > 0.05 → Weak evidence → Fail to reject H₀

---

## 3. Relation to Hypothesis Testing

Hypothesis Testing steps:

1. Define **H₀** (null) and **H₁** (alternative).
   Example:

   * H₀: "The mean height = 170 cm"
   * H₁: "The mean height ≠ 170 cm"
2. Calculate **test statistic** (like Z or t).
3. Find **p-value**.
4. Compare with significance level (α = 0.05).

   * If p ≤ α → Reject H₀.
   * If p > α → Fail to reject H₀.

---

## 4. Python Example

```python
import numpy as np
from scipy import stats

# Example dataset
data = [12, 15, 14, 10, 13, 15, 16, 14, 14, 15]

# One-sample Z-test (assuming population mean=12)
mean_pop = 12
mean_sample = np.mean(data)
std_sample = np.std(data, ddof=1)
n = len(data)

z_score = (mean_sample - mean_pop) / (std_sample / np.sqrt(n))

# p-value (two-tailed)
p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))

print("Z-score:", z_score)
print("p-value:", p_value)
```

---

✅ **Mini Task for You**

* Take any dataset (e.g., student marks).
* Test if the mean is equal to some value (e.g., 50).
* Compute Z-score & p-value.

---
