import streamlit as st

st.title("💰 My Crazy Retail Shop 🤡")

if st.button("💸 MAKE IT RAIN! 💸"):
    st.markdown(
        """
        <style>
        @keyframes fall {
            0% {transform: translateY(-100px);}
            100% {transform: translateY(800px);}
        }

        .money {
            position: fixed;
            top: 0;
            font-size: 40px;
            animation: fall 3s linear infinite;
        }
        </style>

        <div class="money" style="left:10%;">💵</div>
        <div class="money" style="left:20%; animation-delay:0.4s;">💰</div>
        <div class="money" style="left:30%; animation-delay:0.8s;">💵</div>
        <div class="money" style="left:40%; animation-delay:0.2s;">💸</div>
        <div class="money" style="left:50%; animation-delay:1s;">💵</div>
        <div class="money" style="left:60%; animation-delay:0.5s;">💰</div>
        <div class="money" style="left:70%; animation-delay:1.2s;">💵</div>
        <div class="money" style="left:80%; animation-delay:0.7s;">💸</div>
        <div class="money" style="left:90%; animation-delay:0.3s;">💵</div>
        """,
        unsafe_allow_html=True
    )

    st.success("💰 MONEY MONEY MONEY! 💰")
