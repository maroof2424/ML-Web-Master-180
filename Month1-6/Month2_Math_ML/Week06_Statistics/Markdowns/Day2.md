# 📘 Day 2 – Variance & Standard Deviation

Central tendency (mean, median, mode) tells us about the **center** of data,
but we also need to know how much the data **spreads out** from the mean.
This is measured by **Variance** and **Standard Deviation (SD)**.

---

## 1️⃣ Variance (σ² or s²)

Variance is the **average squared deviation** from the mean.

### Formula:

* **Population variance** (σ²):

$$
\sigma^2 = \frac{\sum (x_i - \mu)^2}{N}
$$

* **Sample variance** (s²):

$$
s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}
$$

👉 We divide by **n-1** for sample variance (Bessel’s correction).

---

## 2️⃣ Standard Deviation (σ or s)

The **square root of variance**:

$$
\sigma = \sqrt{\sigma^2}
$$

It’s in the **same unit** as the data, so easier to interpret.

---

## 3️⃣ Example Calculation

Dataset = {2, 4, 4, 4, 5, 5, 7, 9}
Mean = (2+4+4+4+5+5+7+9)/8 = 40/8 = 5

Step 1: Subtract mean (x − μ), square differences:

| x | x − μ | (x − μ)² |
| - | ----- | -------- |
| 2 | -3    | 9        |
| 4 | -1    | 1        |
| 4 | -1    | 1        |
| 4 | -1    | 1        |
| 5 | 0     | 0        |
| 5 | 0     | 0        |
| 7 | 2     | 4        |
| 9 | 4     | 16       |

Step 2: Sum = 32

* Population variance = 32 / 8 = **4**

* Population SD = √4 = **2**

* Sample variance = 32 / (8−1) = 32/7 ≈ **4.57**

* Sample SD = √4.57 ≈ **2.14**

---

## 4️⃣ When to Use?

* **Population variance/SD** → when you have the **whole dataset**.
* **Sample variance/SD** → when working with a **sample** from the population.

---

## ✅ Practice Problems

1. Find variance & SD for {1, 2, 3, 4, 5}.
2. A dataset of exam scores: {50, 60, 70, 80, 90}. Compute variance and SD.

---
