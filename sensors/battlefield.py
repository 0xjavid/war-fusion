import requests
from fusion.scoring import push, locate

HEADERS = {"User-Agent": "Mozilla/5.0"}

# ================= NASA THERMAL =================
def thermal():
    try:
        url = "https://firms.modaps.eosdis.nasa.gov/api/area/csv/VIIRS_SNPP_NRT/world/1"
        r = requests.get(url, headers=HEADERS, timeout=25)

        if "latitude" not in r.text.lower():
            print("NASA: blocked")
            return

        lines = r.text.split("\n")[1:80]

        for line in lines:
            if not line or "," not in line:
                continue

            parts = line.split(",")

            try:
                lat = float(parts[0])
                lon = float(parts[1])
                bright = float(parts[2])
            except:
                continue

            if bright > 380:
                area = locate(lat, lon)
                if area:
                    print("THERMAL HIT:", area, bright)
                    push(area, 4)

    except Exception as e:
        print("THERMAL ERROR:", e)


# ================= MILITARY AIRCRAFT =================
def aircraft():
    try:
        r = requests.get(
            "https://api.adsbexchange.com/v2/mil/",
            headers=HEADERS,
            timeout=25
        )

        if r.status_code != 200 or len(r.text) < 50:
            print("ADSB: blocked")
            return

        data = r.json()

        for ac in data.get("ac", []):
            lat = ac.get("lat")
            lon = ac.get("lon")
            call = str(ac.get("call", ""))

            if not lat:
                continue

            if any(x in call for x in ["KC", "E3", "RCH", "FORTE", "RRR", "NATO"]):
                area = locate(lat, lon)
                if area:
                    print("MIL AIR:", area, call)
                    push(area, 3)

    except Exception as e:
        print("ADSB ERROR:", e)


# ================= AIRSPACE / NOTAM =================
def airspace():
    try:
        r = requests.get(
            "https://aviationweather.gov/api/data/notam?format=xml",
            headers=HEADERS,
            timeout=25
        )

        t = r.text.upper()

        if "AIRSPACE CLOSED" in t or "RESTRICTED" in t or "MILITARY OPS" in t:
            print("NOTAM WARNING")
            for a in ["ISRAEL", "IRAN", "SYRIA", "LEBANON", "IRAQ"]:
                push(a, 2)

    except Exception as e:
        print("NOTAM ERROR:", e)
