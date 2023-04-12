from fastapi import APIRouter, HTTPException
from src.database.models import UserModel, User

router = APIRouter(prefix="/api/user")

@router.post('/create_user', response_model=UserModel, response_description="User Created")
async def create_user(user: UserModel):
    user_db = User(name=user.name, email=user.email, phone_number=user.phone_number)
    await user_db.create()
    return UserModel(name=user.name, email=user.email, phone_number=user.phone_number)
