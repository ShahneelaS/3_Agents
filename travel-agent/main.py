import os
import chainlit as cl
from dotenv import load_dotenv
from agents import Runner
from agents.destination_planning_agent import destination_agent
from agents.travel_exploration_agent import explore_agent
from agents.travel_booking_agent import booking_agent
from agents.run import RunConfig
from config import model  # ✅ yahan se model import kiya

# Load environment
load_dotenv()

# Function to choose agent
async def choose_agent(message_content: str):
    msg = message_content.lower()
    if "book" in msg or "reservation" in msg or "ticket" in msg:
        return booking_agent
    elif "explore" in msg or "visit" in msg or "things to do" in msg:
        return explore_agent
    else:
        return destination_agent

@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("history", [])
    welcome_message = (
        "🌟 Hello! Welcome to your AI Travel Designer. "
        "Ready to discover your next adventure? "
        "Ask me anything about destinations, flights, or hotels! 🌍✈️"
    )
    await cl.Message(welcome_message).send()

@cl.on_message
async def on_message(message: cl.Message):
    session_history = cl.user_session.get("history") or []
    session_history.append({"role": "user", "content": message.content})

    loading_message = await cl.Message("🔎 Planning your perfect trip... Please wait!").send()

    try:
        agent_to_use = await choose_agent(message.content)

        # ✅ RunConfig with actual model object
        run_config = RunConfig(
            model=model,
            temperature=0.7
        )

        runner = Runner()

        agent_result = await runner.run(
            agent=agent_to_use,
            input_list=session_history,
            run_config=run_config
        )

        final_output = agent_result.final_output
        loading_message.content = final_output
        await loading_message.update()

        session_history = agent_result.to_input_list()
        cl.user_session.set("history", session_history)

    except Exception as error:
        loading_message.content = f"❌ Oops! Something went wrong: {error}"
        await loading_message.update()
