
# Project Title

A Retrieval-Augmented Generation (RAG) based Medical Chatbot. With the base model as Llama2 from Meta, the Retrieval system uses a medical document as corpus to generate context-rich output.
 
##  Model and dataset
* Model: llama-2, Download from [hugging face](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)
* Embeddings from [hugging face](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
* Dataset: Gale Encyclopedia of Medicine Vol. 2 (N-S).pdf [Link](https://www.academia.edu/32752835/The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND_EDITION)


## Run Locally

Clone the project

```bash
  git clone https://github.com/abhroroy365/Medical-Chatbot
```

Go to the project directory

```bash
  cd Medical-Chatbot
```
Create virtual environment
```bash
  python -m venv env
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python app.py
```


## Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://www.linkedin.com/in/abhra-ray-chaudhuri-aba3081b5/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abhra-ray-chaudhuri-aba3081b5/)

## Screenshot
![Web App Ui](https://github.com/abhroroy365/Medical-Chatbot/blob/master/chatbot.JPG)

