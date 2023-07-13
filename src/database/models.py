from pydantic import BaseModel, EmailStr
from typing import Optional, List
from beanie import Document, Indexed, PydanticObjectId


class UserModel(BaseModel):
    name: str
    email: EmailStr
    phone_number: str | None


class MessageModel(BaseModel):
    message_title: str
    message_text: str
    send_from_user_name: str
    send_to_user_name: str


class Message(Document):
    message_title: str
    message_text: str
    send_from_user_name: Indexed(str) # TODO change to PydanticObjectId of user
    send_to_user_name: Indexed(str) # TODO change to PydanticObjectId of user

    class Settings:
        name = "messages"


class User(Document): #TODO Add password login, hash, and authentication w JWT

    name: str
    email: EmailStr
    phone_number: str | None
    # Messages send by this user
    messages_ids: List[Message] | None
    class Config:
        name = "users"
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "JohnBoe",
                "email": "johnboe@gmail.com",
                "phone_number": "999999999",
                "messages_ids": None
            }
        }

