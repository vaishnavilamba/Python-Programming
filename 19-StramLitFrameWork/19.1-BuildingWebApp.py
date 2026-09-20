import streamlit as st
import pandas as pd
import numpy as np

st.title("HELLO! VAISHNAVI LAMBA")

st.write("This is a simple text")

df = pd.DataFrame({
    'First Column' : [1,2,3,4,5],
    'Second Column' : [10,20,30,40,50] 
})

st.write("Here is the data frame")
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)
