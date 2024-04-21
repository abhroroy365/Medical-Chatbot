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