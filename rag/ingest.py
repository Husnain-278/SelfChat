from .loaders import load_pdf
from .splitter import split_documents
from .vectorstore import create_vector_store

def ingest_pdf(document):
    docs = load_pdf(document.file.path)
    chunks = split_documents(docs)
    
    create_vector_store(
        chunks,
        collection_name=f"document_{document.id}",
    )