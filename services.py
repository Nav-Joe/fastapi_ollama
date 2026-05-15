import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
#OLLAMA_URL = "http://host.docker.internal:11434"
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

app = FastAPI()

def ask_local_model(message: str) -> str:
    response = requests.post(
        f"{OLLAMA_HOST}/api/generate",
        json={"model": "qwen2.5:3b", "prompt": message, "stream": False}
    )
    return response.json()["response"]

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        # 改用本地模型
        reply = ask_local_model(req.message)
        return {"reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
