import os
from dotenv import load_dotenv
from newsapi import NewsApiClient
import requests
from datetime import datetime, timedelta
import yfinance as yf
import time
import schedule
import pandas as pd
import smtplib
from email.mime.text import MIMEText
#News provided by NewsAPI
#Weather data provided by OpenWeather
load_dotenv()
def get_news(mode):
    summary = ""
    if mode == "morning":
        categories = ["general", "health", "business"]
        newsapi1 = NewsApiClient(api_key = os.getenv("NEWS_API_KEY"))
        
        for cat in categories:
            top_headlines = newsapi1.get_top_headlines(
                                            category=cat,
                                            language='en',
                                            country='us',
                                            page_size=3)
            summary += f"\n Top 3 {cat.capitalize()} articles from overnight:\n "
            for article in top_headlines["articles"]:
                summary+=f"- {article['title']}: ({article['url']})\n"
            summary+="\n\n"
                
    elif mode == "evening":
        categories = ["general", "technology", "sports", "science", "business"]
        newsapi2 = NewsApiClient(api_key = os.getenv("NEWS_API_KEY"))
        
        for cat in categories:
            top_headlines = newsapi2.get_top_headlines(
                                            category=cat,
                                            language='en',
                                            country='us',
                                            page_size=3)
            summary+=f"\n Top {cat.capitalize()} articles from today: \n"
            for article in top_headlines["articles"]:
                summary+=f"- {article['title']}: ({article['url']})\n"
                summary+="\n\n"
    
    return summary
                

    
    
    
    
def get_weather(mode = "morning", city = "london"):
    summary = ""
    mins = []
    maxs = []
    rain_chance = 0
    today = datetime.now().date()
    tomorrow = datetime.now().date() + timedelta(days=1)
    url = "http://api.openweathermap.org/data/2.5/weather"
    url_forecast = "http://api.openweathermap.org/data/2.5/forecast"
    params = {"q": city, "appid": os.getenv("WEATHER_API_KEY"), "units": "metric"}
    response = requests.get(url, params=params)
    response_forecast = requests.get(url_forecast, params=params)
    info = response.json()
    info_forecast = response_forecast.json()
    if mode == "morning":  
        
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
            summary+=f"Weather in {city}: {description}, {temp:.00f} Celsius\n"
            summary+=f"The low for today is {min_temp:.00f} Celsius and the high is {max_temp:.00f} Celsius.\n"
            summary+=f"The chance of rain today is {rain_chance}%\n\n"
        else: 
            summary+="Error:\n\n", info
    elif mode == "evening":
        if response.status_code == 200 and response_forecast.status_code == 200:
            temp = info["main"]["temp"]
            
            for entry in info_forecast["list"]:
                dates = datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S").date()
                if dates == tomorrow:
                    rain_chance = entry.get("pop", 0) * 100
                    mins.append(entry["main"]["temp_min"])
                    maxs.append(entry["main"]["temp_max"])
            if mins and maxs:
                min_temp = min(mins)
                max_temp = max(maxs)
            else:
                min_temp = "NA"
                max_temp = "NA"
            summary+=f"The current weather in {city} is {temp} Celsius.\n"
            summary+=f"The low for tomorrow is expected to be {min_temp:.00f} Celsius and the high to be {max_temp:.00f} Celsius.\n"
            summary+=f"The chance of rain tomorrow shows {rain_chance}%\n\n"
        else: 
            summary+="Error:\n\n", info
    return summary    
        

def get_stocks(mode):
    tickers = ["AAPL", "NVDA", "TSLA", "MSFT", "AMZN", "META" ]
    summary = ""
    if mode == "morning":
        data1 = yf.download(tickers, period = "2d", interval = "1d", auto_adjust=True)["Close"]
        latest_data1 = data1.tail(1)
        
        summary+="Latest closing stock prices:\n"
        for ticker in tickers:
            price = latest_data1[ticker].values[0]
            summary+=f"{ticker}: ${price:.2f}\n"
        summary+="\n\n"
            
            
    elif mode == "evening":
        data2 = yf.download(tickers, period="1d", interval="1d", auto_adjust=True)["Close"]
        latest_data2 = data2.tail(1)
        try:
            change = data2.iloc[-1] - data2.iloc[-2]
            percent_change = (change / data1.iloc[-2]) * 100
            
            biggest_winner = percent_change.sort_values(ascending=False).head(3)
            biggest_loser = percent_change.sort_values(ascending=True).head(3)
            
            summary+="Top 3 Gainers in the stock market today:\n"
            for ticker, change in biggest_winner.items():
                price = data2.iloc[-1][ticker]
                summary+=f"{ticker}: {percent_change:.2f}% (Closing price: {price:.2f})\n"
            summary+="\n\n"
                
            summary+="Top 3 Losers in the stock market today:\n"
            for ticker, change in biggest_loser.items():
                price = data2.iloc[-1][ticker]
                summary+=f"{ticker}: {percent_change:.2f}% (Closing price: {price:.2f})\n"
            summary+="\n\n"
        except IndexError:
            summary+="Not enough data for calculation\n\n"
            
        summary+="Latest Closing stock prices:\n"
        for ticker in tickers:
            price = latest_data2[ticker].values[0]
            summary+=f"{ticker}: ${price:.2f}\n"
        summary+="\n\n"
            
    return summary
            
def send_email(summary):
    msg = MIMEText(summary)
    msg["Subject"] = "Daily Summary Bot"
    msg["From"] = "bainleyzoll@gmail.com"       
    msg["To"] = "bfishman02@gmail.com"
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(os.getenv("EMAIL"),os.getenv("EMAIL_PASS"))
        server.send_message(msg)
        print("Done")
    
    
def run_morning(): 
    town = "hatfield"
    summary = ""
    summary+=get_weather(mode = "morning", city=town)
    summary+="\n\n"
    summary+=get_news(mode = "morning")
    summary+="\n\n"
    summary+=get_stocks(mode = "morning")
    send_email(summary)
    
def run_evening():
    town = "hatfield"
    summary = ""
    summary+=get_weather(mode = "evening", city=town)
    summary+="\n\n"
    summary+=get_news(mode = "evening")
    summary+="\n\n"
    summary+=get_stocks(mode = "evening")
    send_email(summary)
    
schedule.every().day.at("11:00"). do(run_morning)
schedule.every().day.at("21:00").do(run_evening)

while True:
    schedule.run_pending()
    time.sleep(60)
    
