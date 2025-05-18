from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from config import settings

def get_llm(provider: str):
    if provider == "google":
        return ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
    elif provider == "groq":
        return ChatGroq(model="qwen-qwq-32b", temperature=0)
    elif provider == "huggingface":
        return ChatHuggingFace(
            llm=HuggingFaceEndpoint(
                url="https://api-inference.huggingface.co/models/Meta-DeepLearning/llama-2-7b-chat-hf",
                temperature=0,
            ),
        )
    else:
        raise ValueError(f"Unknown provider: {provider}")
