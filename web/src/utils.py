import os
from typing import List
import requests

ENDPOINT = os.getenv("LLM_ENDPOINT", "http://api:80/generate_stream")

def format_prompt(
        system_prompt: str, 
        user_input: str, 
        history: List[List[str]], 
        max_history: int = 3
    ):
    prompt_components = [
        "<|system|>", system_prompt+"</s>"
    ]
    for user, assistant in history[-max_history:]:
        prompt_components.extend([
            "<|user|>", user+"</s>"
        ])
        prompt_components.extend([
            "<|assistant|>", assistant+"</s>"
        ])
    prompt_components.extend([
        "<|user|>", user_input+"</s>", "<|assistant|>"
    ])
    formatted_prompt = """
{}
""".format("\n".join(prompt_components))
    return formatted_prompt

def generate_response(
        system_prompt: str, 
        user_input: str, 
        history: List[List[str]], 
        max_history: int = 3,
        max_new_tokens: int = 64
    ):
        prompt = format_prompt(system_prompt, user_input, history, max_history)
        query = {
            "prompt": prompt,
            "max_tokens": max_new_tokens
        }
        with requests.post(ENDPOINT, json=query, stream=True) as response:
            for chunk in response.iter_content(1024):
                yield chunk.decode('utf8')