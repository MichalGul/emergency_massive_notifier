import pytest
from fastapi.testclient import TestClient
from typing import Iterator
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient
from database.mongo_setup import MONGODB_URL, MONGODB_DATABASE
from src.main import app

TEST_COLLECTION = "test_users" # todo handle dynamic test_collection name


@pytest.fixture()
async def client_test() -> Iterator[AsyncClient]:
    """
    Create an instance of the client.
    :return: yield HTTP async client.
    """
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test", follow_redirects=True) as async_client:
            try:
                yield async_client
            except Exception as e:
                print(e)


@pytest.fixture
async def test_database():
    # Connect to the test database
    client = AsyncIOMotorClient(MONGODB_URL)
    db = client[MONGODB_DATABASE]

    # Drop the test collection if it already exists
    if TEST_COLLECTION in await db.list_collection_names():
        await db.drop_collection(TEST_COLLECTION)

    # Return the test database and collection
    yield db, TEST_COLLECTION

    # Clean up the test collection
    if TEST_COLLECTION in await db.list_collection_names():
        await db.drop_collection(TEST_COLLECTION)