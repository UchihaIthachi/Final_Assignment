# retrievers/custom_retriever.py

import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import SupabaseVectorStore
from supabase.client import create_client
from config import settings

def get_vector_store():
    # Read env variables only when needed
    supabase_url = settings.supabase_url
    supabase_key = settings.supabase_key

    if not supabase_url or not supabase_key:
        raise ValueError("SUPABASE_URL and SUPABASE_SERVICE_KEY must be set in your environment or .env file.")
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    supabase = create_client(supabase_url, supabase_key)
    return SupabaseVectorStore(
        client=supabase,
        embedding=embeddings,
        table_name="documents",
        query_name="match_documents_langchain",
    )

def retrieve(query: str) -> str:
    try:
        vector_store = get_vector_store()
        results = vector_store.similarity_search(query)
        if results:
            return results[0].page_content
    except Exception as e:
        return f"Retriever is not available (reason: {e})"
    return "No similar questions found."

