import requests,json,os,time
from config import TOKEN
from fusion.scoring import push

USERS_FILE="users.json"
offset=0

def load_users():
    if not os.path.exists(USERS_FILE):
        return set()
    try:
        return set(json.load(open(USERS_FILE)))
    except:
        return set()

def save_users(u):
    json.dump(list(u),open(USERS_FILE,"w"))

users=load_users()

def send(text,chat=None):
    targets=[chat] if chat else list(users)
    for uid in targets:
        try:
            requests.post(
                f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                data={"chat_id":uid,"text":text},
                timeout=20
            )
        except:
            time.sleep(2)

def listen():
    global offset,users
    try:
        r=requests.get(
            f"https://api.telegram.org/bot{TOKEN}/getUpdates",
            params={"timeout":25,"offset":offset},
            timeout=60
        ).json()

        for u in r.get("result",[]):
            offset=u["update_id"]+1
            if "message" not in u:continue

            chat=str(u["message"]["chat"]["id"])
            text=u["message"].get("text","")

            if text.startswith("/start"):
                users.add(chat)
                save_users(users)
                send("🛰️ متصل شدی به مانیتور جنگ",chat)

            if text.startswith("/test"):
                push("IRAN",20)
                send("test event injected",chat)

    except:
        pass
