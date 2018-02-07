import requests
from handler import handle_message

while True:
    res = requests.get("")
    d = res.json()

    for elem in d["result"]:
        text = elem["message"]["text"]
        ans = handle_message(text)

        chat_id = elem["message"]["chat"]["id"]

        requests.post("...", params={ "chat_id": chat_id, "text": text })
