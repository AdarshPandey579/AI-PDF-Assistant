import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

MODEL = "llama-3.3-70b-versatile"
# MODEL = "openai/gpt-oss-20b"
# MODEL = "openai/gpt-oss-120b"