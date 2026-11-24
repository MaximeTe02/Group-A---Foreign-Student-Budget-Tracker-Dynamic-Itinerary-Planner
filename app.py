import streamlit as st

st.title("Taipei Student Budget Tracker")

#LOGIN SCREEN
if st.session_state.user is None:
    st.subheader("Log In")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log In"):
        # Replace this temporary check with verify_user(username, password) later
        if username and password == "1234":
            st.session_state.user = username
            st.rerun()
        else:
            st.error("Invalid username or password.")

#MAIN APP
else:
    st.sidebar.write(f"Logged in as **{st.session_state.user}**")
    if st.sidebar.button("Log Out"):
        st.session_state.user = None
        st.rerun()

    budget = st.number_input("Weekly Budget (TWD)", min_value=0, value=3500)
    expense = st.number_input("New Expense Amount", min_value=0.0)
    currency = st.selectbox("Currency", ["TWD", "USD", "EUR", "JPY"])
    category = st.selectbox("Category", ["Food", "MRT", "Night Market", "Leisure"])

    if st.button("Log Expense"):
        st.success(f"Logged {expense} {currency} under {category}!")