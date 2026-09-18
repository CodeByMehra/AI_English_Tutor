import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def get_ai_reply(conversation_history):
    history_text = "\n".join([f"{turn['role']}: {turn['text']}" for turn in conversation_history])

    prompt = f"""You are a friendly English conversation partner helping someone practice speaking.
Keep replies short (1-3 sentences, under 200 characters), natural, and ask a follow-up question to keep the conversation going.
Gently note any obvious grammar mistake in passing, but stay conversational, not like a teacher grading.

Conversation so far:
{history_text}

Reply as the AI partner:"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    return response.text.strip()
