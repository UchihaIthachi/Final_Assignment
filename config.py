import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    provider = os.getenv("LLM_PROVIDER", "groq")
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_SERVICE_KEY")
    # Add other settings

settings = Settings()
