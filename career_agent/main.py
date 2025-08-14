import chainlit as cl
from agents import Runner
from agents.career_guidance_agent import career_agent
from agents.skill_development_agent import skill_agent
from agents.job_search_agent import job_agent
from config import openai_config  # OpenRouter-ready RunConfig

# Router function to pick the right agent based on keywords
async def choose_agent(message_content: str):
    msg = message_content.lower()
    if "skill" in msg or "learn" in msg or "improve" in msg:
        return skill_agent
    elif "job" in msg or "hire" in msg or "vacancy" in msg or "career opportunity" in msg:
        return job_agent
    else:
        return career_agent  # default agent

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])
    await cl.Message(
        "🎓 Hey there! Let us discover the right path for you. What subjects or hobbies do you enjoy?"
    ).send()

@cl.on_message
async def handle(msg: cl.Message):
    history = cl.user_session.get("history", [])
    history.append({"role": "user", "content": msg.content})

    thinking = cl.Message("💡 Thinking...")
    await thinking.send()

    try:
        # Choose the appropriate agent
        agent_to_use = await choose_agent(msg.content)

        runner = Runner()

        # ✅ Use OpenRouter-ready RunConfig from config.py
        result = await runner.run(
            agent=agent_to_use,
            input_list=history,
            run_config=openai_config
        )

        output = result.final_output

        thinking.content = output
        await thinking.update()

        # Update history
        history = result.to_input_list()
        cl.user_session.set("history", history)

    except Exception as e:
        thinking.content = f"❌ Error: {e}"
        await thinking.update()
