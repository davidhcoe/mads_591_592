import requests
import pandas as pd

key = '9a647676da68c9fc6a53b11e6c26db8f3712d02a'

df = pd.read_json('https://api.census.gov/data/2018/pep/population?get=POP&for=COUNTY:*&key={0}'.format(key))

print(df)