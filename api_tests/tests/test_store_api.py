import pytest
from api_tests.utils.api_client import ApiClient
from api_tests.utils.data_factory import pet_payload, order_payload


@pytest.mark.api
class TestStoreApi:
    def setup_method(self):
        self.client = ApiClient()
        self.pet = pet_payload()
        self.client.post("/pet", json=self.pet)
        self.order = order_payload(self.pet["id"])

    def test_create_get_delete_order(self):
        create_response = self.client.post("/store/order", json=self.order)
        assert create_response.status_code == 200
        assert create_response.json()["petId"] == self.pet["id"]

        get_response = self.client.get(f"/store/order/{self.order['id']}")
        assert get_response.status_code == 200
        assert get_response.json()["id"] == self.order["id"]

        delete_response = self.client.delete(f"/store/order/{self.order['id']}")
        assert delete_response.status_code == 200

        self.client.delete(f"/pet/{self.pet['id']}")

    def test_get_inventory(self):
        response = self.client.get("/store/inventory")
        assert response.status_code == 200
        assert isinstance(response.json(), dict)
