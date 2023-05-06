from motor.motor_asyncio import AsyncIOMotorClient
from mongomock_motor import AsyncMongoMockClient
from beanie import init_beanie
from src.database.models import Message, User

MONGODB_URL = "mongodb://localhost:27018"
MONGODB_DATABASE = "emn"
MONGODB_DATABASE_TEST = "test"

async def global_init():
    # Configure MongoEngine to use the async driver
    # TODO get from .env file and add authentication
    client = AsyncIOMotorClient(
        MONGODB_URL
    )
    # client = AsyncMongoMockClient() todo use this in test configuration
    await init_beanie(database=client[MONGODB_DATABASE], document_models=[User, Message])
    return client
