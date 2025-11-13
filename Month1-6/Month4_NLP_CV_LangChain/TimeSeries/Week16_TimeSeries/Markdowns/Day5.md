# Day 5 — Facebook Prophet Model

## ✅ Objectives

* Fit **Prophet** model on time series
* Forecast future values (30–90 days)
* Visualize **trend + seasonality**
* Compare Prophet vs ARIMA

---

## 1. Install & Import Libraries

```python
# Install if not already
# !pip install prophet

import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
```

---

## 2. Load & Prepare Data

Prophet requires **specific column names**:

* `ds` → datetime column
* `y` → target variable

```python
df = pd.read_csv("DailyDelhiClimateTrain.csv")

# Rename columns for Prophet
df = df[['date', 'meantemp']].rename(columns={'date':'ds', 'meantemp':'y'})
df['ds'] = pd.to_datetime(df['ds'])
```

---

## 3. Fit Prophet Model

```python
model = Prophet(daily_seasonality=True)
model.fit(df)
```

**Note:**

* `daily_seasonality=True` → captures daily patterns
* Prophet automatically detects trend + yearly/weekly seasonality

---

## 4. Forecast Future (Next 30–90 Days)

```python
future = model.make_future_dataframe(periods=30)  # 30 days forecast
forecast = model.predict(future)
```

---

## 5. Inspect Forecast

```python
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
```

* `yhat` → predicted value
* `yhat_lower` / `yhat_upper` → confidence intervals

---

## 6. Plot Forecast

```python
fig1 = model.plot(forecast)
plt.title("Prophet Forecast - Mean Temperature")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.show()
```

---

## 7. Plot Components (Trend + Seasonality)

```python
fig2 = model.plot_components(forecast)
plt.show()
```

**Observation:**

* Trend → overall increase/decrease
* Yearly/weekly seasonality → recurring patterns

---

## ✅ Key Takeaways

1. Prophet handles **trend + seasonality automatically**
2. No need for stationarity → simpler than ARIMA
3. Good for **long-term forecasts** with holidays/seasonal effects
4. Always visualize components to understand predictions

---

# ⚠️ Pro Tips

* Rename columns exactly as `ds` and `y`
* For daily data, set `daily_seasonality=True`
* For longer forecasts, increase `periods` in `make_future_dataframe`
* Compare Prophet forecast with ARIMA to see which fits better

---