import json # standard package for working with json

with open('data/ethereum.json', 'r') as f:
    # opens the ethereum.json for reading
    ether_data = json.load(f)
    # stores data from json in 'ether_data'

with open('data/bitcoin.json', 'r') as f:
    # opens the bitcoin.json for reading
    bitcoin_data = json.load(f)
    # stores data from json in 'bitcoin_data'

with open('data/coinmarketcap.json', 'r') as f:
    # opens the coinmarketcap.json for reading
    cmc_data = json.load(f)
    # stores data from json in 'cmc_data'

class Wallet:
# creates the Wallet class
    def __init__(self, ether = 0, bitcoin = 0):
    # instantiates the wallet class with default values for ether (0) and bitcoin(0)
        self.__ether = float(ether)
        # __ether is a private variable, sets ether to a float type
        self.__bitcoin = float(bitcoin)
        # __bitcoin is a private variable, sets bitcoin to a float type
    def getEtherAmount(self):
    # creates a get method named 'getEtherAmount()'
        return self.__ether
        # calling this method retrieves amount of ether in object
    def getBitcoinAmount(self):
    # creates a get method named 'getBitcoinAmount()'
        return self.__bitcoin
        # calling this method retrieves amount of bitcoin in object
    def setEtherAmount(self, newEtherAmount):
    # creates a setter/mutator method to set new amount of ether
        self.__ether = newEtherAmount
        # sets the ether to new amount indicated in Wallet().setEtherAmount(float) call
    def setBitcoinAmount(self, newBitcoinAmount):
    # creates a setter/mutator method to set new amount of bitcoin
        self.__bitcoin = newBitcoinAmount
        # sets the bitcoin to new amount indicated in Wallet().setBitcoinAmount(float) call
    def getEtherBalance(self):
    # creates a get method named 'getEtherBalance()'
        return round(float(self.getEtherAmount() * getCMC()[1]['quote']['USD']['price']),2)
        # returns the ether amount multiplied by current USD price as retrived in extrapolate.getCMC()
    def getBitcoinBalance(self):
    # creates a get method named 'getBitcoinBalance()'
        return round(float(self.getBitcoinAmount() * getCMC()[0]['quote']['USD']['price']),2)
        # returns the bitcoin amount multiplied by current USD price as retrived in extrapolate.getCMC()
    def getTotalBalance(self):
    # creates a get method named 'getTotalBalance()'
        return self.getEtherBalance() + self.getBitcoinBalance()
        # returns the wallet balance (USD) by combining the ether and bitcoin balances

def getBitcoin():
# a function that retrieves the date and price from the 'bitcoin.json' and...
# indexes into the '4a. close (USD)' element to retrieve price data
    bitcoin_date, bitcoin_price = [], []
    # initializes two empty list which will hold the bitcoin date/price data
    for date in bitcoin_data:
    # using a for loop, iterating through all of the dictonary dates (keys) and retrieves...
    # '4a. close (USD)' to store in bitcoin_price
        bitcoin_date += [date]
        # stores the date in the bitcoin_date list
        bitcoin_price += [float(bitcoin_data[str(date)]['4a. close (USD)'])]
        # stores the '4a. close (USD)' in the 'bitcoin_price' list
    return bitcoin_date, bitcoin_price
    # function getBitcoin() will return listed values

def getEthereum():
# a function that takes specific data from the 'ethereum.json' and...
# indexes into certain elements to store them in named variables
    eth_date, openPrice, closePrice, dailyHigh, dailyLow, volume = [], [], [], [], [], []
    # initializes an empty list for variable names to be used in data exploration
    for date in ether_data:
    # using a for loop, iterating through all of the dictonary dates (keys) and retrieves...
    # their values by indexing into the ethereum.json, storing their data in respective empty list
        eth_date += [date]
        # stores the date in a list named eth_date
        openPrice += [float(ether_data[str(date)]['1a. open (USD)'])]
        # stores the '1a. open (USD)' in a list named openPrice
        closePrice += [float(ether_data[str(date)]['4a. close (USD)'])]
        # stores the '4a. close (USD)' in a list named closePrice
        dailyHigh += [float(ether_data[str(date)]['2a. high (USD)'])]
        # stores the '2a. high (USD)' in a list named dailyHigh
        dailyLow += [float(ether_data[str(date)]['3a. low (USD)'])]
        # stores the '3a. low (USD)' in a list named dailyLow
        volume += [round(float(ether_data[str(date)]['5. volume']))]
        # stores the '5. volume' in a list named volume
    return eth_date, openPrice, closePrice, dailyHigh, dailyLow, volume
    # function getEthereum() will return listed values

def getCMC():
# function that indexes past the first element in the cmc api named 'data'...
# iterates through all of the 5000 items pulled from the cmc api and stores them in
# an empty list named tokens
    tokens = []
    # initializes the empty list named tokens
    for token in range(len(cmc_data['data'])):
    # using a for loop goes through the cmc['data'] elements
        tokens += [cmc_data['data'][token]]
        # adds the token to the empty list named tokens
    return tokens
    # function call getCMC() will return the tokens

def cmcScreen():
# function that returns 'filtered/screened' data from the cmc api...
# uses a conditional 'if' statement to act as the filter
    pick, symbol, cost, day_change, multiple, mcap = [], [], [], [], [], []
    # creates multiple empty lists which will be used to store the filtered data
    for i in range(len(cmc_data['data'])):
    # iterate through all of the tokens
        if cmc_data['data'][i]['quote']['USD']['market_cap'] > 1000000000 and \
           cmc_data['data'][i]['quote']['USD']['percent_change_7d'] > 20:
           # only retrieve tokens if market cap is over 1 billion, and whose 24 hour...
           # percent change has exceeded 100% or 2x their value from 24 hours ago
            pick += [cmc_data['data'][i]['name']]
            # stores the token 'name' in a list named pick
            symbol += [cmc_data['data'][i]['symbol']]
            # stores the token 'symbol' in a list named symbol
            cost += [round(cmc_data['data'][i]['quote']['USD']['price'],8)]
            # stores the token 'price' in a list named cost, rounds to 8 decimals (0.00000001 = 1 satoshi)
            day_change += [cmc_data['data'][i]['quote']['USD']['percent_change_7d']]
            # stores the token 'percent_change_7d' in a list named day_change
            multiple += [round(cmc_data['data'][i]['quote']['USD']['percent_change_7d']/100,2)]
            # takes the day_change and divides by 100 to get multiple, rounded to 2 decimals
            mcap += [round(cmc_data['data'][i]['quote']['USD']['market_cap'])]
            # stores the token 'market_cap' in a list named mcap
    return pick, symbol, cost, day_change, multiple, mcap
    # returns the filtered data in their respective list names
