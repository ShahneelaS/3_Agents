import os
from dotenv import load_dotenv, find_dotenv
from agents.function_tool import function_tool
from openai import AsyncOpenAI

# Load environment variables
load_dotenv(find_dotenv())

# ✅ OpenRouter API key
api_key = os.getenv("OPENROUTER_API_KEY")

# ✅ OpenRouter client
client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"  # ✅ OpenRouter endpoint
)

@function_tool
async def get_career_roadmap(input: dict):
    try:
        prompt = (
            f"I'm interested in becoming a {input['career_field']}.\n"
            "Please provide a step-by-step skill roadmap that includes beginner, intermediate, and advanced level skills.\n"
            "Format the response clearly using bullet points or numbered steps."
        )

        response = await client.chat.completions.create(
            model="openai/gpt-4o-mini",  # ✅ OpenRouter model
            messages=[{"role": "user", "content": prompt}]
        )

        output = response.choices[0].message["content"]

        return {
            "skill_roadmap": output.strip()
        }

    except Exception as e:
        print("❌ Exception in get_career_roadmap tool:", str(e))
        return {
            "error": f"❌ Exception in get_career_roadmap tool: {str(e)}"
        }
