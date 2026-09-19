import streamlit as st
from backend import get_llm

st.set_page_config(page_title="McMaster EE Assistant", layout="wide")
st.title("⚡ McMaster EE Assistant")

# Model dropdown (always visible)
model_choice = st.sidebar.selectbox(
    "Model",
    ["GPT-5.4 mini (free)", "GPT-5.4 regular (advanced reasoning)"]
)

# Mode selector with icons
mode = st.sidebar.selectbox(
    "Mode",
    ["📘 Concept Tutor", "📝 Homework Helper", "🛠️ Code/PCB Debug", "🎯 Quiz Generator", "📚 Flashcards"]
)

# Chat input
user_input = st.chat_input("Ask about circuits, EM, code, or projects...")

if user_input:
    st.chat_message("user").markdown(user_input)

    llm = get_llm(model_choice)

    response = llm.invoke(
        f"You are a McMaster second-year EE tutor. Mode: {mode}. "
        f"Help with concept explanations, homework guidance, and project debugging.\n\n"
        f"Question: {user_input}"
    )

    st.chat_message("assistant").markdown(response.content)
