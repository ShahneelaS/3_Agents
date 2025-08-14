import os
from dotenv import load_dotenv, find_dotenv
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel, RunConfig

# Load .env
load_dotenv(find_dotenv())

# Get API key from .env
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in environment variables")

# Create AsyncOpenAI client for OpenRouter
external_client = AsyncOpenAI(
    api_key=api_key,  # ✅ pass API key explicitly here
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost:8000",  # change if hosted online
        "X-Title": "Career Agent App"
    }
)

# Model setup
model = OpenAIChatCompletionsModel(
    model="gpt-4o-mini",
    openai_client=external_client
)

openai_config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
