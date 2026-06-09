from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.agent import handle_user_message
from services.speech import detect_language

router = APIRouter()

class ChatRequest(BaseModel):
    session_id: str
    message: str

@router.post("/message")
async def process_chat_message(req: ChatRequest):
    """
    Endpoint for text-based chat or text that has already been transcribed.
    """
    try:
        response_data = handle_user_message(req.session_id, req.message)
        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
