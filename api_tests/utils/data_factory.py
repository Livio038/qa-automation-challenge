from datetime import datetime
import random


def unique_id():
    timestamp = datetime.now().strftime("%H%M%S%f")
    return int(timestamp) + random.randint(1, 999)


def user_payload():
    user_id = unique_id()
    username = f"qa_user_{user_id}"
    return {
        "id": user_id,
        "username": username,
        "firstName": "Livio",
        "lastName": "Junior",
        "email": f"{username}@email.com",
        "password": "123456",
        "phone": "85999999999",
        "userStatus": 1,
    }


def pet_payload():
    pet_id = unique_id()
    return {
        "id": pet_id,
        "category": {"id": 1, "name": "dogs"},
        "name": f"dog_{pet_id}",
        "photoUrls": ["https://example.com/dog.png"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "available",
    }


def order_payload(pet_id):
    return {
        "id": unique_id(),
        "petId": pet_id,
        "quantity": 1,
        "shipDate": "2026-05-07T00:00:00.000Z",
        "status": "placed",
        "complete": True,
    }
