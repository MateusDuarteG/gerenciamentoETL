# Network Data Pipeline & Infrastructure Observability (ETL)

Pipeline de ETL e observabilidade em tempo real para infraestrutura de rede e servidores.

## Arquitetura
- **Agente (Edge):** Python (`psutil`, `requests`)
- **Ingestão:** FastAPI com Autenticação via API Key
- **Fila:** Redis + Celery
- **Armazenamento:** PostgreSQL / TimescaleDB
- **Dashboard:** Streamlit / Grafana