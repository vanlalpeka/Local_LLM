#!/bin/sh
# entrypoint.sh

# Start Ollama in the background
# ollama serve & ollama run deepseek-r1:1.5b

# Wait for Ollama to start up
sleep 5

# Run the Streamlit app
streamlit run src/chat/app.py