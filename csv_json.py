import pandas as pd

import json

df =pd.read_csv('https://raw.githubusercontent.com/davidhcoe/mads_591_592/master/data/NBER/cbsa2fipsxw.csv')

j = df.to_json()

with open('nber.json','w') as file:
    file.write(j)