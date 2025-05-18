import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import SupabaseVectorStore
from supabase.client import create_client
from config import settings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
supabase = create_client(settings.supabase_url, settings.supabase_key)
vector_store = SupabaseVectorStore(
    client=supabase,
    embedding=embeddings,
    table_name="documents",
    query_name="match_documents_langchain",
)

def retrieve(query: str) -> str:
    results = vector_store.similarity_search(query)
    if results:
        return results[0].page_content
    else:
        return "No similar questions found."
