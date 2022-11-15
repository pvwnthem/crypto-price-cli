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

    namesQuery = tr.find_all('a', href=True, class_='cmc-link')

    for name in namesQuery:
        names.append(name["href"])
    for coin in coinsQuery:
        coins.append(coin.text)
    
    for crypto in cryptoQuery: 
        coins.append(crypto.text)
    

for name in names:
    index = names.index(name)
    if names[index].__contains__("market") or names[index].__contains__("period"):
      
        names[index] = "not-valid"

def remove_items(test_list, item):
 
    # using list comprehension to perform the task
    res = [i for i in test_list if i != item]
 
    return res
 

def resolveSymbol(symbol):
    res = remove_items(names, "not-valid")

    index = coins.index(symbol)
    return res[index]

