# 📊 Plataforma de ETL & Observabilidade de Infraestrutura

> Pipeline assíncrono e distribuído para ingestão, processamento, agregação de telemetria de rede e monitoramento de infraestrutura em tempo real.

---

## 📌 Visão Geral

O **gerenciamentoETL** é uma solução robusta de **Network Data Pipeline & Observabilidade** projetada para coletar métricas de rede, transformar logs e eventos não estruturados e disponibilizar dados valiosos em dashboards analíticos de alta performance.

O objetivo principal do projeto é mitigar gargalos em ambientes corporativos e de telecomunicações através de automação, processamento agendado/assíncrono e alertas preventivos.

---

## 🛠️ Arquitetura e Tecnologias

A aplicação utiliza uma arquitetura moderna baseada em microsserviços e contêineres:

* **Linguagem Principal:** Python 3.x
* **Framework de API:** FastAPI (endpoints RESTful para envio e consulta de dados)
* **Gerenciamento de Filas / Workers:** Celery + Redis (processamento assíncrono de pipelines ETL)
* **Visualização & Dashboard:** Streamlit / Panel (painel em tempo real para observabilidade de rede)
* **Banco de Dados:** SQLite (desenvolvimento/testes) e MySQL / PostgreSQL
* **Containerização & DevOps:** Docker, Docker Compose e WSL2

---

## 🚀 Funcionalidades Principais

* **Extração (Extract):** Ingestão contínua de métricas de rede, logs de pacotes e eventos de ativos de TI.
* **Transformação (Transform):** Limpeza, estruturação, normalização de IP/Portas e agregação de volume de tráfego.
* **Carga (Load):** Persistência otimizada e estruturada para consultas analíticas rápidas.
* **Dashboard Interativo:** Visualização gráfica de consumo de banda, latência e status dos serviços.
* **Fila de Tarefas:** Execução de pipelines em segundo plano sem bloquear a interface/API.

---

## 🔧 Como Executar o Projeto

### Pré-requisitos
* Docker e Docker Compose instalados
* Git

### Passos

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/MateusDuarteG/gerenciamentoETL.git](https://github.com/MateusDuarteG/gerenciamentoETL.git)
   cd gerenciamentoETL

   Suba o ambiente com Docker Compose:

Bash
docker-compose up -d --build
Acesse as interfaces:

API FastAPI (Docs Swagger): http://localhost:8000/docs

Dashboard de Observabilidade: http://localhost:8501

📝 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para utilizar e contribuir!
