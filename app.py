# File for streamlit
import streamlit as st
from src.screens.login_screen import login_screen
from src.screens.user_screen import user_screen
from src.screens.conversation_screen import conversation_screen
from src.components.dialog_signup import signup_dialog
from src.components.header import header_home
from src.ui.base_layout import style_background_home, style_base_layout


def main():
    style_background_home()
    style_base_layout()

    if "screen" not in st.session_state:
        st.session_state.screen = "start"

    if st.session_state.screen == "start":
        header_home()

        st.markdown("""
            <div style="text-align:center; margin-bottom:24px;">
                <h2 style="color:#1B2A33; font-weight:600;">Your Personalized English Tutor</h2>
            </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([2, 1, 2])
        with col2:
            if st.button("Start", type="primary", use_container_width=True):
                st.session_state.screen = "login"
                st.rerun()

    elif st.session_state.screen in ("login", "signup"):
        login_screen()
    elif st.session_state.screen == "userscreen":
        user_screen()
    elif st.session_state.screen == "conversation":
        conversation_screen()


main()