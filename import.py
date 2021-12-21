import json

from decouple import config
from pprint import pprint
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

key = config('ALPHA_VANTAGE_KEY')

session = Session()

url = 'https://www.alphavantage.co/query?function=REAL_GDP&interval=annual&apikey=' + key

try:
    response = session.get(url)
    data = json.loads(response.text)
    with open('data/real_gdp.json', 'w') as f:
        json.dump(data, f, indent = 4)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

url = 'https://www.alphavantage.co/query?function=REAL_GDP_PER_CAPITA&apikey=demo' + key
session = Session()

try:
    response = session.get(url)
    data = json.loads(response.text)
    with open('data/real_gdp_per_capita.json', 'w') as f:
        json.dump(data, f, indent = 4)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

url = 'https://www.alphavantage.co/query?function=TREASURY_YIELD&interval=monthly&maturity=10year&apikey=' + key
session = Session()

try:
    response = session.get(url)
    data = json.loads(response.text)
    with open('data/yield_10yr.json', 'w') as f:
        json.dump(data, f, indent = 4)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
