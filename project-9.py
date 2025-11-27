#STREAMLI DASHBOARD

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Streamlit App of My Resume")
st.text("Welcome to your Dashboard")
st.header("I'm a header")

st.write("You can write", 10 * 5)

# User Input
name = st.text_input("Enter your name")
age = st.number_input("Your age", min_value=0, step=1)

st.write("Your name is:", name, "Your age is:", age)

# Course Selection
st.selectbox("Enter your course", ["MCA", "BTECH", "BCA"])

# Click Button
if st.button("Click ME"):
    st.success("Clicked Button")

# File Upload
file = st.file_uploader("Upload your file")
if file:
    content = file.read()
    st.write("File uploaded successfully")

# Sample DataFrame
data = {"Name": ["Abhinash", "Dev", "Harry", "Kumar"], "Marks": [10, 20, 45, 64]}
df = pd.DataFrame(data)
st.dataframe(df)

# Line Chart and Bar Chart
marks_data = pd.DataFrame({"Marks": [10, 20, 45, 64]})
st.line_chart(marks_data)
st.bar_chart(marks_data)

# Pie Chart
subject = ["python", "c++", "java", "c"]
marks = [20, 10, 54, 78]

fig, ax = plt.subplots()
ax.pie(marks, labels=subject, autopct="%1.1f%%")
st.pyplot(fig)
