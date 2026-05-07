import pytest
from api_tests.utils.api_client import ApiClient
from api_tests.utils.data_factory import user_payload


@pytest.mark.api
class TestUserApi:
    def setup_method(self):
        self.client = ApiClient()
        self.user = user_payload()

    def test_create_get_update_delete_user(self):
        create_response = self.client.post("/user", json=self.user)
        assert create_response.status_code == 200

        get_response = self.client.get(f"/user/{self.user['username']}")
        assert get_response.status_code == 200
        assert get_response.json()["username"] == self.user["username"]

        self.user["firstName"] = "Updated"
        update_response = self.client.put(f"/user/{self.user['username']}", json=self.user)
        assert update_response.status_code == 200

        updated_response = self.client.get(f"/user/{self.user['username']}")
        assert updated_response.status_code == 200
        assert updated_response.json()["firstName"] == "Updated"

        delete_response = self.client.delete(f"/user/{self.user['username']}")
        assert delete_response.status_code == 200

    def test_login_and_logout_user(self):
        self.client.post("/user", json=self.user)

        login_response = self.client.get(
            "/user/login",
            params={"username": self.user["username"], "password": self.user["password"]},
        )
        assert login_response.status_code == 200
        assert "logged in user session" in login_response.json()["message"]

        logout_response = self.client.get("/user/logout")
        assert logout_response.status_code == 200
