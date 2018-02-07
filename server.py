import requests
from handler import handle_message

while True:
    res = requests.get("https://api.telegram.org/bot482414971:AAFJ4-3T9oXmPahj1QPJTRbq2uHH-i7wwtc/getUpdates")
    d = res.json()

    for elem in d["result"]:
        text = elem["message"]["text"]
        ans = handle_message(text)

        chat_id = elem["message"]["chat"]["id"]

        requests.post("https://api.telegram.org/bot482414971:AAFJ4-3T9oXmPahj1QPJTRbq2uHH-i7wwtc/getUpdates", params={ "chat_id": chat_id, "text": ans })
