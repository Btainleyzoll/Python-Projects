import os
from dotenv import load_dotenv
from newsapi import NewsApiClient
#News provided by NewsAPI
#Weather data provided by OpenWeather
load_dotenv()
def get_news():
    categories = ["science", "technology", "sport", "business"]
    newsapi = NewsApiClient(api_key = os.getenv("NEWS_API_KEY"))
    top_headlines_business = newsapi.get_top_headlines(
                                          category='science',
                                          language='en',
                                          country='us',
                                          page_size=3)
    print("Top 3 science articles: ")
    for article in top_headlines_business['articles']:
        print(f"- {article['title']}: ({article['url']})")
        
    top_headlines_tech = newsapi.get_top_headlines(
                                        category='technology',
                                        language='en',
                                        country='us',
                                        page_size=3)
    print("\nTop 3 Tech articles: ")
    for article in top_headlines_tech['articles']:
        print(f"- {article['title']}: ({article['url']})")
        
    top_headlines_sport = newsapi.get_top_headlines(
                                        category='sports',
                                        language='en',
                                        country='us',
                                        page_size=3)
    print("\nTop 3 Sports articles: ")
    for article in top_headlines_sport['articles']:
        print(f"- {article['title']}: ({article['url']})")
    
        
        

    
    
get_news()
    