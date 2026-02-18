import time
from collections import defaultdict
import config

score = defaultdict(int)
level_cache = {}
last_status = 0
last_decay = time.time()

DECAY_INTERVAL = 120
DECAY_AMOUNT = 1

def add_event(area,points):
    if area not in config.AREAS:
        return
    score[area]+=points
    score[area]=min(score[area],50)

def decay():
    global last_decay
    now=time.time()

    # --- حذف مناطق غیر مجاز ---
    invalid=[k for k in list(score.keys()) if k not in config.AREAS]
    for k in invalid:
        del score[k]
        if k in level_cache:
            del level_cache[k]

    if now-last_decay < DECAY_INTERVAL:
        return

    last_decay=now

    for a in list(score.keys()):
        if score[a]>0:
            score[a]-=DECAY_AMOUNT
            print("decay:",a,score[a])
