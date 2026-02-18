from core.state import score
from fusion.reasons import add_reason

def locate(lat,lon):
    import config
    for a,b in config.AREAS.items():
        if b[0]<=lat<=b[1] and b[2]<=lon<=b[3]:
            return a
    return None

def push(area,weight,reason=None):
    if not area:
        return

    score[area]+=weight

    if reason:
        add_reason(area,reason)

    print("EVENT:",area,"+",weight,"=>",score[area],reason)
