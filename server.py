import requests
from handler import handle_message

while True:
    res = requests.get("https://api.telegram.org/boted8953b0bd55fcc772f52337d3586c54052198feccdf89306b872128a3bcb895/getUpdates")
    d = res.json()

    for elem in d["result"]:
        text = elem["message"]["text"]
        ans = handle_message(text)

        chat_id = elem["message"]["chat"]["id"]

        requests.post("...", params={ "chat_id": chat_id, "text": text })
