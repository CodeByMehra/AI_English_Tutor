import streamlit as st
import os
from groq import Groq

def transcribe_audio(audio_file_path):
    """Transcribes audio using Groq Whisper API."""
    client = Groq(api_key= st.secrets["GROQ_API_KEY"])
    with open(audio_file_path, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(audio_file_path, file.read()),
            model="whisper-large-v3-turbo",
            response_format="json",
        )
    return transcription.text
