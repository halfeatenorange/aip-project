from typing import Optional, List
from pydantic import BaseModel

class GenerationInputs(BaseModel):
    prompt: str
    max_tokens: int = 256
    temperature: float = 0.8 
    top_p: float = 0.95
    min_p: float = 0.05
    echo: bool = False
    stop: List[str] = ["</s>", "\n", "Q:", "A:"]
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0
    repeat_penalty: float = 1.1
    top_k: int = 40
    stream: bool = False
    seed: Optional[int] = 0