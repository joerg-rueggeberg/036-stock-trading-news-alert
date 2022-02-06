from stock import check_stock
from news import get_news
from mail import send_mail

stock_percent = check_stock()

if stock_percent:
    news = get_news()
    send_mail(stock_percent, news)
else:
    print("No special course development!")
