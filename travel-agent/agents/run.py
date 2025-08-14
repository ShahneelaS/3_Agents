from dataclasses import dataclass
from typing import Any

@dataclass
class RunConfig:
    model: Any = None
    model_provider: Any = None
    tracing_disabled: bool = True
    temperature: float = 0.7  # Default temperature
    max_tokens: int = 512     # Default token limit
