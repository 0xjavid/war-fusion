from collections import defaultdict

reasons = defaultdict(list)

def add_reason(area, text):
    if text not in reasons[area]:
        reasons[area].append(text)

def get_reasons(area):
    return reasons.get(area, [])

def clear_old(area):
    if area in reasons and len(reasons[area])>5:
        reasons[area]=reasons[area][-5:]
