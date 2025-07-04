import streamlit as st
import pandas as pd

data = {
    'Inome': [1000, 3000, 30000],
    'Age': [25, 30, 35],
    'Name': ['Precious', 'John', 'Doe'],
}
df = pd.DataFrame(data, index=data['Name'])


st.title('Hi welcome to this page')
st.subheader('Lets walk you around')
st.write('''Lets work you around a little I am ibude Precious. 
         A python develoepr in training
         Welcome to this demo webapp\n
         I will publishing my projects here in the follwing weeks''')
st.write(df)
st.line_chart(df)