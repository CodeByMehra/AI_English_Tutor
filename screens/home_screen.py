import streamlit as st


col1, col2 = st.columns 

with col1:
    st.image
    
with col2:
    st.header("Login")
    st.text_input("Enter your username")
    st.text_input("Enter Password")
    
    st.text("Dont have an account?")
    st.link_button("Sign up")