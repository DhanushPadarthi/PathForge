from groq import Groq
from app.config.settings import settings

# Groq client (singleton)
groq_client = Groq(
    api_key=settings.GROQ_API_KEY
)
