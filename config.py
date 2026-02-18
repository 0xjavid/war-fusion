import os

# ================= TELEGRAM =================
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("TOKEN environment variable not set")

# ================= AREAS (Middle East only) =================
AREAS = {
    "IRAN": (24,40,44,63),
    "ISRAEL": (29,34,34,36),
    "LEBANON": (33,35,35,37),
    "SYRIA": (31,37,35,42),
    "IRAQ": (32,37,38,49),
    "SAUDI": (16,32,34,55),
    "YEMEN": (12,19,42,54),
    "UAE": (22,26,51,57),
    "QATAR": (24,27,50,52),
    "OMAN": (16,26,52,60),
    "JORDAN": (29,33,35,39),
    "KUWAIT": (28,31,46,49),
    "BAHRAIN": (25,27,50,51),
    "PERSIAN_GULF": (24,30,48,56),
    "RED_SEA": (12,28,32,44)
}

# ================= TIMERS =================
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 60))
STATUS_INTERVAL = int(os.getenv("STATUS_INTERVAL", 300))

# ================= OPTIONS =================
DEBUG = os.getenv("DEBUG", "0") == "1"
