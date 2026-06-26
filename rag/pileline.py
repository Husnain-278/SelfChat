from .retriever import retrieve
from .llm import llm
from .prompts import RAG_PROMPT


def answer_question(document_id,    question):
    docs = retrieve(document_id, question)
    
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )
    
    prompt = RAG_PROMPT.format(
        context = context,
        question= question,
    )
    
    response = llm.invoke(prompt)
    return response.content