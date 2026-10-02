import time
import psutil
import requests

API_URL = "http://localhost:8000/api/v1/telemetry"
API_KEY = "minha_chave_super_segura_123"

def collect_metrics():
    return {
        "device_id": "server-ubtl-01",
        "timestamp": int(time.time()),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "net_bytes_sent": psutil.net_io_counters().bytes_sent,
        "net_bytes_recv": psutil.net_io_counters().bytes_recv
    }

def send_data():
    data = collect_metrics()
    headers = {
        "X-API-Key": API_KEY,
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(API_URL, json=data, headers=headers, timeout=5)
        print(f"[{data['timestamp']}] Enviado | Status: {response.status_code}")
    except Exception as e:
        print(f"Erro ao enviar métricas: {e}")

if __name__ == "__main__":
    while True:
        send_data()
        time.sleep(10)