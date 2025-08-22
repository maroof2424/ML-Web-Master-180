import streamlit as st
import pandas as pd

st.set_page_config(page_title="Streamlit + Pandas Demo", layout="wide")

st.title("📊 Streamlit + Pandas (CSV Upload, Display, Filtering)")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV into Pandas DataFrame
    df = pd.read_csv(uploaded_file)

    st.subheader("Preview of Dataset")
    st.dataframe(df.head())

    st.markdown("---")

    # Show basic info
    st.subheader("Dataset Info")
    st.write(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
    st.write("Columns:", list(df.columns))

    # Select column for filtering
    col = st.selectbox("Select column to filter:", df.columns)

    if pd.api.types.is_numeric_dtype(df[col]):
        # Numeric filtering
        min_val = float(df[col].min())
        max_val = float(df[col].max())
        range_vals = st.slider(
            f"Select range for {col}", min_val, max_val, (min_val, max_val)
        )
        filtered_df = df[(df[col] >= range_vals[0]) & (df[col] <= range_vals[1])]
    else:
        # Categorical filtering
        unique_vals = df[col].unique()
        selected_vals = st.multiselect(f"Select values for {col}", unique_vals)
        if selected_vals:
            filtered_df = df[df[col].isin(selected_vals)]
        else:
            filtered_df = df

    st.subheader("🔍 Filtered Data")
    st.dataframe(filtered_df)

else:
    st.info("👆 Please upload a CSV file to begin.")
