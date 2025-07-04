import streamlit as st
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
}
df = pd.DataFrame(data)


st.title('Hi welcome to this page')
st.subheader('Lets walk you around')
st.write('''Lets work you around a little I am ibude Precious. 
         A python develoepr in training
         Welcome to this demo webapp\n
         I will publishing my projects here in the follwing weeks''')
st.write(df)
st.line_chart(df['Age'])