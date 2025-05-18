import os
from dotenv import load_dotenv

class Settings:
    llm_provider = os.getenv("LLM_PROVIDER", "groq")  # <- This line is critical!
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_SERVICE_KEY")
    # ... any other settings

settings = Settings()


settings = Settings()
