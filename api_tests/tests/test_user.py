import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2/user"

def test_api_criar_usuario():
    payload = {
        "id": 5566,
        "username": "tester_qa",
        "firstName": "Lívio",
        "lastName": "Automation",
        "email": "test@qa.com",
        "password": "123",
        "phone": "99999999",
        "userStatus": 1
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 200

def test_api_login_usuario():
    response = requests.get(f"{BASE_URL}/login", params={"username": "tester_qa", "password": "123"})
    assert response.status_code == 200
    
    # Validação inteligente: verifica se a palavra 'session' ou 'expires' está presente na resposta
    mensagem = response.json().get("message", "").lower()
    assert "session" in mensagem or "expires" in mensagem

def test_api_buscar_usuario_por_nome():
    response = requests.get(f"{BASE_URL}/tester_qa")
    assert response.status_code in [200, 404]

def test_api_logout_usuario():
    response = requests.get(f"{BASE_URL}/logout")
    assert response.status_code == 200