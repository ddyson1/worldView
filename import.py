import json # standard package for working with json format

from requests import Request, Session # requests packages used to import the coinmarketcap data
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects # for exception errors

from alpha_vantage.cryptocurrencies import CryptoCurrencies # package used to import the alphavantage data

from decouple import config # package used to easily secure and retrieve the API key from an .env file

key_1 = config('ALPHA_VANTAGE_KEY')
# importing the API keys from .env file using the decouple package
key_2 = config('X-CMC_PRO_API_KEY')
# X-CMC_PRO_API_KEY is set in the .env file as the actual API KEY\

cc = CryptoCurrencies(key_1)
# creates a vaiable 'cc' to pull data from the alphavantage API
ether_data, eth_meta_data = cc.get_digital_currency_daily(symbol='ETH', market='USD')
# stores Ethereum data in a variable named data, meta_data included as well
bitcoin_data, btc_meta_data = cc.get_digital_currency_daily(symbol='BTC', market='USD')
# stores Bitcoin data in a variable named bitcoin_data, btc_meta_data included too

with open('data/ethereum.json', 'w') as f:
    # creates a file named 'ethereum.json' and opens it for writing...
    json.dump(ether_data, f, indent = 4, sort_keys=True)
    # overwrites 'ethereum.json' with 'data', cleans up a bit

with open('data/bitcoin.json', 'w') as f:
    # creates a file named 'bitcoin.json' and opens it for writing...
    json.dump(bitcoin_data, f, indent = 4, sort_keys=True)
    # overwrites 'bitcoin.json' with 'bitcoin_data', cleans up a bit

url = 'https://pro-API.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# coinmarketcap API pulls data from the folling url
parameters = {
# setting parameters for the coinmarketcap API request...
  'start':'1',
  'limit':'5000',
  # gets first 5000 data items
  'convert':'USD'
  # handles price data in USD equivalents
}

headers = {
# in order to obtain the data the API must be passed through the url...
  'Accepts': 'application/json',
  # retrieves json formatted data...
  'X-CMC_PRO_API_KEY': key_2,
  # and obtains key from config file as stored in vaiable 'key_2'
}

session = Session()
# instantiates requests.Session() as 'session'
session.headers.update(headers)
# calls the requests.Session() function with updated headers to make the request

try:
# setup error handling using 'try'
    response = session.get(url, params=parameters)
    # sets up the varible 'response' to make a call to requests.Session().get()...
    # using the url and parameters specified
    data = json.loads(response.text)
    # converts response.text into a json format named 'data'
    with open('data/coinmarketcap.json', 'w') as f:
    # creates a file named 'coinmarketcap.json' and opens it for writing...
        json.dump(data, f, indent = 4, sort_keys = True)
        # overwrites 'coinmarketcap.json' with 'data', cleans up a bit
except (ConnectionError, Timeout, TooManyRedirects) as e:
# latter part of 'try:'
    print(e)
    # print out the respective error message from requests.exceptions as 'e'
