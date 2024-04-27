from langchain import PromptTemplate
from langchain_pinecone import PineconeVectorStore
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.vecteorstores import Pinecone 
from pinecone import Pinecone,ServerlessSpec
from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
import os
from tqdm.autonotebook import tqdm
import sys

def load_data(data_path):
    loader = DirectoryLoader(data_path,glob='*.pdf',loader_cls=PyPDFLoader)
    data = loader.load()
    return data

def text_split(data):
    splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap= 20)
    text_chunks = splitter.split_documents(data)
    return text_chunks

def download_huggingface_embedding():
    embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
    return embeddings