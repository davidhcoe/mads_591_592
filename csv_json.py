import pandas as pd

import json

df =pd.read_csv('https://raw.githubusercontent.com/davidhcoe/mads_591_592/master/data/NBER/cbsa2fipsxw.csv')

j = df.to_json(orient='records')

with open('nber2.json','w') as file:
    file.write(j)

#df2 = pd.read_json('https://raw.githubusercontent.com/davidhcoe/mads_591_592/master/data/NBER/cbsa2fipsxw.json')

df2 = pd.read_json(j)

print(df.iloc[3])
print('---')
print(df2.iloc[3])