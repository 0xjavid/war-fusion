import feedparser
from fusion.scoring import push

KEYWORDS = [
    "missile","airstrike","rocket","drone","intercept",
    "explosion","attack","bombardment","raid","sirens"
]

AREAS_MAP = {
    "iran":"IRAN",
    "israel":"ISRAEL",
    "lebanon":"LEBANON",
    "gaza":"ISRAEL",
    "syria":"SYRIA",
    "iraq":"IRAQ",
    "yemen":"YEMEN",
    "saudi":"SAUDI"
}

FEEDS = [
    "https://feeds.reuters.com/reuters/worldNews",
    "https://rss.cnn.com/rss/edition_world.rss",
    "http://feeds.bbci.co.uk/news/world/rss.xml",
    "https://www.aljazeera.com/xml/rss/all.xml"
]

seen=set()

def news_osint():
    try:
        for url in FEEDS:
            feed=feedparser.parse(url)

            for e in feed.entries[:15]:
                title=e.title.lower()

                if title in seen:
                    continue
                seen.add(title)

                if not any(k in title for k in KEYWORDS):
                    continue

                for word,area in AREAS_MAP.items():
                    if word in title:
                        push(area,2,"خبر فوری: "+e.title[:80])

    except:
        pass
