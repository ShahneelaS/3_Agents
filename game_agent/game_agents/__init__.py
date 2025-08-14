from openai import AsyncOpenAI  # ✅ OpenAI client
from .function_tool import function_tool

from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import Any, Callable, Generic, TypeVar, List, Optional

T = TypeVar("T")

# ---------------- Core Agent Classes ----------------

@dataclass
class Agent:
    name: str
    instructions: str
    tools: list = field(default_factory=list)
    model: Any = None
    handoffs: list = field(default_factory=list)

@dataclass
class OpenAIChatCompletionsModel:
    model: str
    openai_client: Any = None

@dataclass
class RunConfig:
    model: Any = None
    model_provider: Any = None
    tracing_disabled: bool = True

@dataclass
class RunContextWrapper(Generic[T]):
    value: Optional[T] = None
    metadata: dict = field(default_factory=dict)

def handoff(agent: Agent, on_handoff: Optional[Callable] = None):
    return SimpleNamespace(agent=agent, on_handoff=on_handoff)

class Runner:
    async def run(self, agent: Agent, input_list: List[dict], run_config: RunConfig):
        user_msgs = [m for m in input_list if m.get("role") == "user"]
        last = user_msgs[-1]["content"] if user_msgs else ""
        model = run_config.model
        client = getattr(model, "openai_client", None)

        if client is not None:
            try:
                msgs = [{"role": m.get("role", "user"), "content": m.get("content", "")} for m in input_list]
                if hasattr(client, "chat") and hasattr(client.chat, "completions"):
                    resp = await client.chat.completions.create(
                        model=model.model if hasattr(model, 'model') else model,
                        messages=msgs
                    )
                    try:
                        content = resp.choices[0].message.content
                    except Exception:
                        content = str(resp)
                else:
                    content = f"(AI response simulated) I understood: {last}"
            except Exception as e:
                content = f"(AI request failed) {e}"
        else:
            content = f"(Simulated response) I understood: {last}"

        return SimpleNamespace(
            final_output=content,
            to_input_list=lambda: input_list + [{"role": "assistant", "content": content}]
        )

# ---------------- Game Specific Agents (No classes, just variables) ----------------

from .game_narrator_agent import narrator_agent as NarratorAgent
from .enemy_monster_agent import monster_agent as MonsterAgent
from .game_item_agent import item_agent as ItemAgent
