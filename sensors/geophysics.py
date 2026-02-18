import requests,time,math
from fusion.scoring import push

recent=[]

# محدوده خاورمیانه (قفل واقعی)
def in_me(lat,lon):
    return 10<=lat<=40 and 30<=lon<=65

def locate_me(lat,lon):
    if 24<=lat<=40 and 44<=lon<=63: return "IRAN"
    if 29<=lat<=34 and 34<=lon<=36: return "ISRAEL"
    if 31<=lat<=37 and 35<=lon<=42: return "SYRIA"
    if 32<=lat<=37 and 38<=lon<=49: return "IRAQ"
    if 12<=lat<=32 and 34<=lon<=55: return "SAUDI"
    if 12<=lat<=19 and 42<=lon<=54: return "YEMEN"
    if 22<=lat<=26 and 51<=lon<=57: return "UAE"
    return None

def seismic():
    global recent
    try:
        r=requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson",timeout=20).json()

        now=time.time()
        recent=[e for e in recent if now-e[0]<600]

        for e in r["features"]:
            mag=e["properties"]["mag"]
            depth=e["geometry"]["coordinates"][2]
            lon=e["geometry"]["coordinates"][0]
            lat=e["geometry"]["coordinates"][1]

            if not in_me(lat,lon):
                continue

            area=locate_me(lat,lon)
            if not area:
                continue

            if mag and 1.2<=mag<=4.2 and depth<=3:

                nearby=sum(1 for t,la,lo in recent if math.hypot(lat-la,lon-lo)<1.5)
                recent.append((now,lat,lon))

                if nearby>=2:
                    print("ME EXPLOSION CLUSTER:",area)
                    push(area,8,"انفجارهای پیاپی ثبت شد")

    except:
        pass


def bgp():
    pass
