# Day 4 — ARIMA Model

## ✅ Objectives

* Determine **p, d, q** parameters from ACF/PACF
* Fit **ARIMA model** using `statsmodels`
* Forecast next 30–90 days
* Plot **actual vs predicted**

---

## 1. Import Libraries

```python
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
```

---

## 2. Load & Prepare Data

```python
df = pd.read_csv("DailyDelhiClimateTrain.csv")
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

ts = df['meantemp']  # Example column
```

---

## 3. Check Stationarity & Differencing

```python
ts_diff = ts.diff().dropna()
```

**Optional:** Use ADF test (Day 3) to confirm stationary.

---

## 4. Identify ARIMA Parameters (p, d, q)

* **d** → number of differencing required (from Day 3)
* **p** → significant lags from **PACF**
* **q** → significant lags from **ACF**

```python
plt.figure(figsize=(12,4))
plot_acf(ts_diff, lags=50)
plt.show()

plt.figure(figsize=(12,4))
plot_pacf(ts_diff, lags=50)
plt.show()
```

**Tip:**

* PACF → where first significant spike → p
* ACF → where first significant spike → q

---

## 5. Fit ARIMA Model

```python
# Example: ARIMA(p=2, d=1, q=2) → adjust based on ACF/PACF
model = ARIMA(ts, order=(2,1,2))
model_fit = model.fit()
print(model_fit.summary())
```

---

## 6. Forecast Next 30 Days

```python
forecast = model_fit.forecast(steps=30)
print(forecast)
```

---

## 7. Plot Actual vs Predicted

```python
plt.figure(figsize=(12,5))
plt.plot(ts, label='Actual')
plt.plot(forecast.index, forecast, label='Forecast', color='red')
plt.title("ARIMA Forecast vs Actual")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
```

---

## ✅ Key Takeaways

1. ARIMA = **AR (p) + I (d) + MA (q)**
2. **Stationarity** is required → differencing (d)
3. **ACF/PACF plots** help find p and q
4. Forecasting is **future prediction**, always visualize vs actual

---

# ⚠️ Pro Tips

* Start simple → low p/q values → increase if residuals show patterns
* Check residual plots (`model_fit.resid`) to validate model
* For longer-term forecast, errors compound → consider **Prophet** (Day 5)
