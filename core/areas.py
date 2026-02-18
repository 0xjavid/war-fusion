import importlib,config

# فقط مناطق مجاز
def allowed_areas():
    importlib.reload(config)
    return list(config.AREAS.keys())
