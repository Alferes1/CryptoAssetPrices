'''
dependencies:
requests
beautifulsoup4 (bs4)
Crypto currencies values by CoinMarketCap (https://coinmarketcap.com/)
'''

import os
import datetime
import requests
from bs4 import *

now = datetime.datetime.now()
year = '{:02d}'.format(now.year)
month = '{:02d}'.format(now.month)
day = '{:02d}'.format(now.day)
hour = '{:02d}'.format(now.hour)
minute = '{:02d}'.format(now.minute)
day_month_year = '{}-{}-{}'.format(year, month, day)
hour_minute = '{}:{}'.format(hour, minute)


print('Crypto Currencies Values - github.com/Alferes1')
print('Date: ' + day_month_year + ' | ' + hour_minute)
print()


btc = "https://coinmarketcap.com/currencies/bitcoin/"
btcHtml = requests.get(btc)

soup = BeautifulSoup(btcHtml.text, 'html.parser')

result = soup.find_all("div", {"class":"priceValue"})

for res in result:
    print("BTC", res.text)

#

eth = "https://coinmarketcap.com/currencies/ethereum/"
ethHtml = requests.get(eth)

soup = BeautifulSoup(ethHtml.text, 'html.parser')

result = soup.find_all("div", {"class":"priceValue"})

for res in result:
    print("ETH", res.text)

#

ltc = "https://coinmarketcap.com/currencies/litecoin/"
ltcHtml = requests.get(ltc)

soup = BeautifulSoup(ltcHtml.text, 'html.parser')

result = soup.find_all("div", {"class":"priceValue"})

for res in result:
    print("LTC", res.text)

#

xmr = "https://coinmarketcap.com/currencies/monero/"
xmrHtml = requests.get(xmr)

soup = BeautifulSoup(xmrHtml.text, 'html.parser')

result = soup.find_all("div", {"class":"priceValue"})

for res in result:
    print("XMR", res.text)

#

bch = "https://coinmarketcap.com/currencies/bitcoin-cash/"
bchHtml = requests.get(bch)

soup = BeautifulSoup(bchHtml.text, 'html.parser')

result = soup.find_all("div", {"class":"priceValue"})

for res in result:
    print("BCH", res.text)

#

usdc = "https://coinmarketcap.com/currencies/usd-coin/"
usdcHtml = requests.get(usdc)

soup = BeautifulSoup(usdcHtml.text, 'html.parser')

result = soup.find_all("div", {"class":"priceValue"})

for res in result:
    print("USDC", res.text)

#

doge = "https://coinmarketcap.com/currencies/dogecoin/"
dogeHtml = requests.get(bch)

soup = BeautifulSoup(dogeHtml.text, 'html.parser')

result = soup.find_all("div", {"class":"priceValue"})

for res in result:
    print("DOGE", res.text)

#

usdt = "https://coinmarketcap.com/currencies/tether/"
usdtHtml = requests.get(usdt)

soup = BeautifulSoup(usdtHtml.text, 'html.parser')

result = soup.find_all("div", {"class":"priceValue"})

for res in result:
    print("USDT", res.text)

#

ada = "https://coinmarketcap.com/currencies/cardano/"
adaHtml = requests.get(ada)

soup = BeautifulSoup(adaHtml.text, 'html.parser')

result = soup.find_all("div", {"class":"priceValue"})

for res in result:
    print("ADA", res.text)

#

etc = "https://coinmarketcap.com/currencies/ethereum-classic/"
etcHtml = requests.get(etc)

soup = BeautifulSoup(etcHtml.text, 'html.parser')

result = soup.find_all("div", {"class":"priceValue"})

for res in result:
    print("ETC", res.text)

#

bnb = "https://coinmarketcap.com/currencies/binance-coin/"
bnbHtml = requests.get(bnb)

soup = BeautifulSoup(bnbHtml.text, 'html.parser')

result = soup.find_all("div", {"class":"priceValue"})

for res in result:
    print("BNB", res.text)

#

bat = "https://coinmarketcap.com/currencies/basic-attention-token/"
batHtml = requests.get(bat)

soup = BeautifulSoup(batHtml.text, 'html.parser')

result = soup.find_all("div", {"class":"priceValue"})

for res in result:
    print("BAT", res.text)

#

trx = "https://coinmarketcap.com/currencies/tron/"
trxHtml = requests.get(trx)

soup = BeautifulSoup(trxHtml.text, 'html.parser')

result = soup.find_all("div", {"class":"priceValue"})

for res in result:
    print("TRX", res.text)

#

cake = "https://coinmarketcap.com/currencies/pancakeswap/"
cakeHtml = requests.get(cake)

soup = BeautifulSoup(cakeHtml.text, 'html.parser')

result = soup.find_all("div", {"class":"priceValue"})

for res in result:
    print("CAKE", res.text)

#

shib = "https://coinmarketcap.com/currencies/shiba-inu/"
shibHtml = requests.get(shib)

soup = BeautifulSoup(shibHtml.text, 'html.parser')

result = soup.find_all("div", {"class":"priceValue"})

for res in result:
    print("SHIB", res.text)

#

busd = "https://coinmarketcap.com/currencies/binance-usd/"
busdHtml = requests.get(busd)

soup = BeautifulSoup(busdHtml.text, 'html.parser')

result = soup.find_all("div", {"class":"priceValue"})

for res in result:
    print("BUSD", res.text)
    
os.system("PAUSE")
