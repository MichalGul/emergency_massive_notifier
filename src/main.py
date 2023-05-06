from fastapi import FastAPI
from src.database.mongo_setup import global_init
from src.routers import users, messages

app = FastAPI(title="Emergency Massive Notifier")
app.include_router(users.router)
app.include_router(messages.router)

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = await global_init()
    print("Connected to the MongoDB database!")

@app.on_event("shutdown")
async def shutdown_db_client():
    print("Shutting down application")
    app.mongodb_client.close()


@app.get("/")
async def root():
    return {"message": "Hello EMN"}

