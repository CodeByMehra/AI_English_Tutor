import streamlit as st
from src.database.db import signup_user

def signup_dialog():
    if st.session_state.screen == "signup":
        st.header("you are at signup")
        
        name = st.text_input("Enter yout name")
        username = st.text_input("Create Username")
        email = st.text_input("Enter Email")
        password = st.text_input("Enter Password", type="password")
        if st.button("Submit", type="primary"):
            success, message = signup_user(name, username, email, password)
            if success:
                st.success(message)
            else:
                st.error(message)
                        