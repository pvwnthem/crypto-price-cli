import requests
from bs4 import BeautifulSoup
from resolveSymbol import resolveSymbol
import sys
baseurl = "https://coinmarketcap.com"


def getPrice(url):
    res =requests.get("https://coinmarketcap.com"+url)
    soup = BeautifulSoup(res.text, 'html.parser')
    price = soup.find('div', class_="priceValue")
    return price.text