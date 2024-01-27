from huggingface_hub import hf_hub_download
from llama_cpp import Llama

def download_model():
    model_name = "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF"
    model_file = "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf" 
    model_path = hf_hub_download(model_name, filename=model_file, cache_dir="/app/models")
    return model_path

def load_llm():
    model_path = download_model()
    llm = Llama(
        model_path=model_path,
        n_gpu_layers=0,
        seed=0
    )
    return llm