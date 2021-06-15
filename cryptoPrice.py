import requests
import cryptocompare
import pprint
def bitcoin():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    print(data["bpi"]["USD"]["rate"])

#response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
price = cryptocompare.get_price('ETH', currency = 'USD')['ETH'] 
pprint.pprint(price['USD'])

Namelist = cryptocompare.get_coin_list(format=True)

for name in Namelist:
    if name == 'SAFEMOON':
        print('yep')
