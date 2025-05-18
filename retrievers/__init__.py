from .custom_retriever import retrieve

class CustomRetriever:
    @staticmethod
    def retrieve(query):
        return retrieve(query)

custom_retriever = CustomRetriever()
