import os
from dotenv import load_dotenv
from newsapi import NewsApiClient
import requests
from datetime import datetime
import yfinance as yf
import pandas as pd
#News provided by NewsAPI
#Weather data provided by OpenWeather
load_dotenv()
def get_news(mode):
    if mode == "morning":
        categories = ["general", "health", "business"]
        newsapi1 = NewsApiClient(api_key = os.getenv("NEWS_API_KEY"))
        
        for cat in categories:
            top_headlines = newsapi1.get_top_headlines(
                                            category=cat,
                                            language='en',
                                            country='us',
                                            page_size=3)
        
            print(f"\n Top 3 {cat.capitalize()} articles from overnight: ")
            for article in top_headlines["articles"]:
                print(f"- {article['title']}: ({article['url']})")
                
    if mode == "evening":
        categories = ["general", "technology", "sports", "science", "business"]
        newsapi2 = NewsApiClient(api_key = os.getenv("NEWS_API_KEY"))
        
        for cat in categories:
            top_headlines = newsapi2.get_top_headlines(
                                            category=cat,
                                            language='en',
                                            country='us',
                                            page_size=3)
            print(f"\n Top 3 {cat.capitalize()} articles from today: ")
            for article in top_headlines["articles"]:
                print(f"- {article['title']}: ({article['url']})")
    
    
    
    
def get_weather(mode, city = "london"):
    if mode == "morning":
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
                    rain_chance = entry.get("pop", 0) * 100
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
            print(f"The chance of rain today is {rain_chance}%")
        else: 
            print("Error:", info)
        

def get_stocks(mode):
    if mode == "morning":
        tickers = ["AAPL", "NVDA", "TSLA", "MSFT", "AMZN", "META" ]
        data = yf.download(tickers, period = "1d", interval = "1h")["Close"]
        latest_data = data.tail(1)
        
        print("Latest closing stock prices:")
        for ticker in tickers:
            price = latest_data[ticker].values[0]
            print(f"{ticker}: ${price:.2f}")
    if mode == "evening":
        

mode = "morning"
town = input("What city do you want the weather for? ")   
get_weather(mode, town)
print("\n\n")
get_news(mode)
print("\n\n")
get_stocks(mode)
    
