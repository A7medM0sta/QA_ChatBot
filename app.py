# ## Conversational Q&A Chatbot
# import streamlit as st
#
# from langchain.schema import HumanMessage,SystemMessage,AIMessage
# from langchain.chat_models import ChatOpenAI
#
# ## Streamlit UI
# st.set_page_config(page_title="Conversational Q&A Chatbot")
# st.header("Hey, Let's Chat")
#
# from dotenv import load_dotenv
# load_dotenv()
# import os
#
# chat=ChatOpenAI(temperature=0.5)
#
# if 'flowmessages' not in st.session_state:
#     st.session_state['flowmessages']=[
#         SystemMessage(content="Yor are a comedian AI assitant")
#     ]
#
# ## Function to load OpenAI model and get respones
#
# def get_chatmodel_response(question):
#
#     st.session_state['flowmessages'].append(HumanMessage(content=question))
#     answer=chat(st.session_state['flowmessages'])
#     st.session_state['flowmessages'].append(AIMessage(content=answer.content))
#     return answer.content
#
# input=st.text_input("Input: ",key="input")
# response=get_chatmodel_response(input)
#
# submit=st.button("Ask the question")
#
# ## If ask button is clicked
#
# if submit:
#     st.subheader("The Response is")
#     st.write(response)

import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

class ChatBotUI:
    def __init__(self):
        load_dotenv()
        self.chat = ChatOpenAI(temperature=0.5)
        st.set_page_config(page_title="Conversational Q&A Chatbot")
        st.header("Hey, Let's Chat")
        self.initialize_session_state()

    def initialize_session_state(self):
        if 'flowmessages' not in st.session_state:
            st.session_state['flowmessages'] = [
                SystemMessage(content="You are a comedian AI assistant")
            ]

    def get_chatmodel_response(self, question):
        st.session_state['flowmessages'].append(HumanMessage(content=question))
        answer = self.chat(st.session_state['flowmessages'])
        st.session_state['flowmessages'].append(AIMessage(content=answer.content))
        return answer.content

    def display_ui(self):
        user_input = st.text_input("Input: ", key="input")
        submit = st.button("Ask the question")
        if submit:
            response = self.get_chatmodel_response(user_input)
            st.subheader("The Response is")
            st.write(response)

if __name__ == "__main__":
    chat_bot_ui = ChatBotUI()
    chat_bot_ui.display_ui()
