import streamlit as st

def user_screen():
    if "userscreen" not in st.session_state.screen:
            st.session_state.screen = "userscreen"
    
        if st.session_state.screen == "userscreen":