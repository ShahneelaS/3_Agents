import os
from dotenv import load_dotenv, find_dotenv
from agents import function_tool, RunContextWrapper, AsyncOpenAI

# Load environment variables
load_dotenv(find_dotenv())

api_key = os.getenv("OPENROUTER_API_KEY")

# OpenRouter client
client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

@function_tool
async def get_flights(input):
    try:
        prompt = (
            f"Find flights from {input['origin']} to {input['destination']} on {input['date']}.\n"
            "Provide flight options with airline, departure time, arrival time, and price.\n"
            "Format the response clearly with bullet points."
        )

        response = await client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        output = response.choices[0].message.content

        return {
            "flight_options": output.strip()
        }

    except Exception as e:
        print("❌ Exception in get_flights tool:", str(e))
        return {
            "error": f"❌ Exception in get_flights tool: {str(e)}"
        }
