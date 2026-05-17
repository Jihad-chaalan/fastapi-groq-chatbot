from fastapi import FastAPI, HTTPException
from app.models import ChatRequest, ChatResponse
from app.groq_client import call_groq

app = FastAPI(title="Groq Chatbot API")



@app.get("/health")
async def healthc_check():
    return{
        "status":"ok"
    }

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        return call_groq(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))