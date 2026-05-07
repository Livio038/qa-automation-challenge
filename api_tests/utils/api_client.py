import requests


class ApiClient:
    def __init__(self, base_url="https://petstore.swagger.io/v2"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get(self, path, **kwargs):
        return self.session.get(f"{self.base_url}{path}", **kwargs)

    def post(self, path, json=None, **kwargs):
        return self.session.post(f"{self.base_url}{path}", json=json, **kwargs)

    def put(self, path, json=None, **kwargs):
        return self.session.put(f"{self.base_url}{path}", json=json, **kwargs)

    def delete(self, path, **kwargs):
        return self.session.delete(f"{self.base_url}{path}", **kwargs)
