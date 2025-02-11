# Local LLM with Streamlit UI
This container runs LLM offline (local). The "stack" is deepseek-r1:1.5b -> langchain -> streamlit UI.

<a href="https://arxiv.org/html/2410.04343v1">IterDRAG</a> technique is used for RAG.

The "\</think>" tag is printed to sys.stdout but it is not printed on the Streamlit UI.

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