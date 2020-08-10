from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
from state_pops import st_pops
import pandas as pd
import sqlite3 as sql

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def open_link(url, file_type = 'html'):
    #URL Bypass
    if file_type == 'html':
        soup_arg = 'html.parser'
    #Open URL, class = 'bytes'
    uh = urllib.request.urlopen(url, context = ctx).read() 
    #Parse using BS4, class = 'bs4.BeautifulSoup'
    data = BeautifulSoup(uh,soup_arg)
    return ET.fromstring(data.decode())


url = 'https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population_density'

# open link and convert to XML tree
pop_den = open_link(url)

#list of US territories and DC
terr = ['District of Columbia', 'Puerto Rico', 'Guam', 'US Virgin Islands', 'American Samoa', 'Northern Mariana Islands']

st_pop_dens = {}    # initialize a dictionary for population density values

tbody_tags = pop_den.findall('.//tbody')    # finding pop den table in XML tree

for tr in tbody_tags[0]:
    try:
        if tr[0][1].text not in terr:   # ignore territories of the US
            st_pop_dens[tr[0][1].text] = int(tr[3].text) # add pop densities to dictionary
    except:
        pass

# create pandas DataFrame of state populations
US_pop_data = pd.DataFrame(list(st_pops.items()),columns = ['State','Population'])

# convert from millions to total population
for i in US_pop_data.index:
    US_pop_data['Population'][i] = US_pop_data['Population'][i]*1000000

# create pandas DataFrame of state population densities 
us_pop_den = pd.DataFrame(list(st_pop_dens.items()), columns = ['State', 'Pop Density (per mi^2)'])

# merge state pop dataframes
US_pop_data = pd.merge(US_pop_data, us_pop_den, on = 'State', how = 'left')

# convert Pandas dataframe to sql table
conn = sql.connect('Covid.db')    
c = conn.cursor()
US_pop_data.to_sql('US_POP_DATA', conn, if_exists = 'replace', index = False)

conn.close()
