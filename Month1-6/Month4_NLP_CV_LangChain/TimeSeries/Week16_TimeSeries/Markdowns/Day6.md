# Day 6 — Forecasting Dashboard (Streamlit + Plotly)

## ✅ Objectives

* Upload your dataset via Streamlit
* Select **model** (ARIMA or Prophet)
* Choose **forecast range** (7 / 30 / 90 days)
* Plot **actual vs predicted** using Plotly
* Option to **download forecast CSV**
* Use **caching** for performance

---

## 1. Install Required Libraries

```bash
pip install streamlit plotly prophet statsmodels pandas
```

---

## 2. Import Libraries

```python
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from prophet import Prophet
from statsmodels.tsa.arima.model import ARIMA
```

---

## 3. Streamlit Layout

```python
st.title("Time Series Forecasting Dashboard")
st.write("Upload CSV, choose model and forecast range")
```

---

## 4. File Upload

```python
uploaded_file = st.file_uploader("Upload your CSV", type=['csv'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:", df.head())
    
    # Prepare for time series
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
```

---

## 5. Model Selection & Forecast Range

```python
model_option = st.selectbox("Select Forecast Model", ["ARIMA", "Prophet"])
days = st.selectbox("Select Forecast Range", [7, 30, 90])
```

---

## 6. Forecast Function with Caching

**Caching prevents re-running model if input unchanged**

```python
@st.cache_data
def forecast_arima(ts, p=2, d=1, q=2, steps=30):
    model = ARIMA(ts, order=(p,d,q))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=steps)
    return forecast

@st.cache_data
def forecast_prophet(df_prophet, steps=30):
    model = Prophet(daily_seasonality=True)
    model.fit(df_prophet)
    future = model.make_future_dataframe(periods=steps)
    forecast = model.predict(future)
    return forecast
```

---

## 7. Run Forecast Based on Selection

```python
if st.button("Run Forecast"):
    ts = df['meantemp']
    
    if model_option == "ARIMA":
        forecast = forecast_arima(ts, steps=days)
        forecast_df = pd.DataFrame({'date':forecast.index, 'forecast':forecast.values})
    else:  # Prophet
        df_prophet = df[['meantemp']].reset_index().rename(columns={'date':'ds', 'meantemp':'y'})
        forecast_prophet_df = forecast_prophet(df_prophet, steps=days)
        forecast_df = forecast_prophet_df[['ds','yhat']].rename(columns={'ds':'date','yhat':'forecast'})
    
    st.write("Forecast Preview:", forecast_df.head())
```

---

## 8. Plot Actual + Forecast using Plotly

```python
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['meantemp'], mode='lines', name='Actual'))
fig.add_trace(go.Scatter(x=forecast_df['date'], y=forecast_df['forecast'], mode='lines', name='Forecast'))
fig.update_layout(title="Actual vs Forecast", xaxis_title="Date", yaxis_title="Temperature (°C)")
st.plotly_chart(fig)
```

---

## 9. Download Forecast CSV

```python
csv = forecast_df.to_csv(index=False)
st.download_button("Download Forecast CSV", csv, file_name='forecast.csv', mime='text/csv')
```

---

## ✅ Honest Advice

1. **Use caching** (`@st.cache_data`) → avoids recomputation and speeds up dashboard
2. **Use Plotly** → Streamlit’s `st.line_chart` is very basic and less interactive
3. **Keep UI clean** → model selection + forecast range + upload + plot + download in one column
4. Optional: Add **metric cards** (mean, max, min forecast) for better insights

---

# ⚠️ Tips for Smooth Dashboard

* Validate uploaded CSV for correct columns (`date`, `meantemp`)
* Handle missing values before forecasting
* Use try/except blocks for model fitting errors
* Keep rolling averages / trend plots optional for more insight

---