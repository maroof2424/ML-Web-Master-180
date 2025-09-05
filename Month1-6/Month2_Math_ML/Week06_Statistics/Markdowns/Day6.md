# 📘 Day 6 – Hypothesis Testing

---

## 1. What is Hypothesis Testing?

Hypothesis testing is a **statistical method** used to make decisions about a population using sample data.

We test an assumption (**hypothesis**) and use probability to accept or reject it.

---

## 2. Types of Hypotheses

* **Null Hypothesis ($H_0$)**

  * Assumes **no effect / no difference**.
  * Example: "The new teaching method has the same effect as the old one."

* **Alternative Hypothesis ($H_1$ or $H_a$)**

  * Opposite of $H_0$.
  * Example: "The new teaching method is more effective than the old one."

---

## 3. Errors in Hypothesis Testing

* **Type I Error (False Positive)**

  * Rejecting $H_0$ when it is true.
  * Example: Concluding a medicine works when it doesn’t.

* **Type II Error (False Negative)**

  * Failing to reject $H_0$ when it is false.
  * Example: Concluding a medicine doesn’t work when it does.

---

## 4. Common Tests

1. **t-test** (for comparing means)

   * One-sample t-test: Compare sample mean with population mean.
   * Two-sample t-test: Compare means of two groups.

2. **Chi-Square Test** (categorical data)

   * Tests independence between two categorical variables.

3. **ANOVA (Analysis of Variance)**

   * Tests if **3 or more group means** are different.

---

## 5. Python Example

```python
import numpy as np
from scipy import stats

# Example: Two-sample t-test
group1 = np.random.normal(50, 5, 30)
group2 = np.random.normal(52, 5, 30)

t_stat, p_val = stats.ttest_ind(group1, group2)

print("T-statistic:", t_stat)
print("P-value:", p_val)

if p_val < 0.05:
    print("Reject Null Hypothesis (significant difference)")
else:
    print("Fail to Reject Null Hypothesis (no significant difference)")
```

---

✅ **Mini Task:**

1. Perform a **chi-square test** on a contingency table.
2. Run a one-way **ANOVA** on 3 different sample groups.

---
