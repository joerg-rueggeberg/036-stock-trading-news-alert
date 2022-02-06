import os
import requests

NEWS_API_KEY = os.environ["api_newsapi"]


def get_news():
    """Gets the top 3 news for Topic 'q' and returns a list with news entries."""
    p = {
        "apiKey": NEWS_API_KEY,
        "q": "Twitter",
        "pageSize": 3,
    }

    response = requests.get(url="https://newsapi.org/v2/top-headlines", params=p)
    response.raise_for_status()

    data = response.json()
    data_news = data["articles"]

    news = []
    for i in data_news:
        entry = i["title"], i["description"], i["url"]
        news.append(entry)
    return news
