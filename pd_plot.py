from world_pop_den import euro_pd
from st_pop_den import st_pop_dens
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# dictionary of Population Densities of each location in dataset
pds = { 'San Marino': 1471.0,
 'New Jersey': 1218,
 'Netherlands': 1091.0,
 'Rhode Island': 1021,
 'Belgium': 973.0,
 'Massachusetts': 871,
 'Connecticut': 741,
 'United Kingdom': 725.0,
 'Liechtenstein': 621.0,
 'Maryland': 618,
 'Luxembourg': 615.0,
 'Germany': 603.0,
 'Switzerland': 539.0,
 'Italy': 518.0,
 'Delaware': 485,
 'Andorra': 425.0,
 'New York': 420,
 'Florida': 378,
 'Czech Republic': 351.0,
 'Denmark': 349.0,
 'France': 319.0,
 'Poland': 318.0,
 'Portugal': 289.0,
 'Slovakia': 288.0,
 'Pennsylvania': 286,
 'Ohio': 284,
 'Austria': 275.0,
 'Hungary': 272.0,
 'Slovenia': 266.0,
 'Albania': 258.0,
 'California': 251,
 'Spain': 240.0,
 'Serbia': 231.0,
 'Illinois': 231,
 'Hawaii': 222,
 'Virginia': 212,
 'Romania': 211.0,
 'Greece': 210.0,
 'North Carolina': 206,
 'Croatia': 187.0,
 'Indiana': 184,
 'Ireland': 181.0,
 'Ukraine': 180.0,
 'Bosnia and Herzegovina': 178.0,
 'Georgia': 177,
 'Michigan': 175,
 'Bulgaria': 162.0,
 'South Carolina': 162,
 'Tennessee': 160,
 'New Hampshire': 148,
 'Belarus': 118.0,
 'Montenegro': 117.0,
 'Kentucky': 112,
 'Lithuania': 111.0,
 'Louisiana': 108,
 'Washington': 107,
 'Wisconsin': 106,
 'Texas': 105,
 'Alabama': 95,
 'United States': 94,
 'Missouri': 88,
 'Europe': 87,
 'Latvia': 77.0,
 'Estonia': 76.0,
 'West Virginia': 76,
 'Minnesota': 68,
 'Vermont': 67,
 'Mississippi': 63,
 'Arizona': 60,
 'Sweden': 59.0,
 'Arkansas': 57,
 'Oklahoma': 57,
 'Iowa': 55,
 'Colorado': 52,
 'Norway': 43.0,
 'Maine': 43,
 'Finland': 42.0,
 'Oregon': 41,
 'Utah': 36,
 'Kansas': 36,
 'Nevada': 26,
 'Nebraska': 24,
 'Russia': 22.0,
 'Idaho': 20,
 'New Mexico': 17,
 'South Dakota': 11,
 'North Dakota': 10,
 'Iceland': 9.2,
 'Montana': 7,
 'Wyoming': 6,
 'Alaska': 1}

# list of European countries
europe = ['Albania',
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

# list of American States
us = ['New Jersey',
 'Rhode Island',
 'Massachusetts',
 'Connecticut',
 'Maryland',
 'Delaware',
 'New York',
 'Florida',
 'Pennsylvania',
 'Ohio',
 'California',
 'Illinois',
 'Hawaii',
 'Virginia',
 'North Carolina',
 'Indiana',
 'Georgia',
 'Michigan',
 'South Carolina',
 'Tennessee',
 'New Hampshire',
 'Kentucky',
 'Louisiana',
 'Washington',
 'Wisconsin',
 'Texas',
 'Alabama',
 'Missouri',
 'West Virginia',
 'Minnesota',
 'Vermont',
 'Mississippi',
 'Arizona',
 'Arkansas',
 'Oklahoma',
 'Iowa',
 'Colorado',
 'Maine',
 'Oregon',
 'Utah',
 'Kansas',
 'Nevada',
 'Nebraska',
 'Idaho',
 'New Mexico',
 'South Dakota',
 'North Dakota',
 'Montana',
 'Wyoming',
 'Alaska']

# dictionary of Populations of each location in dataset
pops = {'Europe': 741400000,
 'United States': 328000000,
 'Russia': 145872256,
 'Germany': 83517045,
 'United Kingdom': 67530172,
 'France': 65129728,
 'Italy': 60550075,
 'Spain': 46736776,
 'Ukraine': 43993638,
 'California': 39512223,
 'Poland': 37887768,
 'Texas': 28995881,
 'Florida': 21477737,
 'New York': 19453561,
 'Romania': 19364557,
 'Netherlands': 17097130,
 'Pennsylvania': 12801989,
 'Illinois': 12671821,
 'Ohio': 11689100,
 'Belgium': 11539328,
 'Czech Republic': 10689209,
 'Georgia': 10617423,
 'North Carolina': 10488084,
 'Greece': 10473455,
 'Portugal': 10226187,
 'Sweden': 10036379,
 'Michigan': 9986857,
 'Hungary': 9684679,
 'Belarus': 9452411,
 'Austria': 8955102,
 'New Jersey': 8882190,
 'Serbia': 8772235,
 'Switzerland': 8591365,
 'Virginia': 8535519,
 'Washington': 7614893,
 'Arizona': 7278717,
 'Bulgaria': 7000119,
 'Massachusetts': 6892503,
 'Tennessee': 6829174,
 'Indiana': 6732219,
 'Missouri': 6137428,
 'Maryland': 6045680,
 'Wisconsin': 5822434,
 'Denmark': 5771876,
 'Colorado': 5758736,
 'Minnesota': 5639632,
 'Finland': 5532156,
 'Slovakia': 5457013,
 'Norway': 5378857,
 'South Carolina': 5148714,
 'Alabama': 4903185,
 'Ireland': 4882495,
 'Louisiana': 4648794,
 'Kentucky': 4467673,
 'Oregon': 4217737,
 'Croatia': 4130304,
 'Oklahoma': 3956971,
 'Connecticut': 3565287,
 'Bosnia and Herzegovina': 3301000,
 'Utah': 3205958,
 'Iowa': 3155070,
 'Nevada': 3080156,
 'Arkansas': 3017804,
 'Mississippi': 2976149,
 'Kansas': 2913314,
 'Albania': 2880917,
 'Lithuania': 2759627,
 'New Mexico': 2096829,
 'Slovenia': 2078654,
 'Nebraska': 1934408,
 'Latvia': 1906743,
 'West Virginia': 1792147,
 'Idaho': 1787065,
 'Hawaii': 1415872,
 'New Hampshire': 1359711,
 'Maine': 1344212,
 'Estonia': 1325648,
 'Montana': 1068778,
 'Rhode Island': 1059361,
 'Delaware': 973764,
 'South Dakota': 884659,
 'North Dakota': 762062,
 'Alaska': 731545,
 'Montenegro': 627987,
 'Vermont': 623989,
 'Luxembourg': 615729,
 'Wyoming': 578759,
 'Iceland': 339031,
 'Andorra': 77142,
 'Liechtenstein': 38019,
 'San Marino': 33860}



#==============================================================================
#       Plotting Bar graph of Pop Density of EU Countries and US States
#==============================================================================
# initialize lists to be populated
patches = []
cts = []
pd = []
cols = []

# y positions of bars will just be the index each location is in our PD dict
y_pos = np.arange(len(pds))

# iterate through dataset in order of Population density
for i in pds:
    cts.append(i)       #add countries to list of countries
    pd.append(pds[i])   # add corresponding population density to PD list
    # to color code our bars we add a color corresponding to location to cols list
    if i in europe:
        cols.append('blue')     # European Countries in blue
    elif i in us:
        cols.append('red')      # American States in red
    else:
        cols.append('black')    # European and US averages in black

# append patches to a list to create a legend
patches.append(mpatches.Patch(color = 'blue', label = 'Europe'))        
patches.append(mpatches.Patch(color = 'red', label = 'United States'))
patches.append(mpatches.Patch(color = 'black', label = 'Averages'))

# Resize plot
fig = plt.gcf()
fig.set_size_inches(6, 16, forward=True)

# create labels at the end of each bar to show numerical value
ax = plt.gca()
# iterate through population densities to be the text of our labels
for i in range(len(pd)):
    # each label will be 5 to the right of the end of the bar
    # y position needed to be slightly adjusted for fit
    ax.text(x = pd[i] + 5, y = y_pos[i] - .3, s = pd[i])

# replace y axis tick labels with the name of each location    
plt.yticks(y_pos, cts)
# adjust x and y scales for readability
plt.xlim(0, 1700)
plt.ylim(-1,91.5)
# create title and axis labels
plt.xlabel('Population Density (People per mi^2)')
plt.title('Population Density of European Countries and US States')
# create legend using previously declared patches 
plt.legend(handles = patches)
# create bar chart
plt.barh(y_pos, pd, color = cols)    
plt.show()

#==============================================================================
#                 Plotting Pops of EU Countries and US States
#==============================================================================
# reinitialize lists to clear them
cts = []
pop = []
cols = []

# iterate through locations in order of population
for i in pops:
    # ignore totals
    if i not in ('Europe', 'United States'):
        # add countries and corresponding populations to their respective lists
        cts.append(i)
        pop.append(pops[i])
        # to color code our bars we add a color corresponding to location to cols list
        if i in europe:
            cols.append('blue')     # European Countries in blue
        elif i in us:
            cols.append('red')      # American States in red  

# y positions of bars will just be the index each location is in our pop dict
y_pos = np.arange(len(pop))

#resize graphs
fig = plt.gcf()
fig.set_size_inches(8, 15, forward=True)

#create labels on bar graph of each population
ax = plt.gca()
# for each country in dataset
for i in range(len(pop)):
    # label with population 5 to the right of end of bar
    # y pos needs slight adjustment for readability
    ax.text(x = pop[i] + 5, y = y_pos[i] - .3, s = pop[i])

# replace y tick labels with countries
plt.yticks(y_pos, cts)
# adjust axis ranges for readability
plt.xlim(0, 170000000)
plt.ylim(-1,93)
# create axis labels and title
plt.xlabel('Population')
plt.title('Population of European Countries and US States')
# create legend using same list of patches for first graph, excluding last patch
plt.legend(handles = patches[:2])
# create bar chart
plt.barh(y_pos, pop, color = cols)  