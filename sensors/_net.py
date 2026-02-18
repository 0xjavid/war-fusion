import requests

def safe_get(url,timeout=20):
    try:
        r=requests.get(url,timeout=timeout,headers={"User-Agent":"Mozilla/5.0"})
        if r.status_code!=200:
            return None
        return r
    except:
        return None
