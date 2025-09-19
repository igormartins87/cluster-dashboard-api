import pytest
from fastapi.testclient import TestClient
from fastapi import status
from app.main import app

client = TestClient(app)

def test_api_Key_required():
    #Testar que API_key é obrigatória
    response = client.get("/api/v1/clusters/cluster_a")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_invalid_api_key():
    #Testar API key inválida
    response = client.get(
        "/api/v1/clusters/cluster_a",
        headers={"X-API-key":"invalid_key"}
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

def test_rate_limiting():
    #Testar rate limiting
    valid_header = {"X-API-Key": "token aqui"}

    for i in range(11): #Limite é de 10 minutos
        response =client.get("/api/v1/clusters/cluster_a", headers=valid_header)

    #11º deve falhar
    assert response.status_code == status.HTTP_429_TOO_MANY_REQUESTS

def test_sql_injection_protection():
    #Teste proteção contra injection
    response =client.get(
        "/api/v1/clusters/' ; DROP TABLE user;--",
        headers={"X-API-key":"tokem aqui"}

    )
    #deve rejeitar inputs malicioso
    assert response.status_code in [400, 404, 422]
