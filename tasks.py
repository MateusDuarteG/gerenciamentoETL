# tasks.py - Celery Task
import requests

TELEGRAM_BOT_TOKEN = "SEU_TOKEN_AQUI"
TELEGRAM_CHAT_ID = "SEU_CHAT_ID"

def check_thresholds_and_alert(data):
    if data['cpu_percent'] > 90.0:
        message = f"🚨 *ALERTA DE CPU* 🚨\nServidor: {data['device_id']}\nUso de CPU: {data['cpu_percent']}%"
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"})