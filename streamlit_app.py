import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.header('Belajar st.write')

# Contoh 1

st.write('Hello, *World!* :sunglasses:')

st.write('1234')

df = pd.DataFrame(
    {'first column': [1, 2, 3, 4], 'second column': [10, 20, 30, 40]})

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

st.write(df2)

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
