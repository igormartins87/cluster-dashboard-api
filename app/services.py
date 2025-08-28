import random
from datetime import datetime,timedelta
from .models import ClusterInfo, Job, Metrics, DashboardData


CLUSTER_MOCK = {
    "Cluster_a": ClusterInfo(
    cluster_id="cluster_a",
    name ="Cluster_Alpha",
    status= "active",
    total_nodes=100,
    available_nodes=75,
    grafana_url="https://grafana.example.com/alpha",
    icon="🧪"
    ),

    "Cluster_b": ClusterInfo(
    cluster_id="cluster_b",
    name="Cluster_Beta",
    status= "active",
    total_nodes=50,
    available_nodes=40,
    grafana_url="https://grafana.example.com/beta",
    icon="🚀"
    ),

    "Cluster_c": ClusterInfo(
    cluster_id="cluster_c",
    name="Cluster_gamma",
    status= "maintenance",
    total_nodes=200,
    available_nodes=0,
    grafana_url="https://grafana.example.com/gamma",
    icon="🔬"
    )
}

def generate_mock_jobs(cluster_id ,count=20):
    statuses = ["RUNNING","PENDING" ,"COMPLETED","FAILED"]
    users = ["user1", "user2", "user3","user4" ,"user5"]
    jobs = []


