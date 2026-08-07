# File for streamlit
import streamlit as st
from src.screens.login_screen import login_screen

def main():
   
    if "screen" not in st.session_state:
        st.session_state.screen = "start"

    if st.session_state.screen == "start":
        st.header("English Tutor")
        
        if st.button("Start"):
            st.session_state.screen = "login"
            st.rerun()

    elif st.session_state.screen == "login":
        login_screen()
        
main()