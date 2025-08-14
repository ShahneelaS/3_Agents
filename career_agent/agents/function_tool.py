# career_agent/agents/function_tool.py
from functools import wraps
from typing import Callable, Any, Optional

def function_tool(func: Optional[Callable] = None, *, name: Optional[str] = None, description: Optional[str] = None):
    """
    Lightweight decorator to mimic a tool decorator.
    Usage:
      @function_tool
      async def mytool(...): ...
    or
      @function_tool(name='mytool')
      async def mytool(...): ...
    It just returns the function and attaches metadata (no external registration).
    """
    def _decorate(f: Callable):
        @wraps(f)
        async def _wrapped(*args, **kwargs):
            return await f(*args, **kwargs)
        # attach metadata so code that inspects it won't crash
        _wrapped._tool_name = name or f.__name__
        _wrapped._tool_description = description
        _wrapped._is_tool = True
        return _wrapped

    if func is None:
        return _decorate
    else:
        return _decorate(func)
