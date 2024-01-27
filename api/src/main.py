
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from utils import load_llm
from generation_inputs import GenerationInputs

LLM = load_llm()

app = FastAPI()

@app.get("/health")
async def healthcheck():
    return {"status": "healthy"}

@app.post("/generate")
async def generate(inputs: GenerationInputs):
    inputs.stream = False
    response = LLM.create_completion(**dict(inputs))
    return response["choices"][0]["text"]
    
@app.post('/generate_stream')
async def generate_stream(inputs: GenerationInputs):
    inputs.stream = True

    async def stream_outputs(inputs: GenerationInputs):
        stream = LLM.create_completion(**dict(inputs))
        for output in stream:
            yield output['choices'][0]['text']

    return StreamingResponse(stream_outputs(inputs), media_type='text/event-stream')
 