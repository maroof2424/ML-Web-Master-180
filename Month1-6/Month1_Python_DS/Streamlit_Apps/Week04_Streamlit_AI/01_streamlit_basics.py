import streamlit as st


st.title("Hello Streamlit")
st.header("Week 4 day1 Streamlit Basic")

st.write("THis is a Basic Streamlit app to get Started")
st.markdown("**Bold Heading**,_italic text_ and `code` ")

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:",min_value=0,max_value=100)

if st.button("Submit"):
    if not name or age <= 0:
        st.warning("Please enter your name or age must be greater than 0")
    else:
        st.success(f"Hello {name}, you are {age} years old!")

col1,col2 = st.columns(2)

with col1:
    st.info("This is column 1")
with col2:
    st.warning("This is column 2")
    
st.write("Sample Data:")
st.dataframe({"name":["Alice","Bob"],"Score":[90,85]})