import streamlit as st
from src.database.db import signup_user

def signup_dialog():
    if st.session_state.screen == "signup":
        st.header("you are at signup page")
        name = "Enter yout name"
        username = "Create Username"
        email = st.text_input("Enter Email")
        password = st.text_input("Enter Password")
        if st.button("Submit", type="primary"):
            signup_user(name, username, email, password)
            