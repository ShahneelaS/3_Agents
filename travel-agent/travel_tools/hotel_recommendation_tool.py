import os
from dotenv import load_dotenv, find_dotenv
from agents import function_tool, RunContextWrapper, AsyncOpenAI

load_dotenv(find_dotenv())

# OpenRouter API key environment variable
api_key = os.getenv("OPENROUTER_API_KEY")

# OpenRouter client setup
client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"  # ✅ OpenRouter endpoint
)

@function_tool
async def suggest_hotels(input: dict):
    try:
        prompt = (
            f"Suggest hotels in {input['location']} for {input['dates']}.\n"
            f"Budget: {input['budget']}\n"
            f"Preferences: {input['preferences']}\n"
            "Provide hotel options with name, rating, price range, and key amenities.\n"
            "Format the response clearly with bullet points."
        )
        
        response = await client.chat.completions.create(
            model="openai/gpt-4o-mini",  # ✅ OpenRouter model format
            messages=[{"role": "user", "content": prompt}]
        )
        
        output = response.choices[0].message["content"]
        
        return {
            "hotel_suggestions": output.strip()
        }
        
    except Exception as e:
        print("❌ Exception in suggest_hotels tool:", str(e))
        return {
            "error": f"❌ Exception in suggest_hotels tool: {str(e)}"
        }
