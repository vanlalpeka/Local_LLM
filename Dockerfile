# Dockerfile
FROM python:3.12-slim

# Install necessary dependencies (e.g., curl)
RUN apt-get update && apt-get install -y curl

# Install Ollama (assuming Ollama installation script)
RUN curl -fsSL https://ollama.com/install.sh | sh

# Add Ollama to PATH
# ENV PATH="/root/.local/bin:$PATH"
RUN ollama serve & ollama pull deepseek-r1:1.5b

# Set the working directory in the container
WORKDIR /app

COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Give execute permission to the entrypoint script
RUN chmod +x entrypoint.sh

# Expose port 8501 (default Streamlit port) and 11434 (Ollama port)
EXPOSE 8501 11434

# Command to run the entrypoint script
CMD ["./entrypoint.sh"]