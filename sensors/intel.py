import requests,feedparser
from fusion.scoring import push

# ---------- NAVWARN ----------
def navwarn():
    try:
        t=requests.get("https://msi.nga.mil/api/publications/navwarnings",timeout=20).text.upper()
        if any(x in t for x in ["MISSILE","FIRING","GUNNERY","ROCKETS","EXERCISE"]):
            print("NAVAL WARNING DETECTED")
            for a in ["IRAN","ISRAEL","SAUDI","SYRIA","IRAQ","LEBANON"]:
                push(a,5)
    except Exception as e:
        print("NAVWARN ERROR:",e)

# ---------- NEWS ----------
def news():
    try:
        f=feedparser.parse("https://www.aljazeera.com/xml/rss/all.xml")
        for e in f.entries[:25]:
            t=e.title.lower()
            if any(x in t for x in ["missile","airstrike","rocket","attack","intercept","drone"]):
                print("NEWS HIT:",t[:70])
                for a in ["ISRAEL","IRAN","SYRIA","LEBANON","IRAQ"]:
                    push(a,4)
    except Exception as e:
        print("NEWS ERROR:",e)

# ---------- SOCIAL BURST ----------
def social():
    try:
        r=requests.get("https://nitter.net/search?f=tweets&q=explosion",timeout=15).text.lower()
        if any(x in r for x in ["boom","blast","intercept","sirens","impact"]):
            print("SOCIAL BURST")
            for a in ["ISRAEL","IRAN","LEBANON","SYRIA"]:
                push(a,4)
    except Exception as e:
        print("SOCIAL ERROR:",e)
