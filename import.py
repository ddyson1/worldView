import json
import pandas as pd
import matplotlib.pyplot as plt

from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.sectorperformance import SectorPerformances

from decouple import config
from pprint import pprint

key = config('ALPHA_VANTAGE_KEY')

fx = ForeignExchange(key='key')
sp = SectorPerformances(key='key')

fx_data, fx_meta = fx.get_currency_exchange_rate(from_currency='CNY',to_currency='USD')
sp_data, sp_meta = sp.get_sector()

with open('exchange_rate.json', 'w') as f:
    json.dump(fx_data, f, indent = 4, sort_keys = True)

sp_data['Rank A: Real-Time Performance'].plot(kind='bar')
plt.title('Real Time Performance (%) per Sector')
plt.tight_layout()
plt.savefig('plots/sectoral_performance.pdf')
