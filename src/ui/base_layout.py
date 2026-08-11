import streamlit as st


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif !important;
        }

        #MainMenu, footer, header { visibility: hidden; }

        button {
            background-color: #2F7D5C !important;
            color: white !important;
            border-radius: 10px !important;
            border: none !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    

def style_background_home():
     st.markdown("""
        <style>
        .stApp { background:#E8F0E9 !important; }
        </style>
    """, unsafe_allow_html=True)

def style_background_dashboard():
    pass

