from flask import Flask, render_template, jsonify, request
import sys
sys.path.append("../src")
from src import download_huggingface_embedding
from langchain import PromptTemplate
from langchain_pinecone import PineconeVectorStore
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
import os

app = Flask(__name__)
key = input("Enter Pinecone Api key: ")
os.environ['PINECONE_API_KEY'] = key
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_INDEX_NAME = "medical-chatbot"

embeddings = download_huggingface_embedding()

index_name="medical-bot"

#Loading the index
docsearch = PineconeVectorStore.from_existing_index(PINECONE_INDEX_NAME,embeddings)

prompt_template = """
Use the given information context to give appropriate answer for the user's question.
If you don't know the answer, just say that you know the answer, but don't make up an answer.
Context: {context}
Question: {question}
Only return the appropriate answer and nothing else.
Helpful answer:
"""

PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])

chain_type_kwargs={"prompt": PROMPT}

config = {'max_new_tokens': 512, 'temperature': 0.8}
llm = CTransformers(model='TheBloke/Llama-2-7B-Chat-GGML',\
                    model_file='llama-2-7b-chat.ggmlv3.q4_0.bin',model_type='llama' ,config=config)


qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)



@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa.invoke(input)
    print("Response : ", result["result"])
    return str(result["result"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)

