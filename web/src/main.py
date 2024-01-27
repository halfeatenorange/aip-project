from typing import List
import gradio as gr
from utils import generate_response

DEFAULT_SYSTEM_PROMPT = "Respond to the user's questions below"

def get_chatbot_response(message: str, history: List[List]):
    response_text = ""
    for token in generate_response(
        system_prompt=DEFAULT_SYSTEM_PROMPT,
        user_input=message,
        history=history,
        max_history=3,
        max_new_tokens=256
    ):
        response_text += token
        yield response_text

if __name__ == "__main__":
    chatbot = gr.ChatInterface(get_chatbot_response).queue()
    chatbot.launch(share=False, debug=True, server_name="0.0.0.0", server_port=7860)