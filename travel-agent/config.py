# config.py
import os
from dotenv import load_dotenv, find_dotenv
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel

# Load .env
load_dotenv(find_dotenv())

# Get API key from env
api_key = os.getenv("OPENROUTER_API_KEY")

# Check API key
if not api_key:
    raise ValueError("OPENROUTER_API_KEY is not set. Please ensure it is defined in your .env file.")

# ✅ Correct OpenRouter Client
external_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"  # ✅ OpenRouter base URL
)

# ✅ Model name (OpenRouter supports many models — you can change here)
# Common free option: "openai/gpt-4o-mini"
model_name = "openai/gpt-4o-mini"  

# Travel Configuration
DEFAULT_BUDGET = 1000
DEFAULT_TRIP_DURATION = 7  # days
MAX_TRAVELERS = 4
DEFAULT_DEPARTURE_CITY = "New York"
DEFAULT_DESTINATION_CITY = "Paris"

# Agent Configuration
AGENT_TEMPERATURE = 0.7
AGENT_MAX_TOKENS = 2000

# Travel Preferences
DEFAULT_ACCOMMODATION_TYPE = "hotel"
DEFAULT_TRANSPORTATION_TYPE = "flight"
DEFAULT_ACTIVITY_PREFERENCES = ["sightseeing", "food", "culture"]

# API Configuration
FLIGHT_API_ENDPOINT = "https://api.example.com/flights"
HOTEL_API_ENDPOINT = "https://api.example.com/hotels"
WEATHER_API_ENDPOINT = "https://api.example.com/weather"

# OpenRouter Configuration
OPENROUTER_API_KEY = api_key
DEFAULT_MODEL = model_name

# Create the actual model object
model = OpenAIChatCompletionsModel(
    model=DEFAULT_MODEL,
    openai_client=external_client
)
