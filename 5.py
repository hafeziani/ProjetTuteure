# An example to call an API to get price of bitcoin in dollar
# inform user if the price is less than a defined value
import requests


my_good_price = 4500

response = requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD')
print(response.text)
print(response.json())
print(response.json()['data'])

price = float(response.json()['data']['amount'])

def inform_hafez():
    print('Hi there, the price is good')

if (price < my_good_price):
    inform_hafez()
else:
    print('Sorry at this moment, bitcoin is %i dollars' %float(response.json()['data']['amount']))
