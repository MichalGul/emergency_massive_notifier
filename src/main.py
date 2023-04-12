from fastapi import FastAPI
from .database.mongo_setup import global_init
from src.routers import users, messages

app = FastAPI(title="Emergency Massive Notifier")
app.include_router(users.router)
app.include_router(messages.router)

@app.on_event("startup")
async def startup_db_client():
    await global_init()
    print("Connected to the MongoDB database!")


@app.get("/")
async def root():
    return {"message": "Hello EMN"}

