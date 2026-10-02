
import os
from fastapi import FastAPI, Security, HTTPException, status
from fastapi.security import APIKeyHeader
from pydantic import BaseModel

app = FastAPI(title="Network ETL Pipeline")

# Define o nome do cabeçalho esperado
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# Chave secreta definida em variável de ambiente (ou valor padrão para dev)
SECRET_API_KEY = os.getenv("API_KEY", "minha_chave_super_segura_123")

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != SECRET_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key inválida ou ausente"
        )
    return api_key

class MetricSchema(BaseModel):
    device_id: str
    timestamp: int
    cpu_percent: float
    memory_percent: float
    net_bytes_sent: int
    net_bytes_recv: int

@app.post("/api/v1/telemetry", status_code=202, dependencies=[Security(verify_api_key)])
async def ingest_telemetry(data: MetricSchema):
    # Envia para a fila (Celery/Redis)
    # process_telemetry_task.delay(data.model_dump())
    return {"status": "queued"}