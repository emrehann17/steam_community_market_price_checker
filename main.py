import requests
from bs4 import BeautifulSoup
import time
import schedule

item_url= "https://steamcommunity.com/market/listings/730/AK-47%20%7C%20Frontside%20Misty%20%28Field-Tested%29"

def get_prices(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
def job():
    prices = get_prices(item_url)
    print("Minimum price: ", prices)

# İlk çalıştırma
job()
