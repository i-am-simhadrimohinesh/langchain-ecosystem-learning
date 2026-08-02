from langchain_core.messages import HumanMessage,AIMessage
from backend import chatbot
import streamlit as st

if 'history' not in st.session_state:
    st.session_state['history'] = []

for message in st.session_state['history']:
    if isinstance(message,HumanMessage):
        with st.chat_message("user"):
            st.text(message.content)
    else : 
        with st.chat_message("ai"):
            st.text(message.content)
userInput = st.chat_input("Type your message")
if userInput:
    st.chat_message("user").text(userInput)
    res = chatbot.invoke({'prompt':userInput},config={
    "configurable": {
        "thread_id": "user-123"
    }})['result']
    st.chat_message("ai").text(res)
    st.session_state['history'].append(HumanMessage(content=userInput))
    st.session_state['history'].append(AIMessage(content=res))