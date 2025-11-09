
 Day 1 — Intro to Time Series + Visualization

## ✅ Objectives

* Understand what a Time Series is
* Parse date correctly and set it as index
* Visualize trends in the data
* Identify seasonality and noise

---

## 1. What is a Time Series?

A **Time Series** is a sequence of data points collected over time in chronological order.
**Examples:**

* Daily sales
* Temperature readings
* Stock prices
* COVID cases

**Key point:** Time is an essential component; you cannot shuffle the data.

---

## 2. Load the Dataset

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load train dataset
df = pd.read_csv("DailyDelhiClimateTrain.csv")
display(df.head())
```

---

## 3. Inspect Columns and Data Types

```python
print(df.columns)
print(df.dtypes)
```

**Goal:** Ensure the `date` column exists and is not already a datetime object.

---

## 4. Convert `date` to Datetime

```python
df['date'] = pd.to_datetime(df['date'], dayfirst=False, errors='coerce')
```

* `errors='coerce'` converts invalid dates to NaT (missing)
* Check for NaT:

```python
df[df['date'].isna()]
```

---

## 5. Sort by Date

```python
df.sort_values('date', inplace=True)
```

Sorting ensures chronological order, which is required for rolling calculations and forecasting models.

---

## 6. Set `date` as Index

```python
df.set_index('date', inplace=True)
print(type(df.index))  # should be DatetimeIndex
```

---

## 7. Basic Line Plot

```python
plt.figure(figsize=(12,5))
plt.plot(df.index, df['meantemp'])
plt.title("Daily Mean Temperature in Delhi")
plt.xlabel("Date")
plt.ylabel("Mean Temperature (°C)")
plt.grid(True)
plt.show()
```

* Observe general trend
* Look for spikes, patterns, seasonality

---

## 8. Resample Monthly (Optional)

```python
monthly = df['meantemp'].resample('M').mean()
plt.figure(figsize=(12,5))
plt.plot(monthly.index, monthly, marker='o')
plt.title("Monthly Average Temperature")
plt.show()
```

---

## 9. Rolling Mean (Optional)

```python
rolling = df['meantemp'].rolling(window=30).mean()
plt.figure(figsize=(12,5))
plt.plot(df.index, df['meantemp'], alpha=0.4, label='Raw')
plt.plot(rolling.index, rolling, label='30-day MA', linewidth=2)
plt.legend()
plt.show()
```

* Smooths out noise
* Helps visualize trend clearly

---

## 10. Check Missing Values

```python
print(df.isna().sum())
```

* Handle missing values with interpolation:

```python
df['meantemp'].interpolate(method='time', inplace=True)
```

---

## ✅ Summary

* **Time Series = Data + Time**
* Always parse dates → sort → set index
* Plot to understand trends before modeling
* Day 1 focus: **understanding the data, not modeling yet**
