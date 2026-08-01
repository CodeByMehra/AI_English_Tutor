# File for streamlit
import streamlit as st
from src.screens.login_screen import login_screen

def main():
    st.header("English Tutor")
    
    if st.button("Start"):
        login_screen()
        
        
main()