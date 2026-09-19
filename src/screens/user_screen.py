import streamlit as st
import tempfile
import os
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.services.transcription import transcribe_audio
from src.services.feedback import get_feedback
from src.services.insights import get_progress_insight
from src.database.db import get_user_sessions, save_session


def render_feedback_card(transcript, feedback):
    st.markdown(f"""
        <div style="background:#EFF5FC; border-radius:16px; padding:28px;
                    max-width:560px; margin:20px auto; box-shadow:0 4px 20px rgba(37,99,235,0.08);">
            <p style="color:#1B2A33; font-size:15px; margin-bottom:16px;">
                <strong>Your Transcript:</strong><br/>{transcript}
            </p>
            <hr style="border-color:#D6E6F7; margin:16px 0;">
            <p style="color:#1B2A33; font-size:15px; margin-bottom:8px;">
                <strong>Grammar:</strong> {feedback['grammar_score']}/10 — {feedback['grammar_feedback']}
            </p>
            <p style="color:#1B2A33; font-size:15px; margin-bottom:8px;">
                <strong>Fluency:</strong> {feedback['fluency_score']}/10 — {feedback['fluency_feedback']}
            </p>
            <p style="color:#1B2A33; font-size:15px;">
                <strong>Tip:</strong> {feedback['suggestion']}
            </p>
        </div>
    """, unsafe_allow_html=True)


def user_screen():
    if st.session_state.screen == "userscreen":

        nav_col1, nav_col2 = st.columns([4, 1])

        with nav_col1:
            header_dashboard()

        with nav_col2:
            st.write("")
            if st.button("Start Live Conversation", type="secondary"):
                st.session_state.screen = "conversation"
                st.rerun()
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

        audio = st.audio_input("Record your practice")

        if audio and audio.getvalue() != st.session_state.last_audio:

            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
                tmp_file.write(audio.getvalue())
                tmp_path = tmp_file.name

            with st.spinner("Transcribing..."):
                try:
                    transcript = transcribe_audio(tmp_path)
                    st.session_state.last_audio = audio.getvalue()
                    st.session_state.last_transcript = transcript

                    with st.spinner("Generating feedback..."):
                        feedback = get_feedback(transcript)
                        st.session_state.last_feedback = feedback

                    render_feedback_card(transcript, feedback)
                    save_session(user["user_id"], transcript, feedback)

                except Exception as e:
                    st.error(f"Error transcribing audio: {e}")
                finally:
                    if os.path.exists(tmp_path):
                        os.remove(tmp_path)
        else:
            if "last_transcript" in st.session_state and "last_feedback" in st.session_state:
                render_feedback_card(st.session_state.last_transcript, st.session_state.last_feedback)
            else:
                st.markdown("""
                    <div style="background:#EFF5FC; border-radius:16px; padding:40px; text-align:center;
                                max-width:480px; margin:0 auto; box-shadow:0 4px 20px rgba(37,99,235,0.08);">
                        <p style="color:#6B7A90; font-size:14px; margin-bottom:16px;">Your practice space</p>
                        <p style="color:#1B2A33; font-size:15px;">
                            Speaking practice and feedback features are coming soon.
                        </p>
                    </div>
                """, unsafe_allow_html=True)

        st.markdown("---")

        history_col1, history_col2, history_col3 = st.columns([1, 4, 1])
        with history_col2:
            sessions = get_user_sessions(user["user_id"])

            if sessions:
                st.subheader("Your Progress")

                chart_data = sessions[::-1]
                st.line_chart({
                    "Grammar": [s["grammar_score"] for s in chart_data],
                    "Fluency": [s["fluency_score"] for s in chart_data],
                })

                with st.spinner("Analyzing your recent sessions..."):
                    insight = get_progress_insight(sessions)

                st.markdown(f"""
                    <div style="background:#EFF5FC; border-radius:14px; padding:20px; margin-bottom:24px;">
                        <p style="color:#1B2A33; font-size:14px; margin-bottom:6px;"><strong>What to focus on:</strong></p>
                        <p style="color:#1B2A33; font-size:14px; margin:0;">{insight}</p>
                    </div>
                """, unsafe_allow_html=True)

            st.subheader("Your Practice History")

            if sessions:
                for s in sessions:
                    with st.expander(f"{s['created_at'][:10]} — Grammar: {s['grammar_score']}/10, Fluency: {s['fluency_score']}/10"):
                        st.markdown(f"**Transcript:** {s['transcript']}")
                        st.markdown(f"**Grammar feedback:** {s['grammar_feedback']}")
                        st.markdown(f"**Fluency feedback:** {s['fluency_feedback']}")
                        st.markdown(f"**Tip:** {s['suggestion']}")
            else:
                st.caption("No practice sessions yet — record something above to get started.")

        footer_dashboard()