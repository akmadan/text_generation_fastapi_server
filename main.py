from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()


model  = pipeline("text-generation", model  = "gpt2")


class TextGenerationRequest(BaseModel):
    prompt: str
    max_length: int = 1000

@app.post("/generate_text")
async def generate_text(request: TextGenerationRequest):
    try:
        result = model(request.prompt, max_length = request.max_length)
        return {"text": result[0]['generated_text']}
    except Exception as e:
        return {"error": str(e)}
    
        

@app.get("/")
async def root():
    return {"message": "Hello World"}