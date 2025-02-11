# app.py
# Uses Streamlit's chat interface (st.chat_message())
# Stores conversation history using session state


import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
import time

from state import SummaryState, SummaryStateInput, SummaryStateOutput
from prompts import query_writer_instructions, summarizer_instructions, reflection_instructions


def main():
    # st.title("Local App with LLM")
    # st.write("Welcome to the app with LLM integration!")

    # # Initialize the Ollama model
    # llm = ChatOllama(model="deepseek-r1:1.5b", temperature=0)

    # llm_json_mode = ChatOllama(model="deepseek-r1:1.5b", temperature=0, format='json')

    # # user_input = st.text_input("Enter something:")
    # # if user_input:
    # #     # response = llm(user_input)
    # #     response = llm.invoke(user_input)
    # #     st.write(f"LLM Response: {response}")

    # msg = llm.invoke('good morning')
    # st.write(f"LLM Response: {msg.content}")





    # Set up the Streamlit app
    st.set_page_config(page_title="Chatbot", layout="wide")

    st.title("💬 AI Chatbot with Streamlit")


    # Initialize session state for messages
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I help you today?"}]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    user_input = st.chat_input("Type your message...")

    if user_input:
        # Add user message to session
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Display user message
        with st.chat_message("user"):
            st.markdown(user_input)

        # Call OpenAI API
        try:
            response = ChatOllama(model="deepseek-r1:1.5b", 
                                  temperature=1.3, 
                                #   format='json'
                                  )            

            # thinking_msg = st.empty()
    
            # # Animated dots for "Thinking..."
            # for _ in range(3):
            #     thinking_msg.markdown("🤖 Thinking.")
            #     time.sleep(0.5)
            #     thinking_msg.markdown("🤖 Thinking..")
            #     time.sleep(0.5)
            #     thinking_msg.markdown("🤖 Thinking...")
            #     time.sleep(0.5)

            assistant_reply = response.invoke([
                SystemMessage(content=summarizer_instructions),
                HumanMessage(content=user_input)
                ])   
            
            print(assistant_reply.content)
            
            # Display assistant response
            with st.chat_message("assistant"):

                running_summary = assistant_reply.content

                # This is a hack to remove the <think> tags w/ Deepseek models 
                while "<think>" in running_summary and "</think>" in running_summary:
                    start = running_summary.find("<think>")
                    end = running_summary.find("</think>") + len("</think>")
                    running_summary = running_summary[:start] + running_summary[end:]

                st.markdown(running_summary)

            # Store assistant message
            st.session_state.messages.append({"role": "assistant", "content": running_summary})
        
        except Exception as e:
            st.error(f"Error: {e}")



if __name__ == "__main__":
    main()