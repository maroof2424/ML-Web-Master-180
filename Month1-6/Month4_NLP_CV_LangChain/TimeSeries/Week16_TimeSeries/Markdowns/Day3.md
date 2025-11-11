# Day 3 — Stationarity & Differencing

## ✅ Objectives

* Understand **stationarity** in time series
* Perform **Dickey-Fuller test**
* Apply **differencing** to make series stationary
* Plot **ACF & PACF** for ARIMA model tuning

---

## 1. Import Libraries

```python
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
```

---

## 2. Load & Prepare Data

```python
df = pd.read_csv("DailyDelhiClimateTrain.csv")
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

ts = df['meantemp']  # example column
```

---

## 3. Check Raw Time Series

```python
plt.figure(figsize=(12,5))
plt.plot(ts)
plt.title("Daily Mean Temperature - Raw")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.grid(True)
plt.show()
```

---

## 4. Check Stationarity — Dickey-Fuller Test

```python
def adf_test(series):
    result = adfuller(series)
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    for key, value in result[4].items():
        print('Critical Value (%s): %.3f' % (key, value))
        
adf_test(ts)
```

**Interpretation:**

* **p-value < 0.05** → stationary
* **p-value > 0.05** → non-stationary, need differencing

---

## 5. Differencing to Make Series Stationary

**First-order differencing:**

```python
ts_diff = ts.diff().dropna()
```

**Check differenced series:**

```python
plt.figure(figsize=(12,5))
plt.plot(ts_diff)
plt.title("Differenced Series (1st order)")
plt.grid(True)
plt.show()

adf_test(ts_diff)
```

* If still non-stationary → second-order differencing:

```python
ts_diff2 = ts_diff.diff().dropna()
```

---

## 6. Plot ACF and PACF

**ACF (Autocorrelation Function) → q parameter in MA**
**PACF (Partial Autocorrelation Function) → p parameter in AR**

```python
plt.figure(figsize=(12,4))
plot_acf(ts_diff, lags=50)
plt.show()

plt.figure(figsize=(12,4))
plot_pacf(ts_diff, lags=50)
plt.show()
```

**Observation:**

* Look for **significant lags above confidence intervals**
* Use these as **AR & MA orders** for ARIMA

---

## ✅ Key Takeaways

1. **Stationarity** is critical for ARIMA/forecasting
2. Dickey-Fuller test tells whether differencing is needed
3. Differencing removes trend & stabilizes variance
4. **ACF & PACF** guide ARIMA hyperparameters (p, d, q)

---

# ⚠️ Pro Tips

* Always plot series before and after differencing
* Don’t over-difference — it can remove useful signal
* Use `ts_diff = ts.diff().dropna()` carefully, `.dropna()` avoids NaN

---
