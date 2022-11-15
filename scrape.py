import requests
from bs4 import BeautifulSoup
from resolveSymbol import resolveSymbol
import sys
from getPrice import getPrice
baseurl = "https://coinmarketcap.com"

res =requests.get("https://coinmarketcap.com/currencies/ethereum")

print(sys.argv[1].upper())

html = res.text

soup = BeautifulSoup(html, 'html.parser')

price = soup.find('div', class_="priceValue")

#for span in price.find_all('span'):
    #print(span.text)



print(getPrice(resolveSymbol(str(sys.argv[1].upper()))))
