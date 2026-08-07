import streamlit as st
from src.dialogs.dialog_signup import signup_dialog


def login_screen():
    col1, col2 = st.columns(2)

    with col1:
        st.image
        
    with col2:
        st.header("Login")
        st.text_input("Enter your username")
        st.text_input("Enter Password")
        
        st.text("Dont have an account?")
        if st.button("Sign up") :
            signup_dialog()