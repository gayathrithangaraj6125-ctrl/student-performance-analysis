import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🎓 Student Performance Dashboard")

# Load data
data = pd.read_csv("data/student.csv")

# Dataset preview
st.subheader("Dataset Preview")
st.write(data.head())

# Math Score Distribution
st.subheader("Math Score Distribution")

fig1, ax1 = plt.subplots()
sns.histplot(data["math score"], bins=20, ax=ax1)
st.pyplot(fig1)

# Heatmap
st.subheader("Correlation Heatmap")

numeric_data = data.select_dtypes(include=['int64'])
corr = numeric_data.corr()

fig2, ax2 = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax2)
st.pyplot(fig2)