from .vectorstore import load_vector_store

def retrieve(document_id: int, question: str, k: int = 4):
    collection_name = f"document_{document_id}"
    vectordb = load_vector_store(collection_name)
    return vectordb.max_marginal_relevance_search(
        question,
        k = k, 
        fetch_k=20,
        lambda_mult=0.5
    )


