import streamlit as st
from src.database.db import signup_user

def signup_dialog():
    st.header("you are at signup")
    email = st.text_input("Enter Email")
    password = st.text_input("Enter Password")
    signup_user(email, password)