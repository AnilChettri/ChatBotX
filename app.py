import streamlit as st
from chatbot import get_bot_response

def main():
    st.title("ChatBotX")

    # User input section
    user_input = st.text_input("You: ", "")

    if user_input:
        response = get_bot_response(user_input)
        st.write(f"Bot: {response}")

if __name__ == "__main__":
    main()
