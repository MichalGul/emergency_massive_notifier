from fastapi import FastAPI
from .database.mongo_setup import global_init
from .database.models import User, Message, UserModel
app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    global_init()
    print("Connected to the MongoDB database!")


#TODO add routers
@app.post('/create_user', response_model=UserModel)
async def create_user(user: UserModel):
    user_db = User(name=user.name, email=user.email, phone_number=user.phone_number)
    user_db.save()
    return UserModel(name=user.name, email=user.email, phone_number=user.phone_number)

@app.get("/")
async def root():
    return {"message": "Hello EMN"}

