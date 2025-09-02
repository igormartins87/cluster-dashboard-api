import random
from datetime import datetime,timedelta
from .models import ClusterInfo, Job, Metrics, DashboardData


CLUSTER_MOCK = {
    "cluster_a": ClusterInfo(
    cluster_id="cluster_a",
    name ="Cluster_Alpha",
    status= "active",
    total_nodes=100,
    available_nodes=75,
    grafana_url="https://grafana.example.com/alpha",
    icon="🧪"
    ),

    "cluster_b": ClusterInfo(
    cluster_id="cluster_b",
    name="Cluster_Beta",
    status= "active",
    total_nodes=50,
    available_nodes=40,
    grafana_url="https://grafana.example.com/beta",
    icon="🚀"
    ),

    "cluster_c": ClusterInfo(
    cluster_id="cluster_c",
    name="Cluster_gamma",
    status= "maintenance",
    total_nodes=200,
    available_nodes=0,
    grafana_url="https://grafana.example.com/gamma",
    icon="🔬"
    )
}
# job
def generate_mock_jobs(cluster_id ,count=20):
    statuses = ["RUNNING","PENDING" ,"COMPLETED","FAILED"]
    users = ["user1", "user2", "user3","user4" ,"user5"]
    jobs = []

    for i in range(count):
        job_id = f"{cluster_id}_job{i+1}"
        status=random.choice(statuses)
        runtime= f"{random.randint(1, 48)} : {random.randint(0,59):02d} : {random.randint(0,59):02d}"
        queue_time = f"{random.randint(0, 24):02d} : {random.randint(0, 59):02d}"

        jobs.append(Job(
            job_id=job_id,
            name=f"job{i+1}",
            user=random.choice(users),
            status=status,
            partition="genral",
            nodes=random.randint(1, 8),
            rumtime= runtime,
            queue_time= queue_time
        ))
    return jobs

#metrica

def generate_mock_metrics(cluster_id):
    return Metrics(
        cluster_id=cluster_id,
        lazy_workers=random.randint(0, 10),
        pending_jobs= random.randint(0, 50),
        complete_jobs=random.randint(100, 1000),
        last_update=datetime.now()
    )

#Principal para obter Dados

def get_dashboard_data(cluster_id:str) -> DashboardData:
    #Obtem todos os dados para o dash de um cluster especifico
    cluster_info = CLUSTER_MOCK.get(cluster_id.lower())

    if not cluster_info:
        cluster_info = ClusterInfo(
            cluster_id=cluster_id,
            name= f"Cluster {cluster_id.upper()}",
            status= "unknown",
            total_nodes=0,
            available_nodes=0,
            grafana_url="",
            icon="❓"
        )
    jobs = generate_mock_jobs(cluster_id)
    metrics = generate_mock_metrics(cluster_id)

    return DashboardData(
        cluster_id=cluster_id,
        cluster_info=cluster_info,
        jobs=jobs,
        metrics=metrics
    )

