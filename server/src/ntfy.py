import requests
import json

def send_notification(ntfy_key: str, message: json):
    requests.post(
        f"https://ntfy.sh/{ntfy_key}",
        json=message
    )