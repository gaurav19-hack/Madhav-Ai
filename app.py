import streamlit as st
import openai
import os

# Set your OpenAI key
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🧠 Madhav AI - Mental Health Companion")
st.subheader("How are you feeling today?")

# Mood Check-in
mood = st.selectbox("Select your current mood:", ["🙂 Fine", "😟 Anxious", "😢 Sad", "😡 Angry", "😕 Confused"])

# Chat Input
user_input = st.text_input("Talk to Madhav AI:")

from openai import OpenAI

from openai import OpenAI
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"]
)


response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input},
    ]
)

# To get the output text:
output = response.choices[0].message.content


# Emergency Trigger
if "suicide" in user_input.lower() or "end my life" in user_input.lower():
    st.error("⚠️ It seems you're in distress. Here's help:")
    st.markdown("📞 [iCall Helpline](https://icallhelpline.org/) - 9152987821  \n🧠 [AASRA Helpline](http://www.aasra.info/) - 91-22-27546669")

