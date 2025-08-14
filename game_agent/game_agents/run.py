from .game_base_agent import Agent
from .function_tool import OpenAIChatCompletionsModel

class RunConfig:
    def __init__(self, model=None, temperature=0.7):
        self.model = model
        self.temperature = temperature

class Runner:
    def __init__(self):
        pass

    async def run(self, agent: Agent, input_list: list, run_config: RunConfig):
        # Ye basic execution simulation hai
        result = await agent.run(input_list, run_config)
        return result
