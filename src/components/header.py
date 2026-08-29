import streamlit as st

def header_home():
    logo_url = "https://i.ibb.co/0jpP8MjJ/Speak-Wise-Logo-front.png"
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; gap:14px; margin-bottom:36px; margin-top:36px">
            <img src="{logo_url}" style="height:90px; border-radius:18px; box-shadow:0 4px 14px rgba(37,99,235,0.15);">
            <h1 style="text-align:center; color:#1B2A33; font-weight:700; letter-spacing:-0.5px; margin:0;">SpeakWise</h1>
            <p style="text-align:center; color:#5B7185; font-size:14px; margin:0;">Practice speaking. Get real feedback.</p>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():
    logo_url = "https://i.ibb.co/0jpP8MjJ/Speak-Wise-Logo-front.png"
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:14px; padding:12px 0;">
            <img src="{logo_url}" style="height:48px; border-radius:12px;">
            <h2 style="text-align:left; color:#2563EB; font-weight:700; margin:0;">SpeakWise</h2>
        </div>
    """, unsafe_allow_html=True)