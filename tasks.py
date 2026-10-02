# tasks.py - Celery Task
from celery import Celery

# Inicialização do Celery conectando ao Redis
app = Celery('tasks', broker='redis://localhost:6379/0')

TELEGRAM_BOT_TOKEN = "SEU_TOKEN_AQUI"
TELEGRAM_CHAT_ID = "SEU_CHAT_ID"

@app.task
def check_thresholds_and_alert(data):
    if data.get('cpu_percent', 0) > 90.0:
        message = f"🚨 ALERTA DE CPU 🚨\nServidor: {data['device_id']}\nUso de CPU: {data['cpu_percent']}%"
        print(message)
        
        # Envia para o Telegram apenas se o Token tiver sido configurado
        if TELEGRAM_BOT_TOKEN != "SEU_TOKEN_AQUI":
            import requests
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message})