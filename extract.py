import json
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

with open('data/real_gdp.json', 'r') as f:
    real_gdp = json.load(f)

with open('data/real_gdp_per_capita.json', 'r') as f:
    real_gdp_per_capita = json.load(f)

with open('data/yield_10yr.json', 'r') as f:
    yield_10yr = json.load(f)

print(type(real_gdp['data'][0]['date']))
print(type(float(real_gdp['data'][0]['value'])))

print(real_gdp['data'][0]['date'])
print(float(real_gdp['data'][0]['value']))

'''
def getRGDP():
    dates, values = [], []
    for i in real_gdp['data']:
        dates += [real_gdp['data'][i]['date']]
        values += [float(real_gdp['data'][i]['value'])]
    return dates, values

dates, values = getRGDP()
d = {'dates': dates, 'values': values}

df = pd.DataFrame(data=d)
print(df)
'''
