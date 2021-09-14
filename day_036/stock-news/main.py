from twilio.rest import Client
import json
import requests
from datetime import datetime, timedelta


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = ""

NEWSAPI_KEY = ""

TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""
PHONE_TO = ""
PHONE_FROM = ""


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_diff():
    alpha_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": ALPHAVANTAGE_API_KEY
    }

    url = "https://www.alphavantage.co/query"
    response = requests.get(url, params=alpha_parameters)
    data_av = response.json()

    # with open(file='alphavantage.json', mode='w', encoding="utf-8") as outfile:
    #     json.dump(data_av, fp=outfile, ensure_ascii=False, indent=4)

    if datetime.today().weekday() == 0:
        yesterday1 = (datetime.today() - timedelta(days=3)).date().isoformat()
        yesterday2 = (datetime.today() - timedelta(days=4)).date().isoformat()
    elif datetime.today().weekday() == 1:
        yesterday1 = (datetime.today() - timedelta(days=1)).date().isoformat()
        yesterday2 = (datetime.today() - timedelta(days=4)).date().isoformat()
    else:
        yesterday1 = (datetime.today() - timedelta(days=1)).date().isoformat()
        yesterday2 = (datetime.today() - timedelta(days=2)).date().isoformat()

    data1 = data_av["Time Series (Daily)"][str(yesterday1)]
    data2 = data_av["Time Series (Daily)"][str(yesterday2)]
    close1 = float(data1["4. close"])
    close2 = float(data2["4. close"])

    diff = (close2 - close1)/close2 * 100.0
    return (yesterday2, diff)


# STEP 2: Use https://newsapi.org
def get_top_3_news(news_date):
    news_api_url = "https://newsapi.org/v2/everything"
    news_parameters = {
        "q": "tesla",
        "from": news_date,
        "sortBy": "publishedAt",
        "language": "en",
        "apiKey": NEWSAPI_KEY
    }
    response = requests.get(news_api_url, news_parameters)
    data_news = response.json()

    top_3 = [(item["title"], item["description"])
             for item in data_news["articles"][:3]]

    # with open(file='news.json', mode='w', encoding="utf-8") as outfile:
    #     json.dump(data_news, fp=outfile, ensure_ascii=False, indent=4)
    return top_3


# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
def send_sms(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to = PHONE_TO,
        from_ = PHONE_FROM,
        body = message
    )
    print(message.sid)


def format_message(diff, news_piece):
    icon = '↑' if diff > 0 else '↓'
    topic = f"{STOCK}: {icon}{abs(diff):.2f}%"
    headline = f"Headline: {news_piece[0]}"
    brief = f"Brief: {news_piece[1]}"
    return f"{topic}\n{headline}\n{brief}"


(yesterday2, diff) = get_diff()
if abs(diff) >= 5:
    top_3 = get_top_3_news(yesterday2)
    for item in top_3:
        sms_text = format_message(diff, item)
        send_sms(sms_text)
