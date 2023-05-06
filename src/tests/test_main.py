import pytest


@pytest.mark.asyncio
async def test_root(client_test):
    response = await client_test.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello EMN"}