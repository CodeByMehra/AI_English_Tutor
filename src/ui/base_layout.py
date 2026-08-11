import streamlit as st


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300..700&display=swap');

        h1, h2, h3 {
            font-family: 'Sora', sans-serif !important;
            color: #1F2A1F !important;
        }

        html, body, p, span, div, label, input, button {
            font-family: 'Outfit', sans-serif !important;
        }

        #MainMenu, footer, header { visibility: hidden; }

        button {
            background-color: #2F7D5C !important;
            color: white !important;
            border-radius: 10px !important;
            border: none !important;
        }
        button:hover {
        transform: scale(1.05) !important;
        transition: transform 0.2s ease-in-out !important;
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

