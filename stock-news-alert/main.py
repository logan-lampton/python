import requests
import sys
import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# import keys for security:
sys.path.insert(1, '//wsl$/Ubuntu/home/logan/Development/code/passwords')
import stock_news_alert_api


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stocks():
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
    change = ""
    if change_in_stock > 0:
        change = "🔺"
    else:
        change = "🔻"
    change_percent = round(change_in_stock / float(two_days_ago_stock["1. open"]), 2)
    # to tell if API call is working:
    stock_print = f"TSLA {change} {change_percent}%: ${round(change_in_stock, 2)}"
    print(stock_print)

    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    if change_percent >= five_percent:
        news_endpoint = "https://newsapi.org/v2/everything?"
        parameters = {
            "apiKey": stock_news_alert_api.keys("news_api"),
            "q": "Tesla"
        }
        news_response = requests.get(news_endpoint, params=parameters)
        news_response.raise_for_status()
        news_data = news_response.json()
        articles = news_data["articles"]
        unique_articles = {}
        for article in articles:
            source_name = article["source"]["name"]
            if source_name not in unique_articles:
                unique_articles[source_name] = article
        # Method to get the top 3 stories
        # Convert the dictionary to a list of tuples (source_name, article)
        article_list = list(unique_articles.items())
        # Print the first three elements (source_name, article) using slicing
        top_three_articles = article_list[:3]

        ## STEP 3: Use https://www.twilio.com
        # Send a separate message with the percentage change and each article's title and description to your phone number.
        account_sid = stock_news_alert_api.keys("twilio_account_sid")
        auth_token = stock_news_alert_api.keys("twilio_auth_token")
        client = Client(account_sid, auth_token)

        # format the message for twilio
        body = f"TSLA {change} {change_percent}%: ${round(change_in_stock, 2)}\n"
        for article in top_three_articles:
            outlet = article[0]
            headline = article[1]["title"]
            brief = article[1]["description"]

            body += f"{outlet} - Headline: {headline}\nBrief: {brief}\n",

        message = client.messages.create(
          from_=stock_news_alert_api.keys("twilio_number"),
          body=body,
          to=stock_news_alert_api.keys("my_number")
        )
        print(message.sid)


get_stocks()


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