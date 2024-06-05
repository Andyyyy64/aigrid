import requests

ENDPOINT = "http://127.0.0.1:5000/"
CHAT_URL = f"{ENDPOINT}chat"

def gen_payload(props: dict):
    payload = {
        "message": props["message"]
    }
    
    return payload

while True:
    message = input("you: ");
    props = {
        "message": message
    }
    response = requests.post(CHAT_URL, json=gen_payload(props))
    print(f"aigrid: {response.text}")

