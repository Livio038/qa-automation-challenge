import requests

BASE_URL = "https://petstore.swagger.io/v2"

class TestPetStore:
    def test_create_user(self):
        payload = {"id": 101, "username": "tester_gemini", "firstName": "Test", "lastName": "User"}
        response = requests.post(f"{BASE_URL}/user", json=payload)
        assert response.status_code == 200

    def test_add_new_pet(self):
        payload = {"id": 999, "name": "Snoopy", "status": "available"}
        response = requests.post(f"{BASE_URL}/pet", json=payload)
        assert response.status_code == 200
        assert response.json()['name'] == "Snoopy"

    def test_place_order(self):
        payload = {"id": 1, "petId": 999, "quantity": 1, "status": "placed"}
        response = requests.post(f"{BASE_URL}/store/order", json=payload)
        assert response.status_code == 200
