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

def getGDP():

    dates, values = [], []

    for i in real_gdp['data']:
        dates += [str(i['date'])]
        values += [float(i['value'])]

    return dates, values

dates, values = getGDP()


d = {'date': dates, 'USD (billions)': values}
df = pd.DataFrame(data=d)

pd.to_datetime(df['date'], format='%Y/%m/%d')
df = df.set_index(pd.DatetimeIndex(df['date']))

df.drop(columns=['date'])
df = df.iloc[::-1]

print(df)

'''
df.plot()
plt.show()
'''
