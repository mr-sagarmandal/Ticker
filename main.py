import json
from win10toast import ToastNotifier
import urllib.request


def set_tickers():
    tickers = []
    while True:
        ticker = input('Set Ticker. Current Tickets are {}. '.format(','.join(tickers)))
        if ticker == '0':
            break
        else:
            tickers.append(ticker)
    return tickers


def set_prices(tickers, current_prices):
    prices = []
    for i in range(0, len(tickers)):
        price = input('Set threshold for ticker:{}. Current Price is {}:'.format(tickers[i], current_prices[i]))
        prices.append(float(price))
    return prices


def check_prices(tickers, key):
    url =  'https://www.alphavantage.co/query?function=BATCH_QUOTES_US&symbols={}&apikey={}'
    ticker_string = ','.join(tickers)
    final_url = url.format(ticker_string, key)
    with urllib.request.urlopen(final_url) as url:
        data = json.loads(url.read().decode())
        print(data)


def set_key():
    key = input("Please Input your Alpha_Vantage Key: ")
    return key


if __name__ == "__main__":
    key = set_key()
    tickers = set_tickers()
    curr_prices = check_prices(tickers, key)
    #set_prices(tickers, curr_prices)