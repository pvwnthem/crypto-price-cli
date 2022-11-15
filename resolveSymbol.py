import requests
from bs4 import BeautifulSoup

res = requests.get('https://coinmarketcap.com/currencies/')

soup = BeautifulSoup(res.text, 'html.parser')

tbody = soup.find('tbody')

trs = tbody.find_all('tr')

coins = []
names = []
for tr in trs:
    coinsQuery = tr.find_all('p', class_='coin-item-symbol')
    cryptoQuery = tr.find_all('span', class_='crypto-symbol')
    for coin in coinsQuery:
        coins.append(coin.text)
    
    for crypto in cryptoQuery: 
        coins.append(crypto.text)
    

print(coins)



for tr in trs: