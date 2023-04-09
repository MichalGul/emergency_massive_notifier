from mongoengine import Document, StringField, EmailField, IntField, FloatField, ListField, ObjectIdField
from pydantic import BaseModel, EmailStr




class UserModel(BaseModel):
    name: str
    email: EmailStr
    phone_number: str | None


class User(Document):
    name = StringField(required=True, max_length=50)
    email = EmailField(required=True, max_length=50)
    phone_number = StringField(max_length=15)
    # Messages send by this user
    messages_ids = ListField(ObjectIdField())
    # more to add

    meta = {
        'db_alias': 'core',
        'collection': 'users'
    }

class Message(Document):
    message_title = StringField(required=True, max_length=50)
    message_text = StringField(required=True, max_length=300)
    send_to_user_id = ObjectIdField()

    meta = {
        'db_alias': 'core',
        'collection': 'messages'
    }