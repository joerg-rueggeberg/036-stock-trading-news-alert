import os
import requests

STOCK = "TWTR"
COMPANY_NAME = "Twitter Inc."
STOCK_API_KEY = os.environ["api_alpha_vantage"]


def check_stock():
    """ Gets Stock Data from API and checks if the stock gained or lost equal or bigger to 5/-5. If so returns Value"""
    # ------------------------------- STOCK -------------------------------
    p = {
        "symbol": STOCK,
        "datatype": "json",
        "apikey": STOCK_API_KEY
    }

    response = requests.get(url="https://www.alphavantage.co/query?function=GLOBAL_QUOTE", params=p)
    response.raise_for_status()

    # ------------------------------- DATA -------------------------------
    data = response.json()
    stock_percent = round(float(data["Global Quote"]['10. change percent'].split("%")[0]), 2)

    if stock_percent >= 5:
        return f"{STOCK}: 🔺{stock_percent}%"
    elif stock_percent <= -5:
        return f"{STOCK}: 🔻{stock_percent}%"
    else:
        return False
