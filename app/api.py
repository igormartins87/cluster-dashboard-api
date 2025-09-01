from fastapi import APIRouter, HTTPException
from .services import get_dashboard_data
from .cache import get_cached_data, set_cached_data
from .models import DashboardData

router = APIRouter()

@router.get("/clusters/{cluster_id}", response_model= DashboardData)
async def get_cluster_dashboard(cluster_id:str):
    # EndPoint principal para obter dados do dashboard
    # cache_Key = f"cluster_dashboard:{cluster_id}"
    # cached_data = get_cached_data(cache_Key)

    # if cached_data:
    #     return DashboardData(**cached_data)

    # Se não tiver cached, busca dados

    dashboard_data = get_dashboard_data(cluster_id)
    #armazena no cache(ttl de 30 segundos)
    # set_cached_data(cache_Key, dashboard_data.dict(), ttl_seconds=30)

    return dashboard_data

@router.get("/clusters/{cluster_id}/info")
async def get_cluster_dashboard(cluster_id:str):
    # EndPoint apenas para informações do cluster (cache mais limpo)
    # cache_Key = f"cluster_info:{cluster_id}"
    # cached_data = get_cached_data(cache_Key)

    # if cached_data:
    #     return cached_data

    dashboard_data = get_dashboard_data(cluster_id)
    cluster_info =dashboard_data.cluster_info.dict()
    #armazena no cache(ttl de 30 segundos)
    # set_cached_data(cache_Key, cluster_info, ttl_seconds=3600) # 1 hora

    return cluster_info

@router.get("/health")
async def healh_check():
    return{"status": "healthy", "message": "API is running"}

