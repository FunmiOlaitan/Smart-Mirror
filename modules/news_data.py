from newsapi import NewsApiClient

class NewsData:
    def __init__(self, api_key):
        self.api_key = api_key
        self.newsapi = NewsApiClient(api_key = self.api_key)
    
    def fetch_news(self):
        try:
            # Fetch top headlines for the United Kingdom
            top_headlines = self.newsapi.get_top_headlines(language='en', country='gb')
            articles = top_headlines['articles']
            # Extract title and description from articles
            news_list = []
            for article in articles:
                title = article['title']
                description = article['description']
                news_list.append({'Title': title, 'Description': description})
            return news_list
        except Exception as e:
            print(f"Error fetching news data: {e}")
            return None
        