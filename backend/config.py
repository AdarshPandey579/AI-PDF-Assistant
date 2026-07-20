import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("OPENROUTER_API_KEY"),
#     base_url="https://openrouter.ai/api/v1"
# )
# MODEL = "nvidia/nemotron-3-ultra-550b-a55b:free"


# client = OpenAI(
#     api_key=os.getenv("GEMINI_API_KEY"),
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )
# MODEL = "gemini-2.5-flash"
# MODEL = "gemini-2.5-pro"


client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)
MODEL = "llama-3.3-70b-versatile"
# MODEL = "openai/gpt-oss-20b"
# MODEL = "openai/gpt-oss-120b"