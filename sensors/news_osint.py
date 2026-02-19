import feedparser
from fusion.scoring import push

KEYWORDS = [
    "missile","rocket","strike","airstrike","drone","explosion",
    "intercept","sirens","attack","raid","bombardment"
]

ME_WORDS = {
    "iran":"IRAN",
    "israel":"ISRAEL",
    "lebanon":"LEBANON",
    "hezbollah":"LEBANON",
    "gaza":"ISRAEL",
    "hamas":"ISRAEL",
    "syria":"SYRIA",
    "iraq":"IRAQ",
    "yemen":"YEMEN",
    "houthi":"YEMEN",
    "saudi":"SAUDI",
    "red sea":"RED_SEA",
    "gulf":"PERSIAN_GULF"
}

FEEDS = [
    "https://feeds.reuters.com/reuters/worldNews",
    "http://feeds.bbci.co.uk/news/world/rss.xml",
    "https://www.aljazeera.com/xml/rss/all.xml"
]

seen=set()

def news_osint():
    try:
        for url in FEEDS:
            feed=feedparser.parse(url)

            for e in feed.entries[:20]:
                title=e.title.lower()

                if title in seen:
                    continue
                seen.add(title)

                # اول باید کلمه نظامی داشته باشد
                if not any(k in title for k in KEYWORDS):
                    continue

                # بعد باید منطقه خاورمیانه داشته باشد
                for word,area in ME_WORDS.items():
                    if word in title:
                        print("ME NEWS:",title)
                        push(area,2,"خبر فوری: "+e.title[:90])
                        break

    except:
        pass
