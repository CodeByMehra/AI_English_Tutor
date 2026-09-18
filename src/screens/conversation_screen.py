import streamlit as st
import tempfile
import os
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.services.transcription import transcribe_audio
from src.services.conversation import get_ai_reply
from src.services.voice_reply import synthesize_speech


def conversation_screen():
    header_dashboard()

    st.markdown("""
        <div style="text-align:center; margin-bottom:24px;">
            <h1 style="color:#1B2A33; font-weight:700;">Live Conversation</h1>
            <p style="color:#5B7185; font-size:16px;">Talk naturally — I'll reply back.</p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Back to Dashboard", type="tertiary"):
        st.session_state.screen = "userscreen"
        st.rerun()

    if "conversation" not in st.session_state:
        st.session_state.conversation = []
    if "last_conv_audio" not in st.session_state:
        st.session_state.last_conv_audio = None

    for turn in st.session_state.conversation:
        speaker = "You" if turn["role"] == "user" else "SpeakWise"
        st.markdown(f"**{speaker}:** {turn['text']}")

    if "last_ai_audio" in st.session_state:
        st.audio(st.session_state.last_ai_audio)

    audio = st.audio_input("Speak your turn")

    if audio and audio.getvalue() != st.session_state.last_conv_audio:
        st.session_state.last_conv_audio = audio.getvalue()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            tmp_file.write(audio.getvalue())
            tmp_path = tmp_file.name

        try:
            with st.spinner("Listening..."):
                user_text = transcribe_audio(tmp_path)
                st.session_state.conversation.append({"role": "user", "text": user_text})

            with st.spinner("Thinking..."):
                ai_text = get_ai_reply(st.session_state.conversation)
                st.session_state.conversation.append({"role": "ai", "text": ai_text})

            with st.spinner("Speaking..."):
                audio_path = synthesize_speech(ai_text)
                st.session_state.last_ai_audio = audio_path

            st.rerun()

        except Exception as e:
            st.error(f"Something went wrong: {e}")
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    if st.button("Reset conversation", type="tertiary"):
        st.session_state.conversation = []
        st.session_state.last_conv_audio = None
        if "last_ai_audio" in st.session_state:
            del st.session_state.last_ai_audio
        st.rerun()

    footer_dashboard()
