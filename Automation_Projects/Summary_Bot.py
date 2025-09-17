import os
from dotenv import load_dotenv
from newsapi import NewsApiClient
import requests
from datetime import datetime
#News provided by NewsAPI
#Weather data provided by OpenWeather
load_dotenv()
def get_news():
    categories = ["science", "technology", "sports", "business"]
    newsapi = NewsApiClient(api_key = os.getenv("NEWS_API_KEY"))
    
    for cat in categories:
        top_headlines = newsapi.get_top_headlines(
                                          category=cat,
                                          language='en',
                                          country='us',
                                          page_size=3)
    
        print(f"\n Top 3 {cat.capitalize()} articles: ")
        for article in top_headlines["articles"]:
            print(f"- {article['title']}: ({article['url']})")
    
    
    
    
def get_weather(city = "london"):
    today = datetime.now().date()
    mins = []
    maxs = []
    url = "http://api.openweathermap.org/data/2.5/weather"
    url_forecast = "http://api.openweathermap.org/data/2.5/forecast"
    params = {"q": city, "appid": os.getenv("WEATHER_API_KEY"), "units": "metric"}
    response = requests.get(url, params=params)
    response_forecast = requests.get(url_forecast, params=params)
    info = response.json()
    info_forecast = response_forecast.json()
    
    if response.status_code == 200 and response_forecast.status_code == 200:
        description = info["weather"][0]["description"]
        temp = info["main"]["temp"]
        
        for entry in info_forecast["list"]:
            dates = datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S").date()
            if dates == today:
                mins.append(entry["main"]["temp_min"])
                maxs.append(entry["main"]["temp_max"])
        if mins and maxs:
            min_temp = min(mins)
            max_temp = max(maxs)
        else:
            min_temp = "NA"
            max_temp = "NA"
        print(f"Weather in {city}: {description}, {temp} Celsius")
        print(f"The low for today is {min_temp} Celsius and the high is {max_temp} Celsius.")
    else: 
        print("Error:", info)

town = input("What city do you want the weather for? ")   
get_weather(town)
    
