import streamlit as st

st.title("Taipei Student Budget Tracker")

budget = st.number_input("Weekly Budget (TWD)", min_value=0, value=3500)
expense = st.number_input("New Expense Amount", min_value=0.0)
currency = st.selectbox("Currency", ["TWD", "USD", "EUR", "JPY"])
category = st.selectbox("Category", ["Food", "MRT", "Night Market", "Leisure"])

if st.button("Log Expense"):
    st.success(f"Logged {expense} {currency} under {category}!")