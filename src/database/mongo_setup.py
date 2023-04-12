from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from src.database.models import Message, User
async def global_init():
    # Configure MongoEngine to use the sync driver todo get from .env file and add authentication
    client = AsyncIOMotorClient(
        "mongodb://localhost:27018"
    )
    await init_beanie(database=client.emn, document_models=[User, Message])

