Day 5-6 ke liye hum ek **Streamlit mini project**

---

### 📂 Project Structure

```
05_mini_project/
│── app.py
│── sample_data.csv
│── requirements.txt
```

---

### 🐍 Code: `app.py`

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Sidebar – File Upload
# -------------------------------
st.sidebar.header("📂 Upload your CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

# -------------------------------
# Main Title
# -------------------------------
st.title("📊 EDA Web App + 🤖 AI Assistant")

# -------------------------------
# Part 1: EDA Section
# -------------------------------
st.header("📈 Exploratory Data Analysis")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### 🔍 Dataset Preview", df.head())

    st.write("### 📊 Summary Statistics")
    st.write(df.describe())

    # Column selection
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    selected_col = st.selectbox("Select Column for Visualization", numeric_cols)

    if selected_col:
        fig, ax = plt.subplots(1, 2, figsize=(12, 4))

        sns.histplot(df[selected_col], kde=True, ax=ax[0])
        ax[0].set_title(f"Histogram of {selected_col}")

        sns.boxplot(y=df[selected_col], ax=ax[1])
        ax[1].set_title(f"Boxplot of {selected_col}")

        st.pyplot(fig)
else:
    st.info("Please upload a CSV file to begin EDA.")

# -------------------------------
# Part 2: AI Assistant Section
# -------------------------------
st.header("🤖 AI Assistant (Demo)")

user_input = st.text_input("Ask me anything:")

if st.button("Send"):
    if user_input:
        # Placeholder logic (later you can connect OpenAI API or Llama.cpp, etc.)
        st.write(f"**You asked:** {user_input}")
        st.success("🤖 AI Assistant: This is a dummy response. Connect an LLM API here!")
    else:
        st.warning("Please type something to ask.")
```

---

### 📂 `requirements.txt`

```
streamlit
pandas
matplotlib
seaborn
```

---

### 📊 Sample Run

```bash
cd 05_mini_project
streamlit run app.py
```

---

