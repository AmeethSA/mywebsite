import streamlit as st

st.title("Ameeth's first website at Regent Business School")

st.write("Welcome to my website!")

name = st.text_input("Enter your name")

if st.button("Submit"):

  st.write("Hello", name)

import streamlit as st

st.title("Retail Sales Calculator")

product = st.text_input("Product name")
price = st.number_input("Price", min_value=0.0)
quantity = st.nimport streamlit as st

st.title("Retail Sales Calculator")

product = st.text_input("Product name")
price = st.number_input("Price", min_value=0.0)
quantity = st.number_input("Quantity", min_value=1)

total = price * quantity

if st.button("Calculate"):
    st.write("Product:", product)
    st.write("Total: R", total)umber_input("Quantity", min_value=1)

total = price * quantity

if st.button("Calculate"):
    st.write("Product:", product)
    st.write("Total: R", total)
