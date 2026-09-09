import streamlit as st
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

from src.services.feedback import get_feedback


def user_screen():
    if st.session_state.screen == "userscreen":

        nav_col1, nav_col2 = st.columns([4, 1])

        with nav_col1:
            header_dashboard()

        with nav_col2:
            st.write("")  # small vertical spacer to align button with logo
            if st.button("Log out", type="tertiary"):
                del st.session_state.user
                st.session_state.screen = "login"
                st.rerun()

        st.markdown("<hr style='margin-top:0; margin-bottom:24px; border-color:#DCE8F5;'>", unsafe_allow_html=True)

        user = st.session_state.user

        st.markdown(f"""
            <div style="text-align:center; margin-bottom:36px;">
                <h1 style="color:#1B2A33; font-weight:700; margin-bottom:6px;">
                    Welcome back, {user['name']}
                </h1>
                <p style="color:#5B7185; font-size:16px;">
                    Ready to practice your English today?
                </p>
            </div>
        """, unsafe_allow_html=True)
        if "last_audio" not in st.session_state:
            st.session_state.last_audio = None
        audio = st.audio_input("Record your practice") # testing line 

        if audio and audio.getvalue() != st.session_state.last_audio:
            import tempfile
            import os
            from src.services.transcription import transcribe_audio

            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                tmp_file.write(audio.getvalue())
                tmp_path = tmp_file.name

            with st.spinner("Transcribing..."):
                try:
                    transcript = transcribe_audio(tmp_path)
                    st.success("Transcription Complete!")
                    st.markdown(f"**Your Transcript:**\n\n> {transcript}")
                    st.session_state.last_audio = audio.getvalue()
                    st.session_state.last_transcript = transcript
                    
                    with st.spinner("Generating feedback..."):
                        feedback = get_feedback(transcript)
                        st.session_state.last_feedback = feedback
                except Exception as e:
                    st.error(f"Error transcribing audio: {e}")
                finally:
                    if os.path.exists(tmp_path):
                        os.remove(tmp_path)
        else:
            if "last_transcript" in st.session_state:
                st.markdown(f"**Your Transcript:**\n\n> {st.session_state.last_transcript}")
                st.markdown(f"""
                    **Grammar:** {feedback['grammar_score']}/10 — {feedback['grammar_feedback']}

                    **Fluency:** {feedback['fluency_score']}/10 — {feedback['fluency_feedback']}

                    **Tip:** {feedback['suggestion']}
                """)
            else:
                st.markdown("""
                    <div style="background:#FFFFFF; border-radius:16px; padding:40px; text-align:center;
                                max-width:480px; margin:0 auto; box-shadow:0 4px 20px rgba(37,99,235,0.08);">
                        <p style="color:#6B7A90; font-size:14px; margin-bottom:16px;">Your practice space</p>
                        <p style="color:#1B2A33; font-size:15px;">
                            Speaking practice and feedback features are coming soon.
                        </p>
                    </div>
                """, unsafe_allow_html=True)

        footer_dashboard()