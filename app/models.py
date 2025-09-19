from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class Job(BaseModel):
    job_id: str = Field(..., pattern="^[a-zA-Z0-9_-]+$")
    name: str = Field(..., min_length=1, max_length=100)
    user: Optional[str]= Field(None,max_length=50)
    status: str= Field(..., pattern="^(RUNNING|PENDING|FAILED)$")
    partition: str = Field(..., max_length=50)
    nodes: int = Field(ge=1, le=256)
    rumtime: str= Field(...,pattern="^\d{1,2}:\d{2}:\d{2}$")
    queue_time: str= Field(...,pattern="^\d{1,2}:\d{2}$")
    cluster_id:str = Field(..., min_length=1, max_length=20, pattern="^[a-zA-Z0-9_-]+$")

class ClusterInfo(BaseModel):
    cluster_id: str = Field(..., min_length=1, max_length=20, pattern="^[a-zA-Z0-9_-]+$")
    name: str = Field(..., min_length=1, max_length=50)
    user: Optional[str]= Field(None,max_length=50)
    status: str= Field(..., pattern="^(active|inactive|maintenance)$")
    total_nodes: int =Field(ge=0, le=1000)
    available_nodes: int =Field(ge=0, le=1000)
    grafana_url: Optional[str] = Field(None, pattern="^https?://")
    icon: str = Field(..., max_length=5)


class Metrics(BaseModel):
    cluster_id: str
    lazy_workers: int
    pending_jobs: int
    complete_jobs: int
    last_update: datetime

class DashboardData(BaseModel):
    cluster_id: str
    cluster_info: ClusterInfo
    jobs: List[Job]
    metrics: Metrics







