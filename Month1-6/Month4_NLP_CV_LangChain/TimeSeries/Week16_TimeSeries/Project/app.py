import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from prophet import Prophet
from statsmodels.tsa.arima.model import ARIMA

# =======================
# Forecast Functions
# =======================
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

# =======================
# Streamlit UI
# =======================
st.title("Time Series Forecasting Dashboard")
st.write("Upload CSV, choose model and forecast range")

uploaded_file = st.file_uploader("Upload your CSV", type=['csv'])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:", df.head())
    
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
    
    model_option = st.selectbox("Select Forecast Model", ["ARIMA", "Prophet"])
    days = st.selectbox("Select Forecast Range", [7, 30, 90])
    
    if st.button("Run Forecast"):
        ts = df['meantemp']
        
        if model_option == "ARIMA":
            forecast = forecast_arima(ts, steps=days)
            forecast_df = pd.DataFrame({'date':forecast.index, 'forecast':forecast.values})
        else:  # Prophet
            df_prophet = df[['meantemp']].reset_index().rename(columns={'date':'ds', 'meantemp':'y'})
            forecast_prophet_df = forecast_prophet(df_prophet, steps=days)  # NOW it works
            forecast_df = forecast_prophet_df[['ds','yhat']].rename(columns={'ds':'date','yhat':'forecast'})
        
        st.write("Forecast Preview:", forecast_df.head())

        # Plotting
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df.index, y=df['meantemp'], mode='lines', name='Actual'))
        fig.add_trace(go.Scatter(x=forecast_df['date'], y=forecast_df['forecast'], mode='lines', name='Forecast'))
        fig.update_layout(title="Actual vs Forecast", xaxis_title="Date", yaxis_title="Temperature (°C)")
        st.plotly_chart(fig)

        # Download CSV
        csv = forecast_df.to_csv(index=False)
        st.download_button("Download Forecast CSV", csv, file_name='forecast.csv', mime='text/csv')
