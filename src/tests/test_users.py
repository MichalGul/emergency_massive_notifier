from fastapi.testclient import TestClient
import pytest
from httpx import AsyncClient
from bson.objectid import ObjectId
from src.database.models import UserModel, User

@pytest.mark.asyncio
async def test_get_non_existing_user(client_test: AsyncClient):
    response = await client_test.get("/api/user/test")
    assert response.status_code == 404
    msg = response.json()
    assert "detail" in msg and "No user with name" in msg["detail"]

@pytest.mark.asyncio
async def test_create_user(client_test):
    test_user = UserModel(name="test", email="test@test.pl", phone_number="666666666")
    create_response = await client_test.post('/api/user/create_user', json=test_user.dict())
    assert create_response.status_code == 200
    assert create_response.json() == test_user.dict()

    response = await client_test.get(f"/api/user/{test_user.name}")
    assert response.status_code == 200
    assert response.json() == test_user.dict()

    #todo add cleanup or handling mock database with client_test



async def test_create_user_db(test_database):
    db, collection = test_database
    test_user = UserModel(name="test", email="test@test.pl", phone_number="666666666")
    result = await db[collection].insert_one(test_user.dict())
    # cleanup
    del_result = await db[collection].delete_one({'_id': ObjectId(result.inserted_id)})



