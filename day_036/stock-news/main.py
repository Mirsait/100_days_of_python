from twilio.rest import Client
import requests


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = ""

NEWSAPI_KEY = ""

TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""
PHONE_TO = ""
PHONE_FROM = ""


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and
# the day before yesterday then print("Get News").

def get_diff() -> (str, float):
    alpha_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": ALPHAVANTAGE_API_KEY
    }

    url = "https://www.alphavantage.co/query"
    response = requests.get(url, params=alpha_parameters)
    data_av = response.json()["Time Series (Daily)"]

    # with open(file='alphavantage.json', mode='w', encoding="utf-8") as outfile:
    #     json.dump(data_av, fp=outfile, ensure_ascii=False, indent=4)

    data_list = [value for (key, value) in data_av.items()][:2]
    date_list = list(data_av.keys())[:3]

    yesterday_data = float(data_list[0]["4. close"])
    before_yesterday_data = float(data_list[1]["4. close"])
    from_date = date_list[2]

    difference = (before_yesterday_data - yesterday_data) / yesterday_data * 100.0

    return (from_date, difference)


# STEP 2: Use https://newsapi.org
def get_top_3_news(news_date):
    news_api_url = "https://newsapi.org/v2/everything"
    news_parameters = {
        "q": COMPANY_NAME,
        "qInTitle": COMPANY_NAME,
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
# Send a seperate message with the percentage change and
# each article's title and description to your phone number.
def send_sms(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to=PHONE_TO,
        from_=PHONE_FROM,
        body=message
    )
    print(message.sid)


def format_message(difference, news_piece):
    icon = '↑' if difference > 0 else '↓'
    topic = f"{STOCK}: {icon}{abs(diff):.2f}%"
    headline = f"Headline: {news_piece[0]}"
    brief = f"Brief: {news_piece[1]}"
    return f"{topic}\n{headline}\n{brief}"


(news_from_date, diff) = get_diff()
if abs(diff) >= 5:
    top_3_news = get_top_3_news(news_from_date)
    for item in top_3_news:
        sms_text = format_message(diff, item)
        send_sms(sms_text)
