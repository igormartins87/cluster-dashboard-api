from fastapi import HTTPException, Depends, status
from fastapi.security import APIKeyHeader
import secrets
import logging
from slowapi import Limiter
from slowapi.util import get_remote_address

logger = logging.getLogger(__name__)
limiter = Limiter(Key_func=get_remote_address)
api_key_header =APIKeyHeader(name="X-API-KEY")

#Chave API

VALID_API_KEYS = {
    "dashboard-user":"tokem -aqui",
    "admin-user":"outro-tokem"
}

async def validate_api_key(api_key: str = Depends(api_key_header)):
    #Validar API key com timing attack protection
    for valid_Key in VALID_API_KEYS.values():
        if secrets.compare_digest(api_key, valid_Key):
            logger.info(f"API Key validated sucessfully")
            return api_key
    logger.warning(f"Invalid API Key attempt:{api_key}")
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid API key"
    )

def log_security_event(event_type: str, details: str):
    #Log  de evento de segurança
    logger.warning(f"SECURITY - {event_type}: {details}")