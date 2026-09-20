import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")
name = st.text_input("Enter your name : ")

if name:
    st.write(f"Hello, {name}")

age = st.slider("Select your age : ") 
st.write(f"Your age is {age}")

options = ['Python','JAVA','C++','Java Script']
choice = st.selectbox('Choose your favourite language : ',options=options)

data = {
    'Name' : ['Joey','Chandler','Monica','Ross','Rachel','Pheebe'],
    'Age' : [30,28,30,31,29,27],
    'City' : ['New York','Loss Angless','Chicago','Houston','America','London']
}



df = pd.DataFrame(data)
# df.to_csv('Sampledata.csv')
st.subheader("--- Friends show Data ---")
st.write(df)

uploaded_file = st.file_uploader('Choose a csv file',type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)