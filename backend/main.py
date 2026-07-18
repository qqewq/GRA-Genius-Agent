from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from gra_agent.agent import GeniusAgent
import os

app = FastAPI(title="GRA Genius Agent API")

# Разрешаем CORS для фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Инициализация агента
agent = GeniusAgent()

# Модель запроса
class Message(BaseModel):
    text: str

# Эндпоинт чата
@app.post("/api/chat")
async def chat(message: Message):
    try:
        response = agent.respond(message.text)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Эндпоинт для получения истории (опционально)
@app.get("/api/history")
async def history():
    return {"history": agent.history}

# Раздаём статические файлы фронтенда (если они лежат в ./frontend)
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
