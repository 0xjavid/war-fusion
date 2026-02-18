import config
from core.state import score

levels = {
    0:"🟢 عادی",
    2:"🔵 رزمایش",
    4:"🟡 آماده‌باش",
    8:"🟠 احتمال درگیری",
    12:"🔴 حمله واقعی",
    18:"⚫ جنگ"
}

def intent(area):

    # --- فیلتر خاورمیانه ---
    if area not in config.AREAS:
        return "IGNORED"

    s = score.get(area,0)

    if s >= 18: return levels[18]
    if s >= 12: return levels[12]
    if s >= 8: return levels[8]
    if s >= 4: return levels[4]
    if s >= 2: return levels[2]
    return levels[0]
