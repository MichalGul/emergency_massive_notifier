from fastapi import APIRouter, HTTPException
from src.database.models import MessageModel, Message

router = APIRouter(prefix="/api/message")

@router.post('/create_message', response_model=MessageModel, response_description="Message Created")
async def create_message(message: Message):
    await message.create()
    return MessageModel(message_title=message.message_title,
                         message_text=message.message_text,
                         send_from_user_name=message.send_from_user_name,
                         send_to_user_name=message.send_to_user_name)
