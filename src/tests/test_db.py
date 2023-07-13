from src.database.models import UserModel, MessageModel
from src.tests.conftest import TEST_USERS, TEST_MESSAGES
from bson.objectid import ObjectId


async def test_create_user_db(test_database):
    db = test_database
    test_user = UserModel(name="test", email="test@test.pl", phone_number="123456789")
    result = await db[TEST_USERS].insert_one(test_user.dict())
    inserted_user = await db[TEST_USERS].find_one({'_id': ObjectId(result.inserted_id)})

    assert inserted_user['name'] == "test"
    assert inserted_user['email'] == "test@test.pl"
    assert inserted_user['phone_number'] == "123456789"
    assert inserted_user['_id'] == ObjectId(result.inserted_id)


async def test_create_message_db(test_database):
    db = test_database
    test_message = MessageModel(message_title="Test title", message_text="test text", send_from_user_name="user1",
                                send_to_user_name="User2")
    result = await db[TEST_MESSAGES].insert_one(test_message.dict())

    inserted_message = await db[TEST_MESSAGES].find_one({'_id': ObjectId(result.inserted_id)})
    assert inserted_message['message_title'] == "Test title"
    assert inserted_message['message_text'] == "test text"
    assert inserted_message['send_from_user_name'] == "user1"
    assert inserted_message['_id'] == ObjectId(result.inserted_id)
