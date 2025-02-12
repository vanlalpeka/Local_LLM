# Local LLM with Streamlit UI
This container is based on ollama/ollama image to run LLM offline (local). The "stack" is deepseek-r1:1.5b -> langchain -> streamlit UI.
To update the LLM model, change the model name in the ChatOllama() call.
```
# /src/app.py
# Currently using deepseek-r1:1.5b.
# Update the model as prefered

response = ChatOllama(model="deepseek-r1:1.5b",....)
```

<a href="https://arxiv.org/html/2410.04343v1">IterDRAG</a> technique is used for RAG.

The "\</think>" tag is not printed on the Streamlit UI.

The prompt instructions are from <a href="https://github.com/langchain-ai/ollama-deep-researcher/tree/main">Langchain's Ollama Deep Researcher</a>.

# Usage (Docker):
Pull the image from Docker hub
```

```


# Usage (Linux/WSL): Clone this repo
Clone this repo, then run the following steps:
1. Install Ollama
```
curl -fsSL https://ollama.com/install.sh | sh
```

2. Install requirements
```
pip install -r requirements.txt
```

3. Run Ollama in the background
```
ollama serve & sleep 5 && ollama run deepseek-r1:1.5b
```

4. Run the streamlit app
```
streamlit run src/chat/app.py
```