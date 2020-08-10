from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import pandas as pd
from name_conv import name_conv
import sqlite3 as sql
from world_pop_den import euro_pd

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

clist = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria',
         'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 
         'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 
         'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of',
         'Congo, Republic of', 'Cook Islands', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 
         'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 
         'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 
         'Guinea', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iraq', 'Ireland', 'Israel', 'Italy', 
         'Jamaica', 'Japan', 'Jordan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Kosovo', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 
         'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 
         'Mauritania', 'Mauritius', 'Mexico', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Namibia', 'Nauru', 'Nepal', 
         'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'North Korea', 'Norway', 'Oman', 'Pakistan', 
         'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Romania', 
         'Russia', 'Rwanda', 'Saint Lucia', 'Samoa', 'San Marino', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 
         'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 
         'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Thailand', 'Togo', 'Tonga', 
         'Tunisia', 'Turkey', 'Turkmenistan', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 
         'Uzbekistan', 'Vanuatu', 'Venezuela', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']


url9 = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'

poptree = open_link(url9)   # open URL as XML tree

tbody_tags = poptree.findall('.//tbody') # find population table in XML tree

pcountries = []
cont = []
pops = []

for tr in tbody_tags[3]:
    if tr[0].tag == 'th':   # ignore headings
        continue
    if name_conv(tr[0][0].get('data-sort-value')) in clist: # test to see if entry is a country
        # some locations indexes werent the countries name and needed to be converted
        name = name_conv(tr[0][0].get('data-sort-value')) 
        pcountries.append(name_conv(name))
        pop = tr[4].text
        pop = pop.replace(',','')
        pops.append(int(pop))
        cont.append(tr[1][0].text)


eu_pop = {} #initialize a dictionary of just european populations

# iterate through world continent data
for i in range(len(cont)):
    if cont[i] == 'Europe':
        # populate only european countries
        eu_pop[pcountries[i]] = pops[i]

# create pandas DataFrame for european population
euro_pops = pd.DataFrame(eu_pop.items(), columns = ['Country', 'Population']) 
# create pandas DataFrame for european population density
pds = pd.DataFrame(euro_pd.items(), columns = ['Country', 'Pop Density (per mi^2)'])  
# merge european population density data
euro_pops = pd.merge(euro_pops, pds, on = 'Country', how = 'left')

# convert pandas DF to sql table
if __name__ == '__main__':    
    conn = sql.connect('Covid.db')    
    c = conn.cursor()
    try:
        c.execute('DROP TABLE EURO_POP_DATA;')
    except:
        pass
    euro_pops.to_sql('EURO_POP_DATA', conn, if_exists = 'replace', index = False)
    conn.close()