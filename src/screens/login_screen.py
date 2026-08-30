import streamlit as st
from src.components.dialog_signup import signup_dialog
from src.components.footer import footer_dashboard
from src.database.db import login_user


def login_screen():
    if "login" not in st.session_state.screen:
        st.session_state.screen = "login"

    if st.session_state.screen == "login":

        col1, col2 = st.columns(2)

        with col1:
            st.image("https://i.ibb.co/gZQr6T6k/login-illustration.png", use_container_width=True)

        with col2:
            st.header("Login")
            username = st.text_input("Enter your username")
            password = st.text_input("Enter Password", type="password")

            if st.button("Log in", type="primary"):
                if st.button("Log in", type="primary"):
                    success, result = login_user(username, password)
                    if success:
                        st.success("Logged in successfully!")
                    else:
                        st.error(result)

            st.text("Dont have an account?")
            if st.button("Sign up", type="secondary"):
                st.session_state.screen = "signup"
                st.rerun()
        footer_dashboard()