from sensors.battlefield import thermal,aircraft,airspace
from sensors.intel import navwarn,news,social
from sensors.geophysics import seismic,bgp
from sensors.news_osint import news_osint
from fusion.analysis import intent
from fusion.reasons import get_reasons,clear_old
import asyncio,time,config,importlib
from bot.telegram_bot import send,listen
from core.state import level_cache,last_status,decay

CHECK_INTERVAL = config.CHECK_INTERVAL
STATUS_INTERVAL = config.STATUS_INTERVAL

def areas():
    importlib.reload(config)
    return list(config.AREAS.keys())

def build_message(area,level):
    reasons=get_reasons(area)
    msg=f"🚨 {area} — {level}\n"
    for r in reasons:
        msg+=f"• {r}\n"
    clear_old(area)
    return msg

async def telegram_loop():
    while True:
        listen()
        await asyncio.sleep(2)

async def world_loop():
    global last_status

    print("WORLD MONITOR ACTIVE")
    send("🌍 مانیتور خاورمیانه فعال شد")

    while True:

        print("Scanning sensors...")

        thermal()
        aircraft()
        airspace()
        navwarn()
        news()
        social()
        news_osint()
        seismic()
        bgp()

        decay()

        for a in areas():
            cur=intent(a)

            if a not in level_cache:
                level_cache[a]=cur
                if cur!="🟢 عادی":
                    send(build_message(a,cur))
                continue

            if level_cache[a]!=cur:
                send(build_message(a,cur))

            level_cache[a]=cur

        now=time.time()
        if now-last_status>STATUS_INTERVAL:
            last_status=now
            rep="🌎 وضعیت خاورمیانه\n"
            for a in areas():
                rep+=f"{a}: {intent(a)}\n"
            send(rep)

        await asyncio.sleep(CHECK_INTERVAL)
