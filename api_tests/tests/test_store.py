import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2/store"

def test_api_consultar_inventario():
    response = requests.get(f"{BASE_URL}/inventory")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_api_criar_pedido():
    payload = {
        "id": 1,
        "petId": 1010,
        "quantity": 1,
        "shipDate": "2026-05-06T23:00:00.000Z",
        "status": "placed",
        "complete": True
    }
    response = requests.post(f"{BASE_URL}/order", json=payload)
    assert response.status_code == 200

def test_api_buscar_pedido_inexistente():
    response = requests.get(f"{BASE_URL}/order/99999")
    assert response.status_code == 404