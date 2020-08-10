from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
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

#open link as XML tree
pops = open_link('https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population')

st_pops = {}    # initialize state population dictionary

tbody_tags = pops.findall('.//tbody') # find population table in XML tree

for tr in tbody_tags[0]:
    try:
        if tr[2][1].text is not None: # when None means instance is territory not state
            pop = tr[3].text.replace(",","")
            st_pops[tr[2][1].text] = int(pop) # populate dictionary
    except:
        pass

# final product
st_pops = {'Alabama': 4.903185,
 'Alaska': 0.731545,
 'American Samoa': 0.049437,
 'Arizona': 7.278717,
 'Arkansas': 3.017804,
 'California': 39.512223,
 'Colorado': 5.758736,
 'Connecticut': 3.565287,
 'Delaware': 0.973764,
 'District of Columbia': 0.705749,
 'Florida': 21.477737,
 'Georgia': 10.617423,
 'Guam': 0.168485,
 'Hawaii': 1.415872,
 'Idaho': 1.787065,
 'Illinois': 12.671821,
 'Indiana': 6.732219,
 'Iowa': 3.15507,
 'Kansas': 2.913314,
 'Kentucky': 4.467673,
 'Louisiana': 4.648794,
 'Maine': 1.344212,
 'Maryland': 6.04568,
 'Massachusetts': 6.892503,
 'Michigan': 9.986857,
 'Minnesota': 5.639632,
 'Mississippi': 2.976149,
 'Missouri': 6.137428,
 'Montana': 1.068778,
 'Nebraska': 1.934408,
 'Nevada': 3.080156,
 'New Hampshire': 1.359711,
 'New Jersey': 8.88219,
 'New Mexico': 2.096829,
 'New York': 19.453561,
 'North Carolina': 10.488084,
 'North Dakota': 0.762062,
 'Northern Mariana Islands': 0.051433,
 'Ohio': 11.6891,
 'Oklahoma': 3.956971,
 'Oregon': 4.217737,
 'Pennsylvania': 12.801989,
 'Puerto Rico': 3.193694,
 'Rhode Island': 1.059361,
 'South Carolina': 5.148714,
 'South Dakota': 0.884659,
 'Tennessee': 6.829174,
 'Texas': 28.995881,
 'Virgin Islands': 0.106235,
 'Utah': 3.205958,
 'Vermont': 0.623989,
 'Virgin Islands': 0.106235,
 'Virginia': 8.535519,
 'Washington': 7.614893,
 'West Virginia': 1.792147,
 'Wisconsin': 5.822434,
 'Wyoming': 0.578759}

