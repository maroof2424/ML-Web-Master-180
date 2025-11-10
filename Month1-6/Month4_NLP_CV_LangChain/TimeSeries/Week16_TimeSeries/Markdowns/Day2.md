# Day 2 — Moving Averages & Trends

## ✅ Objectives

* Understand trends in a time series
* Apply **moving averages** to smooth data
* Separate **trend vs noise**
* Visualize trends clearly

---

## 1. Import Libraries

```python
import pandas as pd
import matplotlib.pyplot as plt
```

---

## 2. Load and Prepare Data

```python
df = pd.read_csv("DailyDelhiClimateTrain.csv")
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Optional: focus on one column
ts = df['meantemp']
```

---

## 3. Plot Raw Time Series

```python
plt.figure(figsize=(12,5))
plt.plot(ts, label='Raw Data')
plt.title("Daily Mean Temperature - Raw")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
```

* Observe **spikes, volatility, seasonal patterns**
* Raw data is noisy → next step smooth it

---

## 4. Apply Moving Averages

**Rolling Mean** (Simple Moving Average, SMA)

```python
rolling_7 = ts.rolling(window=7).mean()    # 7-day rolling
rolling_30 = ts.rolling(window=30).mean()  # 30-day rolling
```

---

## 5. Plot Rolling Averages

```python
plt.figure(figsize=(12,5))
plt.plot(ts, alpha=0.4, label='Raw')
plt.plot(rolling_7, label='7-day MA', linewidth=2)
plt.plot(rolling_30, label='30-day MA', linewidth=2)
plt.title("Moving Averages - Trends")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
```

**Observation:**

* 7-day MA → short-term trends
* 30-day MA → long-term trends
* Spikes/noise are smoothed out

---

## 6. Decompose Trend vs Noise (Optional)

Using Pandas diff for simple trend detection:

```python
trend = ts - ts.rolling(window=30).mean()  # approximate noise
plt.figure(figsize=(12,5))
plt.plot(trend, label='Noise / Detrended')
plt.title("Noise vs Trend Approximation")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
```

**Insight:**

* Values oscillating around 0 → mostly noise
* Upward/downward movement → trend

---

## 7. Resample to Monthly or Weekly (Optional)

```python
monthly = ts.resample('M').mean()
plt.figure(figsize=(12,5))
plt.plot(monthly, marker='o', label='Monthly Average')
plt.title("Monthly Temperature Trend")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
```

* Helps see **long-term trends** clearly
* Combine with rolling mean for better visualization

---

## ✅ Key Takeaways

1. **Moving Average** smooths short-term fluctuations
2. 7-day → short-term trend, 30-day → long-term trend
3. Trend analysis is essential before building ARIMA or Prophet models
4. Always visualize raw + smoothed data for insights

---

# ⚠️ Pro Tips

* Avoid rolling window bigger than dataset length
* Always plot raw + rolling together
* Monthly resample works better for highly volatile daily data

---
