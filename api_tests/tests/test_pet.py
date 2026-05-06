import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2/pet"

def test_api_cadastrar_pet():
    payload = {"id": 1010, "name": "PythonBot", "status": "available"}
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 200

def test_api_consultar_pet():
    response = requests.get(f"{BASE_URL}/1010")
    assert response.status_code in [200, 404]

def test_api_atualizar_pet():
    payload = {"id": 1010, "name": "PythonBot Editado", "status": "sold"}
    response = requests.put(BASE_URL, json=payload)
    assert response.status_code == 200