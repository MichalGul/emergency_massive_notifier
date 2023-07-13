import pytest
from fastapi.testclient import TestClient
from typing import Iterator
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient
from database.mongo_setup import MONGODB_URL, MONGODB_DATABASE, MONGODB_DATABASE_TEST
from src.main import app

TEST_USERS = "test_users"
TEST_MESSAGES = "test_messages"

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
            finally:
                # Clean all test colection on teardown
                test_db = app.mongodb_client[MONGODB_DATABASE_TEST]
                for collection in await test_db.list_collections():
                    await test_db[collection['name']].delete_many({})


@pytest.fixture
async def test_database():
    # Connect to the test database
    client = AsyncIOMotorClient(MONGODB_URL)
    db = client[MONGODB_DATABASE_TEST]

    # Return the test database and collection
    yield db

    # Clean up the test collections
    for collection in await db.list_collections():
        await db[collection['name']].delete_many({})