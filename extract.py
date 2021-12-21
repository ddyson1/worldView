import json
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")
sns.set_style("dark")

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

df = pd.DataFrame(data={'date': dates, 'USD (billions)': values})
df = df.iloc[::-1]
df.reset_index(drop=True, inplace=True)
df = df.set_index(pd.DatetimeIndex(df['date']))
print(df)

sns.lineplot(data=df)
plt.savefig('plots/realgdp.png')
