from dataclasses import dataclass
from typing import Any

@dataclass
class RunConfig:
    model: Any = None
    model_provider: Any = None
    tracing_disabled: bool = True
