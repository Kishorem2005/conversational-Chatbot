import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_openai import ChatOpenAI

st.set_page_config(page_title="Converational Chatbot", page_icon=":earth_americas:")

st.header("Hey, Lets Chat!")

load_dotenv()

chat = ChatOpenAI(temperature=0.5)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="Hello, I am a chatbot. I am here to help you with your queries. Please ask me anything!")
    ]

def get_openai_response(query):
    st.session_state['flowmessages'].append(HumanMessage(content=query))
    answer = chat.invoke(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))

    return answer.content

input_text = st.text_input("Input: ", key="input")
submit = st.button("Submit")

if submit and input_text:
    response = get_openai_response(input_text)
    st.write(response)
