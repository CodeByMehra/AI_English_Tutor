import streamlit as st


def footer_home():
    logo_url = "Link Here"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
        <p style="font-weight:bold; color:white;"> Created by Vishal Mehra</p>  
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "Link Here"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
        <p style="font-weight:bold; color:black;"> Created by Vishal Mehra</p>  
        </div>
                
                """, unsafe_allow_html=True)