from core.state import level,score

def classify(area):
    s=score[area]

    if s>=20:
        return "ACTIVE WAR"
    if s>=14:
        return "REAL STRIKE"
    if s>=9:
        return "LIKELY ATTACK"
    if s>=5:
        return "MILITARY POSTURE"
    if s>=2:
        return "EXERCISE"
    return "NORMAL"