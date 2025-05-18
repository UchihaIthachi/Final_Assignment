from langchain_core.tools import tool
from langchain_community.document_loaders import WikipediaLoader, ArxivLoader
from langchain_community.tools.tavily_search import TavilySearchResults

@tool
def wiki_search(query: str) -> dict:
    """Search Wikipedia for a query and return maximum 2 results."""
    search_docs = WikipediaLoader(query=query, load_max_docs=2).load()
    formatted = "\n\n---\n\n".join(
        f'<Document source="{doc.metadata["source"]}" page="{doc.metadata.get("page", "")}"/>\n{doc.page_content}\n</Document>'
        for doc in search_docs
    )
    return {"wiki_results": formatted}

@tool
def web_search(query: str) -> dict:
    """Search Tavily for a query and return maximum 3 results."""
    search_docs = TavilySearchResults(max_results=3).invoke(query=query)
    formatted = "\n\n---\n\n".join(
        f'<Document source="{doc.metadata["source"]}" page="{doc.metadata.get("page", "")}"/>\n{doc.page_content}\n</Document>'
        for doc in search_docs
    )
    return {"web_results": formatted}

@tool
def arxiv_search(query: str) -> dict:
    """Search Arxiv for a query and return maximum 3 results."""
    search_docs = ArxivLoader(query=query, load_max_docs=3).load()
    formatted = "\n\n---\n\n".join(
        f'<Document source="{doc.metadata["source"]}" page="{doc.metadata.get("page", "")}"/>\n{doc.page_content[:1000]}\n</Document>'
        for doc in search_docs
    )
    return {"arxiv_results": formatted}
