#!/bin/sh
# entrypoint.sh

# Start Ollama in the background
ollama serve & sleep 5 && ollama run deepseek-r1:1.5b

# Run the Streamlit app
streamlit run src/chat/app.py