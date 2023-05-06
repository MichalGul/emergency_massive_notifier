from fastapi import APIRouter, HTTPException
from src.database.models import UserModel, User

router = APIRouter(prefix="/api/user")

@router.post('/create_user', response_model=UserModel, response_description="User Created")
async def create_user(user: UserModel):
    user_db = User(name=user.name, email=user.email, phone_number=user.phone_number)
    await user_db.create()
    return UserModel(name=user.name, email=user.email, phone_number=user.phone_number)

@router.get('/{user_name}')
async def get_user(user_name: str):
    user = await User.find({"name": "test"}).to_list()
    if user:
        return UserModel(name=user[0].name, email=user[0].email, phone_number=user[0].phone_number)
    else:
        raise HTTPException(status_code=404, detail=f"No user with name {user_name}")