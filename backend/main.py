from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import datetime

from routers import chat, reporting

app = FastAPI(title="ShopNow AI Voice Agent API")

# Setup CORS for Frontend React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(reporting.router, prefix="/api/dashboard", tags=["dashboard"])

@app.get("/")
def read_root():
    return {"status": "Backend Operating normally"}

@app.get("/api/health")
def health_check():
    return {"status": "ok", "timestamp": datetime.datetime.now().isoformat()}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
