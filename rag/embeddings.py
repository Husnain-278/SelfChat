from langchain_mistralai import MistralAIEmbeddings
from django.conf import settings

embeddings = MistralAIEmbeddings(
    api_key=settings.MISTRAL_API_KEY,
    model = 'mistral-embed'
)