import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services import get_dashboard_data , generate_mock_jobs

client = TestClient(app)

def test_health_check():
    #Teste o endpoint de health check
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "message": "API is running"}

def test_get_cluster_info():
    #Teste o endpoint de  informações do cluster
    response = client.get("/api/v1/clusters/cluster_a/info")
    assert response.status_code == 200
    data = response.json()
    assert "cluster_id" in data
    assert "name" in data
    assert "status" in data

def test_get_cluster_dashboard():
    #Teste o endpoint de  informações do cluster
    response = client.get("/api/v1/clusters/cluster_a")
    assert response.status_code == 200
    data = response.json()
    assert "cluster_id" in data
    assert "jobs" in data
    assert "metrics" in data

def test_generate_mock_jobs():
    #Teste a geração de jobs mockados
    jobs = generate_mock_jobs("cluster_a", count=5)
    assert len(jobs) == 5
    assert all(job.cluster_id == "cluster_a" for job in jobs)



def test_nonexistent_cluster():
    #Teste cluster qque não existe
    response = client.get("/api/v1/clusters/nonexistent_cluster")
    assert response.status_code == 200 # Deve retornar fallback







