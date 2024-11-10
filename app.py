import google.generativeai as genai
import os
import streamlit as st


GOOGLE_API_KEY='AIzaSyBlt4K4Bxi6mLjNpEjMWgTvBKTTyey_ALU'
genai.configure(api_key=GOOGLE_API_KEY)
models=genai.GenerativeModel('gemini-pro')

chat = models.start_chat(history=[])

def get_gemini_response(input):
    resp = models.generate_content(input)
    return resp


st.set_page_config(page_title="--Q&A Project--", page_icon="🌌", layout="wide")
st.header(" **Gemini End to End Project ** ")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [] # Initialize chat history

input = st.text_input("Input: ",key = "input")
submit = st.button("Ask the bot")

if submit and input:
    response = get_gemini_response(input)
    st.session_state['chat_history'].append(("You: ",input))
    st.subheader("The response is ")
    full_resp=""
    for chunk in response:
        full_resp+=chunk.text
    st.session_state['chat_history'].append(("Bot: " ,full_resp))
    st.write(full_resp)


st.subheader("Chat History")
for role,session in st.session_state['chat_history']:
    st.write(f"{role}: {session}")  # Display chat history