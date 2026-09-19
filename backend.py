import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if "OPENAI_API_KEY" in st.secrets:
    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

def get_llm(model_choice):
    if model_choice == "GPT-5.4 regular (advanced reasoning)":
        return ChatOpenAI(
            model="gpt-5.4",
            temperature=0.2,
            api_key=OPENAI_API_KEY
        )
    else:
        return ChatOpenAI(
            model="gpt-5.4-mini",
            temperature=0.2,
            api_key=OPENAI_API_KEY
        )
