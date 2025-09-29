This Folder contains small automation projects, which can be run autonomously and is meant to help in everyday life. Each Project is standalone but all with the goal in mind to automate boring/repetitive tasks and make daily life easier.

## Projects

### 1. Daily Summary Bot for News, Weather and Stocks sent to email.

This bot was made to send me an email every morning (11:00am) and evening (9:00pm).
The content of the email includes:
- **News Headlines** (Top categories from NewsAPI)
- **Weather** (Current + tomorrow's forecast from OpenWeatherAPI)
- **Stock Prices** (Top winners and losers and closing prices)

#### How it works
- Uses the Task scheduler on Windows or cron for Linux/Mac to run the script at set times.
- Gathers data from:
  - [NewsAPI](https://newsapi.org/) for headlines
  - [OpenWeather](https://openweathermap.org/) for weather
  - [Yahoo Finance](https://pypi.org/project/yfinance/) for stock data
- Sends results via **Gmail SMTP** 

#### Setup
1. Clone repo

2. Install dependencies:
'''bash
pip install -r requirements.txt
3. Create .env file:
NEWS_API_KEY=your_newsapi_key
WEATHER_API_KEY=your_openweather_key
EMAIL=youremail@gmail.com
EMAIL_PASS=your_app_password
4. Change the recipient email 
5. Automate:
Use Task Scheduler for windows or add it cron job for Linux/Mac to run script at certain times.
