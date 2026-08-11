import streamlit as st
from src.components.dialog_signup import signup_dialog
from src.components.footer import footer_home


def login_screen():
    if "login" not in st.session_state.screen:
        st.session_state.screen = "login"
        
    if st.session_state.screen == "login":
        
        col1, col2 = st.columns(2)

        with col1:
            st.image
            
        with col2:
            st.header("Login")
            st.text_input("Enter your username")
            st.text_input("Enter Password")
            
            st.text("Dont have an account?")
            if st.button("Sign up") :
                st.session_state.screen = "signup"
                st.rerun()
                
        footer_home()
        