import mongoengine
from motor.motor_asyncio import AsyncIOMotorClient


def global_init():
    # Configure MongoEngine to use the sync driver todo get from .enf file and add authentication
    mongoengine.connect(host="mongodb://localhost:27018", alias="core", name="emn")
