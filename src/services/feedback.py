import streamlit as st
from google import genai
import json

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def get_feedback(transcript):
    prompt = f"""You are an English speaking coach. Analyze this transcript from a language learner's spoken practice session.

Transcript: "{transcript}"

Respond ONLY with valid JSON in this exact format, no other text:
{{
  "grammar_score": <1-10>,
  "fluency_score": <1-10>,
  "grammar_feedback": "<one specific sentence on grammar>",
  "fluency_feedback": "<one specific sentence on fluency/flow>",
  "suggestion": "<one actionable tip for improvement>"
}}"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    raw_text = response.text.strip()
    if raw_text.startswith("```"):
        raw_text = raw_text.split("```")[1].replace("json", "", 1).strip()

    return json.loads(raw_text)