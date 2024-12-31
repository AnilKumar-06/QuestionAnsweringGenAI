import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
#from langchain.chat_models import ChatOpenAI
#from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
#from langchain_community import chat_models
from dotenv import load_dotenv
load_dotenv()
import os

# import getpass

# if not os.environ.get("OPENAI_API_KEY"):
#     os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

api_key = os.getenv("OPEN_API_KEY")
#chat = ChatOpenAI(openai_api_key=api_key, temperature=0.5)
chat = ChatOpenAI(
    model="gpt-3.5-turbo-0125",
    temperature=0,
    max_tokens=20,
    timeout=None,
    max_retries=2,
    api_key=api_key,  # if you prefer to pass api key in directly instaed of using env vars
    # base_url="...",
    # organization="...",
    # other params...
)
st.set_page_config(page_title="My ChatBot")
st.header("I am your chatbot, Ask me Anything?")

if 'mymessages' not in st.session_state:
    st.session_state['mymessages']=[
        SystemMessage(content="You are Anil Kumar chatbot and your work is answer my question")
    ]


def chatmodel_response(ques):
    st.session_state['mymessages'].append(HumanMessage(content=ques))
    response = chat.invoke(st.session_state['mymessages'])
    st.session_state['mymessages'].append(AIMessage(content=response.content))
    return response.content


input = st.text_input("input: ", key="input")
response = chatmodel_response(input)
submit_button = st.button("Ask Question?")

if submit_button:
    st.subheader("This is your Response: ")
    st.write(response)