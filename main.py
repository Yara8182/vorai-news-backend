from fastapi import FastAPI
import feedparser

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Vorai News Assistant Running"}

@app.get("/news")
def get_news():
    feed_url = "https://www.thenewhumanitarian.org/rss.xml"
    feed = feedparser.parse(feed_url)
    return [{"title": entry.title, "link": entry.link} for entry in feed.entries[:5]]
