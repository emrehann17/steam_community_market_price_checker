import requests
from bs4 import BeautifulSoup
import time
import schedule

item_url= "https://steamcommunity.com/market/listings/730/AK-47%20%7C%20Frontside%20Misty%20%28Field-Tested%29"

def get_prices(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    price_spans = soup.find_all("span", class_ = "market_listing_price market_listing_price_with_fee")
    price_list= []
    for span in price_spans:
        text = span.text.strip()
        if text and not text.startswith("Sold"):
            price_list.append(text)
        if len(price_list) >= 3:
            break

    return price_list

def job():
    prices = get_prices(item_url)
    for p in prices:
        print(p)

job()
