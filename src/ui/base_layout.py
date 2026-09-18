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

        .block-container {
            padding-top: 2rem !important;
        }

        h1, h2, h3 {
            font-family: 'Sora', sans-serif !important;
            color: #1B2A33 !important;
        }

        .stApp p, .stMarkdown, label, .stCaption {
            font-family: 'Outfit', sans-serif !important;
            color: #1B2A33 !important;
        }

        div[data-baseweb="input"] input {
            background-color: #FFFFFF !important;
            color: #1B2A33 !important;
        }

        div[data-baseweb="input"] input::placeholder {
            color: #8B98A8 !important;
        }

        #MainMenu, footer, header,
        [data-testid="stToolbar"],
        .stAppDeployButton {
            visibility: hidden;
        }

        div.stButton > button[kind="primary"] {
            background-color: #2563EB !important;
            color: white !important;
            border-radius: 10px !important;
            border: none !important;
        }

        div.stButton > button[kind="secondary"] {
            background-color: #FFFFFF !important;
            color: #2563EB !important;
            border: 1.5px solid #2563EB !important;
            border-radius: 10px !important;
        }

        div.stButton > button[kind="tertiary"] {
            background-color: transparent !important;
            color: #5B7185 !important;
            border: none !important;
            text-decoration: underline !important;
        }

        div.stButton > button:hover {
            transform: scale(1.05) !important;
            transition: transform 0.2s ease-in-out !important;
        }
        </style>
    """, unsafe_allow_html=True)