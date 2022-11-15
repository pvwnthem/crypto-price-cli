import requests
from bs4 import BeautifulSoup

res =requests.get("https://coinmarketcap.com/currencies/ethereum")


html = res.text

soup = BeautifulSoup(html, 'html.parser')

price = soup.find('div', class_="priceValue")

for span in price.find_all('span'):
    print(span.text)
