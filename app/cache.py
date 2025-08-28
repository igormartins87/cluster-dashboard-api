import redis
import json
from datetime import timedelta
from typing import Optional, Any

#config do Redis
redis_client = redis.Redis(host='localhost',port=6379, db=0, decode_responses=True)

def get_cached_data(Key: str) -> Optional[Any]:
    cached = redis_client.get(Key)
    if cached:
        return json.load(cached)
    return None

def set_cached_data(Key: str, data: Any, ttl_seconds: int = 30) -> None:
    seralized = json.dumps(data, default=str)
    redis_client.setex(Key, timedelta(seconds=ttl_seconds), seralized)

def clear_cache(Key: str=None) -> None:
    #limpa todo o tipo de cache
    if Key:
        redis_client.delete(Key)
    else:
        redis_client.flushdb()
