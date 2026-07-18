from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from gra_agent import GeniusAgent
from config import S_CRIT

app = FastAPI(title="GRA-Genius-Agent API", version="1.0")

# CORS to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files for frontend
app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")

# Initialize agent (singleton)
agent = GeniusAgent()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    s_value: float = None
    e_value: float = None
    i_value: float = None

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Empty message")
    # Get response and the selected state details
    selected = agent.select_best_response(agent.generate_candidates(request.message))
    if selected:
        response_text = selected.get("text", "No text")
        # Store in history
        agent.history.append({"user": request.message, "agent": response_text})
        return ChatResponse(
            response=response_text,
            s_value=selected.get("S"),
            e_value=selected.get("E"),
            i_value=selected.get("I")
        )
    else:
        return ChatResponse(response="No suitable response found.")

@app.get("/api/history")
async def history():
    return agent.get_history()

@app.get("/api/config")
async def config():
    return {"s_crit": S_CRIT}

# For running directly: uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
