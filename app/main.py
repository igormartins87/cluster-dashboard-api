from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from .api import router as api_router
from .security import limiter


app = FastAPI (
    title="Cluster Dashboard API",
    description="API para centralizar e cachear dados do dashboard de Cluster",
    version="1.0.0"
)

#Configurar CORS para permitir requests do Streamlit

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"], # URL do Streamlit
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["X-API-key", "Content-Type"],
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost" ,"127.0.0.1"]
)

app.state.limiter = limiter

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Cluster Dashboard API", "version": "1.0.0"}


