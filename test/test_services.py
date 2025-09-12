import pytest
from app.services import get_dashboard_data, CLUSTER_MOCK
from app.models import DashboardData
from unittest.mock import patch

def test_get_dashboard_data_existing_cluster():
    #Teste para busca de cluster existente
    dashboard_data = get_dashboard_data("cluster_a")
    assert isinstance(dashboard_data, DashboardData)
    assert dashboard_data.cluster_id == "cluster_a"
    assert dashboard_data.cluster_info.name == "Cluster_Alpha"


def test_get_dashboard_data_nonexistent_cluster():
    #Teste para busca de  cluster  não existente
    with patch('app.service.generate_mock_jobs',return_value=[]):
        dashboard_data = get_dashboard_data("unknown_cluster")
        assert isinstance(dashboard_data, DashboardData)
        assert dashboard_data.cluster_id == "unknown_cluster"
        assert dashboard_data.cluster_info.status == "unknown"



def test_clusters_mock_structure():
    #Teste a estrrutura dos dados mockados
    assert "cluster_a" in CLUSTER_MOCK
    assert "cluster_b" in CLUSTER_MOCK
    cluster_a = CLUSTER_MOCK["cluster_a"]
    assert cluster_a.total_nodes > 0
    assert cluster_a.available_nodes <=cluster_a.total_nodes



