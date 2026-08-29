# File for streamlit
import streamlit as st
from src.screens.login_screen import login_screen
from src.components.dialog_signup import signup_dialog
from src.components.header import header_home
from src.ui.base_layout import style_background_home ,  style_base_layout

def main():
    style_background_home()
    style_base_layout()
    header_home()
   
    if "screen" not in st.session_state:
        st.session_state.screen = "start"

    if st.session_state.screen == "start":
        st.header("Your Personalized English Tutor")
        
        if st.button("Start"):
            st.session_state.screen = "login"
            st.rerun()

    elif st.session_state.screen == "login":
        login_screen()
    elif st.session_state.screen == "signup":
        signup_dialog()
        
main()