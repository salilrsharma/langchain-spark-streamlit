import streamlit as st
import pandas as pd

st.title('Sample application')
st.markdown("Let's load Iris dataset")

df = pd.read_csv("./Data/irisdata.csv", header=None) 
df.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

st.write(df)

st.line_chart(df)