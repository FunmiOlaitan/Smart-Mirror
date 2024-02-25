from newsapi import NewsApiClient

class NewsData:
    def __init__(self, api_key):
        self.api_key = api_key
        self.newsapi = NewsApiClient(api_key = self.api_key)
    
    def fetch_news(self):
            top_headlines = self.newsapi.get_top_headlines(language='en' country='gb'):
            articles = top_headlines['articles']