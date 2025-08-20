import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Streamlit Visuals", layout="wide")

st.title("📊 Streamlit + Matplotlib + Seaborn Visualizations")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    
    st.write("### Preview of Data")
    st.dataframe(df.head())

    st.sidebar.header("Filters")
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

    x_axis = st.sidebar.selectbox("Select X-axis", options=numeric_cols)
    y_axis = st.sidebar.selectbox("Select Y-axis", options=numeric_cols)

    st.write(f"### 🔵 Scatter Plot ({x_axis} vs {y_axis})")
    fig, ax = plt.subplots()
    ax.scatter(df[x_axis], df[y_axis], alpha=0.7)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    st.pyplot(fig)

    st.write("### 📊 Distribution Plot")
    col = st.selectbox("Select column for Histogram", options=numeric_cols)
    fig, ax = plt.subplots()
    sns.histplot(df[col], kde=True, ax=ax)
    st.pyplot(fig)

    if categorical_cols:
        st.write("### 📦 Box Plot")
        cat_col = st.selectbox("Select Categorical Column", options=categorical_cols)
        num_col = st.selectbox("Select Numerical Column", options=numeric_cols)
        fig, ax = plt.subplots()
        sns.boxplot(x=df[cat_col], y=df[num_col], ax=ax)
        st.pyplot(fig)

else:
    st.info("👆 Please upload a CSV file to start.")
