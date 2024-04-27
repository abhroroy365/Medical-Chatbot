from langchain_pinecone import PineconeVectorStore
from helper import load_data, text_split, download_huggingface_embedding
import os

def main():
    ROOT_DIR = os.path.abspath('..')
    PINECONE_INDEX_NAME = "medical-chatbot"
    key = input("Enter Pinecone Api key: ")
    os.environ['PINECONE_API_KEY'] = key
    data_path = os.path.join(ROOT_DIR, 'Medical-Chatbot','data')
    data = load_data(data_path)
    text_chunks = text_split(data)
    embeddings = download_huggingface_embedding()
    vectorstore_from_docs = PineconeVectorStore.from_documents(
            text_chunks,
            index_name=PINECONE_INDEX_NAME,
            embedding=embeddings
        )
    
if __name__ == '__main__':
    main()