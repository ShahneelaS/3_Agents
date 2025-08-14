from agents import Agent
from config import model  # OpenRouter compatible model
from tools.skill_roadmap_generator import get_career_roadmap  # Tool must use OpenRouter client

skill_agent = Agent(
    name="SkillAgent",
    instructions="""
You help users plan their skill journey for a specific career field.

Steps:
- Ask the user which career they want to pursue.
- Use the tool `get_career_roadmap()` to generate a beginner-to-advanced roadmap.
- Clearly present the skill roadmap in bullet or numbered format.
- Then ask if the user wants to explore job roles in this field. If yes, hand off to JobAgent.

Tone:
motivational, encouraging and helpful.
""",
    tools=[get_career_roadmap],  # ✅ Tool uses OpenRouter client internally
    model=model  # ✅ OpenRouter model from config.py
)
