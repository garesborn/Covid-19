from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from name_conv import name_conv
import ssl

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

url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population_density'

# open URL as XML tree
pop_den = open_link(url)

table_tags = pop_den.findall('.//table') # find pop dens table in XML tree

euro_ct = ['Albania',
 'Andorra',
 'Austria',
 'Belarus',
 'Belgium',
 'Bosnia and Herzegovina',
 'Bulgaria',
 'Croatia',
 'Czech Republic',
 'Denmark',
 'Estonia',
 'Finland',
 'France',
 'Germany',
 'Greece',
 'Hungary',
 'Iceland',
 'Ireland',
 'Italy',
 'Latvia',
 'Liechtenstein',
 'Lithuania',
 'Luxembourg',
 'Malta',
 'Monaco',
 'Montenegro',
 'Netherlands',
 'Norway',
 'Poland',
 'Portugal',
 'Romania',
 'Russia',
 'San Marino',
 'Serbia',
 'Slovakia',
 'Slovenia',
 'Spain',
 'Sweden',
 'Switzerland',
 'Ukraine',
 'United Kingdom']

world_pd = {} # initialize dictionary for worlds population densities

for tr in table_tags[0][0][2:]:
    try:
        # NOTE: first command will sort out non-countries from the dictionary
        rnk = int(tr[0].text)
        pd = float(tr[6].text.replace(',', '')) # must remove commas from pd string to convert to float
        #print(name_conv(tr[1][1].text))
        world_pd[name_conv(tr[1][1].text)] = pd # populate dictionary
    except:
        pass


euro_pd = {} #initialize dictionary for just european Pop densities

# iterate though world PDs
for i in euro_ct:
    # populate european PDs if country is in list of European Nations
    euro_pd[i] = world_pd[i]