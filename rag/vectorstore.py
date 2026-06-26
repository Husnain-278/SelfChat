from langchain_chroma import Chroma
from django.conf import settings
from .embeddings import embeddings 
from chromadb import PersistentClient



def create_vector_store(chunks, collection_name):
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(settings.CHROMA_DB_DIR),
        collection_name=collection_name
    )
    


def delete_collection(collection_name):

    client = PersistentClient(
        path=str(settings.CHROMA_DB_DIR)
    )

    try:
        client.delete_collection(collection_name)
    except Exception:
        pass
    
    


def load_vector_store(collection_name: str):
    return Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
        persist_directory=str(settings.CHROMA_DB_DIR)
    )
    