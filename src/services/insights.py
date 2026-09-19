import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])


def get_progress_insight(sessions):
    """Analyzes recent sessions to find recurring patterns worth focusing on."""
    if len(sessions) < 2:
        return "Complete a few more sessions to start seeing patterns in your progress."

    recent = sessions[:5]  # most recent 5, since sessions are already sorted newest-first
    feedback_summary = "\n".join([
        f"- Grammar: {s['grammar_feedback']} | Fluency: {s['fluency_feedback']}"
        for s in recent
    ])

    prompt = f"""Here is feedback from a language learner's last {len(recent)} speaking practice sessions, most recent first:

{feedback_summary}

In 2-3 short sentences, identify any recurring pattern or repeated mistake across these sessions, and give one focused thing to work on this week. If there's no clear pattern, say they're progressing well and encourage them to keep practicing varied topics. Be specific and encouraging, not generic."""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text.strip()