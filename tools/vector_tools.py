from langchain_core.tools import tool
# Example vector tool using retriever
from retrievers import custom_retriever

@tool
def similar_question(query: str) -> str:
    """Retrieve a similar question from the vector store."""
    return custom_retriever.retrieve(query)
