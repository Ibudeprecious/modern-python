import streamlit as st
import pandas as pd

Name = ['Precious', 'John', 'Doe']
data = {
    'Income': [100, 120, 140],
    'Age': [25, 30, 35],
}
df = pd.DataFrame(data, index=Name)
df.index.name = 'Name'


st.title('Hi welcome to this page')
st.subheader('Lets walk you around')
st.write('''Lets work you around a little I am ibude Precious. 
         A python develoepr in training
         Welcome to this demo webapp\n
         I will publishing my projects here in the follwing weeks''')
st.write(df)
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
age = st.slider('Select your age', 0, 100, 25)
st.write(f'Your age is {age}, your predicted income is ${age * 4}')