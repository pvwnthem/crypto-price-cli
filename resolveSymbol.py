import requests
from bs4 import BeautifulSoup

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

res = requests.get('https://coinmarketcap.com/currencies/')

soup = BeautifulSoup(res.text, 'html.parser')

tbody = soup.find('tbody')

trs = tbody.find_all('tr')

coins = []
names = []
for tr in trs:
    coinsQuery = tr.find_all('p', class_='coin-item-symbol')
    cryptoQuery = tr.find_all('span', class_='crypto-symbol')

    namesQuery = tr.find_all('a', href=True, class_='cmc-link')

    for name in namesQuery:
        names.append(name["href"])
    for coin in coinsQuery:
        coins.append(coin.text)
    
    for crypto in cryptoQuery: 
        coins.append(crypto.text)
    

for name in names:
    print(names.index(name))


