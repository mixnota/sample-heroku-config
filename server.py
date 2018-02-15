import requests
from handler import handle_message


max_update_id = -1
chat_ids_of_users = set()
while True:
    res = requests.get("https://api.telegram.org/bot482414971:AAFJ4-3T9oXmPahj1QPJTRbq2uHH-i7wwtc/getUpdates", params={"offset": -1})
    d = res.json()
    if d["result"][0]["update_id"] > max_update_id:
        max_update_id = max(max_update_id, d["result"][0]["update_id"])
        for elem in d["result"]:
            text = elem["message"]["text"]
            ans = handle_message(text, elem["message"]["chat"]["id"])
            chat_id = elem["message"]["chat"]["id"]
            if text == "/start":
                chat_ids_of_users.add(chat_id)
                continue
            if ans and text != "/show":
                for chat in chat_ids_of_users:
                    requests.post("https://api.telegram.org/bot482414971:AAFJ4-3T9oXmPahj1QPJTRbq2uHH-i7wwtc/sendMessage",
                                  params={"chat_id": chat, "text": ans})
            elif ans and text == "/show":
                requests.post("https://api.telegram.org/bot482414971:AAFJ4-3T9oXmPahj1QPJTRbq2uHH-i7wwtc/sendMessage",
                              params={"chat_id": chat_id, "text": ans})
