import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
        .stApp { background: #E6F0F7 !important; }
        </style>
    """, unsafe_allow_html=True)

def style_background_dashboard():
    pass

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300..700&display=swap');

        h1, h2, h3 {
            font-family: 'Sora', sans-serif !important;
            color: #1B2A33 !important;
        }

        html, body, p, span, div, label, input, button {
            font-family: 'Outfit', sans-serif !important;
        }

        #MainMenu, footer, header { visibility: hidden; }

        div.stButton > button[kind="primary"] {
            background-color: #2563EB !important;
            color: white !important;
            border-radius: 10px !important;
            border: none !important;
        }

        div.stButton > button[kind="secondary"] {
            background-color: transparent !important;
            color: #2563EB !important;
            border: 1.5px solid #2563EB !important;
            border-radius: 10px !important;
        }

        div.stButton > button[kind="tertiary"] {
            background-color: transparent !important;
            color: #1B2A33 !important;
            border: none !important;
            text-decoration: underline !important;
        }

        div.stButton > button:hover {
            transform: scale(1.05) !important;
            transition: transform 0.2s ease-in-out !important;
        }
        </style>
    """, unsafe_allow_html=True)