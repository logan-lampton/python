import requests
import sys
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# import keys for security:
sys.path.insert(1, '//wsl$/Ubuntu/home/logan/Development/code/passwords')
import stock_news_alert_api

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_endpoint = "https://www.alphavantage.co/query?"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": stock_news_alert_api.keys("alpha_vantage")
}

stock_response = requests.get(stock_endpoint, params=parameters)

stock_response.raise_for_status()

stock_data = stock_response.json()

# calculating the dates of yesterday and the day before yesterday
yesterday = datetime.date.today() - datetime.timedelta(days=1)
two_days_ago = yesterday - datetime.timedelta(days=1)

yesterday_stock = stock_data["Time Series (Daily)"][f"{yesterday}"]
two_days_ago_stock = stock_data["Time Series (Daily)"][f"{two_days_ago}"]

# 5% of initial stock two days ago
five_percent = float(two_days_ago_stock["1. open"]) * 0.05

# find change from two days ago to yesterday; multiply by -1, since two days ago would be a greater number if yesterday
# is less, and a negative number if yesterday is more than two days ago
change_in_stock = (float(two_days_ago_stock["1. open"]) - float(yesterday_stock["4. close"])) * -1

print(change_in_stock)

# if change_in_stock > five_percent:


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# news_endpoint = ""
#
# parameters = {
#
# }
#
# news_response = requests.get(news_endpoint, params=parameters)
# news_response.raise_for_status()
#
# news_data = news_response.json()

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""