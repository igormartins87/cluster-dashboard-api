from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime

class Job(BaseModel):
    job_id: str
    name: str
    user: str
    status: str
    partition: str
    nodes: int
    rumtime: str
    queue_time: str

class ClusterInfo(BaseModel):
    cluster_id: str
    name: str
    user: Optional[str] = None
    status: str
    total_nodes: int
    available_nodes: int
    grafana_url: str
    icon: str

class Metrics(BaseModel):
    cluster_id: str
    lazy_workers: int
    pending_jobs: int
    complete_jobs: int
    last_update: datetime

class DashboardData(BaseModel):
    cluster_id: ClusterInfo
    Job: List[Job]
    metrics: Metrics







