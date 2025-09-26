from fastapi import APIRouter, HTTPException, Depends, Request
from .security import validate_api_key, log_security_event, limiter
from .services import get_dashboard_data, CLUSTER_MOCK
from .cache import get_cached_data, set_cached_data
from .models import DashboardData, ClusterInfo, Job
from slowapi.errors import RateLimitExceeded

router = APIRouter()

@router.exception.handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    log_security_event("RATE_LIMIT_EXCEEDED", f"IP: {request.client.host}")
    return {
        "detail" :"Rate limit exceeded",
        "retry_after": f"{exc.retry_after} seconds"
    },429

@router.get("/test-auth")
@limiter.limit("5/minute")
async def test_auth_endpoint(
    request: Request,
    api_Key: str = Depends(validate_api_key)
):
    return {
        "message": "Authenticated sucessfully",
        "user_type": user_type,
        "rate_limit": "5 requests per minut"
    }



@router.get("/clusters/{cluster_id}", response_model= DashboardData)
@limiter.limit("10/minute")
async def get_cluster_dashboard(
    request: Request,
    cluster_id: str,
    api_Key: str = Depends(validate_api_key)
):
    # EndPoint principal para obter dados do dashboard
    # cache_Key = f"cluster_dashboard:{cluster_id}"
    # cached_data = get_cached_data(cache_Key)

    # if cached_data:
    #     return DashboardData(**cached_data)

    # Se não tiver cached, busca dados

    try:
        dashboard_data = get_dashboard_data(cluster_id)
        log_security_event("CLUSTER_ACESS", f"User {user_type} acessed cluster {cluster_id}")

        return dashboard_data
    except Exception as e:
        log_security_event("CLUSTER_ACESS", f"User {user_type} acessed cluster {cluster_id}")




@router.get("/clusters/{cluster_id}/info" ,response_model=ClusterInfo)
async def get_cluster_info(
    cluster_id: str,
    api_key:str =Depends(validate_api_key)
):

    # EndPoint apenas para informações do cluster (cache mais limpo)
    # cache_Key = f"cluster_info:{cluster_id}"
    # cached_data = get_cached_data(cache_Key)

    # if cached_data:
    #     return cached_data

    cluster_info = CLUSTER_MOCK.get(cluster_id)

    if not cluster_info:
        log_security_event("UNAUTHORIZED_ACESS", f"Cluster não encontrado: {cluster_id}")
        raise HTTPException(status_code=404,detail="Cluster not found")
    #armazena no cache(ttl de 30 segundos)
    # set_cached_data(cache_Key, cluster_info, ttl_seconds=3600) # 1 hora

    return cluster_info

@router.get("/health")
async def healh_check():
    return{"status": "healthy", "message": "API is running"}

