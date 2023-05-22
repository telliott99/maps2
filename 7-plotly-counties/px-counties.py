import sys, json

print(sys.path)

d = '../data/'
fn = 'geojson-counties-fips.json'

with open(d+fn,'r') as fh:
    counties = json.load(fh)

#-------------------------------

# still working on how to do this w/o pandas

fn2 = 'example.csv'
import pandas as pd

# plotly wants a dataframe
# note:  dtype required for map to display correctly

df = pd.read_csv(fn2, dtype={'fips': str})
print (df.head())

'''
    fips  value
0  01001      1
1  06071      2
'''

# 06071 is the largest county in the US:  
# San Bernardino, CA

#-------------------------------
    
import plotly.express as px

cL = ['green','magenta']

fig = px.choropleth(
    df,
    geojson=counties,
    locations='fips',
    color=["Autauga","San Bernardino"],
    color_discrete_sequence=cL,
    scope='usa')
    
fig.show()

'''
county ids are really fips by another name

px uses locations
i.e. fips as the key into the data frame
to retrieve the value in the 'value' column

note:  w/o scope, it draws the whole world
'''