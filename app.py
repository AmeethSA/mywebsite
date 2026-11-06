import streamlit as st

st.title("💰 My Crazy Retail Shop 🤡")
st.write("Welcome! Let us make some money! 💵💵💵")

product = st.text_input("🛒 Enter product name")
price = st.number_input("💰 Enter price", min_value=0.0)
quantity = st.number_input("📦 Enter quantity", min_value=1)

total = price * quantity

if st.button("💸 Calculate my damage!"):
    
    st.write("🛍️ Product:", product)
    st.write("💰 Total cost: R", total)

    if total >= 1000:
        st.warning("🤡 WHOA! My wallet is crying! 💸😭")
        st.balloons()
    else:
        st.success("🎉 Not bad! We still have some money left! 💵")
