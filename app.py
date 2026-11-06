import streamlit as st

st.title("Ameeth and Teams first website at Regent Business School")

st.write("Welcome to my website!")

name = st.text_input("Enter your name")

if st.button("Submit"):

  st.write("Hello", name)

