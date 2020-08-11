
import pandas as pd

key = '9a647676da68c9fc6a53b11e6c26db8f3712d02a'

# working to get structure like https://data.census.gov/cedsci/table?q=disability&g=0100000US.04000.001&hidePreview=false&tid=ACSST1Y2018.S1810&t=Disability&vintage=2018

# from https://api.census.gov/data/2016/acs/acsse/groups/K201803/
# K201803_005E = Total Cognitive Disability
# K201803_005M = Margin of error

# the below is just 2018
df = pd.read_json('https://api.census.gov/data/2018/acs/acsse?get=NAME,K201803_005E,K201803_005M&for=state:*&key={0}'.format(key))

#drop the first row
df = df.drop([0])

df.columns = ['State','With_Cog_Disability_Est','With_Cog_Disability_MarginError','State_ID']
df = df.sort_values(by='State')
print(df)

print(df.columns)


print('done')