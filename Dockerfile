# Dockerfile
FROM ollama/ollama

# Set the working directory in the container
WORKDIR /app

COPY . .

RUN apt update 
RUN apt-get install -y python3 python3-pip nano git 

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Give execute permission to the entrypoint script
RUN chmod +x entrypoint.sh

# Expose port 8501 (default Streamlit port) and 11434 (Ollama port)
EXPOSE 8501 
EXPOSE 11434

# HEALTHCHECK instruction tells Docker how to test a container to check that it is still working
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Command to run the entrypoint script
ENTRYPOINT  ["./entrypoint.sh"]