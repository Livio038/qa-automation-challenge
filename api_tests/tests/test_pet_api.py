import pytest
from api_tests.utils.api_client import ApiClient
from api_tests.utils.data_factory import pet_payload


@pytest.mark.api
class TestPetApi:
    def setup_method(self):
        self.client = ApiClient()
        self.pet = pet_payload()

    def test_create_get_update_delete_pet(self):
        create_response = self.client.post("/pet", json=self.pet)
        assert create_response.status_code == 200
        assert create_response.json()["name"] == self.pet["name"]

        get_response = self.client.get(f"/pet/{self.pet['id']}")
        assert get_response.status_code == 200
        assert get_response.json()["id"] == self.pet["id"]

        self.pet["status"] = "sold"
        update_response = self.client.put("/pet", json=self.pet)
        assert update_response.status_code == 200
        assert update_response.json()["status"] == "sold"

        delete_response = self.client.delete(f"/pet/{self.pet['id']}")
        assert delete_response.status_code == 200

    def test_find_pet_by_status(self):
        self.client.post("/pet", json=self.pet)

        response = self.client.get("/pet/findByStatus", params={"status": "available"})
        assert response.status_code == 200
        assert isinstance(response.json(), list)

        self.client.delete(f"/pet/{self.pet['id']}")
