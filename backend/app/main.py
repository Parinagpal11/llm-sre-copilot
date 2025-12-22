from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

class ChatReq(BaseModel):
    message: str
    session_id: str | None = None

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/chat")
def chat(req: ChatReq):
    # TEMP stub: replace with Gemini call next step
    return {
        "reply": f"Echo: {req.message}",
        "meta": {
            "session_id": req.session_id or "demo",
            "model": os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
        }
    }
