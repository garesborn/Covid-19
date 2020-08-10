from world_csv_dl import euro
from st_csv_dl import st_df, drange, peaks
from eu_us_avs import eu, us
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
import time
from datetime import datetime, date, time, timedelta

# list of European countries
euro_lst = ['Albania','Andorra','Austria','Belarus','Belgium','Bosnia and Herzegovina',
      'Bulgaria','Croatia','Cyprus','Czech Republic','Denmark','Estonia',
      'Finland','France','Germany','Greece', 'Hungary','Iceland',
      'Ireland','Italy','Jersey','Kosovo','Latvia','Liechtenstein','Lithuania',
      'Luxembourg','Macedonia','Malta','Moldova','Monaco','Montenegro','Netherlands',
      'Norway','Poland','Portugal','Romania','Russia','Serbia',
      'Slovakia','Slovenia','Spain','Sweden','Switzerland','Ukraine','United Kingdom']

# list of American States
st = ['Alabama',
 'Alaska',
 'Arizona',
 'Arkansas',
 'California',
 'Colorado',
 'Connecticut',
 'Delaware',
 'District of Columbia',
 'Florida',
 'Georgia',
 'Guam',
 'Hawaii',
 'Idaho',
 'Illinois',
 'Indiana',
 'Iowa',
 'Kansas',
 'Kentucky',
 'Louisiana',
 'Maine',
 'Maryland',
 'Massachusetts',
 'Michigan',
 'Minnesota',
 'Mississippi',
 'Missouri',
 'Montana',
 'Nebraska',
 'Nevada',
 'New Hampshire',
 'New Jersey',
 'New Mexico',
 'New York',
 'North Carolina',
 'North Dakota',
 'Northern Mariana Islands',
 'Ohio',
 'Oklahoma',
 'Oregon',
 'Pennsylvania',
 'Puerto Rico',
 'Rhode Island',
 'South Carolina',
 'South Dakota',
 'Tennessee',
 'Texas',
 'Utah',
 'Vermont',
 'Virgin Islands',
 'Virginia',
 'Washington',
 'West Virginia',
 'Wisconsin',
 'Wyoming']

# list of colors of American states' curves
st_col = {'Alabama': 'crimson',
 'Alaska': 'gray',
 'Arizona': 'brown',
 'Arkansas': 'gray',
 'California': 'teal',
 'Colorado': 'gray',
 'Connecticut': 'cornflowerblue',
 'Delaware': 'gray',
 'District of Columbia': 'gray',
 'Florida': 'black',
 'Georgia': 'goldenrod',
 'Guam': 'gray',
 'Hawaii': 'cyan',
 'Idaho': 'gray',
 'Illinois': 'gray',
 'Indiana': 'gray',
 'Iowa': 'gray',
 'Kansas': 'gray',
 'Kentucky': 'gray',
 'Louisiana': '#411900',
 'Maine': 'green',
 'Maryland': 'gray',
 'Massachusetts': 'steelblue',
 'Michigan': 'slateblue',
 'Minnesota': 'gray',
 'Mississippi': 'maroon',
 'Missouri': 'gray',
 'Montana': 'gray',
 'Nebraska': 'gray',
 'Nevada': 'darkorange',
 'New Hampshire': 'lime',
 'New Jersey': 'blue',
 'New Mexico': 'gray',
 'New York': 'deepskyblue',
 'North Carolina': 'gray',
 'North Dakota': 'gray',
 'Northern Mariana Islands': 'gray',
 'Ohio': 'gray',
 'Oklahoma': 'gray',
 'Oregon': 'gray',
 'Pennsylvania': 'indigo',
 'Puerto Rico': 'gray',
 'Rhode Island': 'yellow',
 'South Carolina': 'gold',
 'South Dakota': 'gray',
 'Tennessee': '#cd5909',
 'Texas': 'yellow',
 'Utah': 'gray',
 'Vermont': 'darkgreen',
 'Virgin Islands': 'gray',
 'Virginia': 'gray',
 'Washington': 'gray',
 'West Virginia': 'gray',
 'Wisconsin': 'gray',
 'Wyoming': 'gray'}

#list of 10 states with highest cases per million
cmax = ['Florida', 'Louisiana', 'Mississippi', 'Arizona', 'Alabama',
        'Tennessee','Nevada', 'Georgia', 'South Carolina', 'Texas']
#list of 10 states with lowest cases per million
cmin = ['Pennsylvania', 'Michigan', 'New Jersey', 'Massachusetts', 'Connecticut', 'New York',
        'Hawaii', 'New Hampshire', 'Maine', 'Vermont']

# list of European Countries in top and bottom 10 of current daily cases
euro_20 = {'Luxembourg': 123.92071428571428,
 'Montenegro': 92.80242857142858,
 'Bosnia and Herzegovina': 78.29071428571429,
 'Romania': 60.20185714285714,
 'Spain': 55.82928571428572,
 'Serbia': 48.49671428571428,
 'Belgium': 39.308714285714295,
 'Russia': 37.339857142857134,
 'Albania': 36.73457142857143,
 'Malta': 34.94271428571429,
 'Greece': 6.990285714285713,
 'Slovenia': 6.459142857142858,
 'Lithuania': 5.3,
 'Italy': 4.590714285714285,
 'Slovakia': 4.526714285714286,
 'Estonia': 4.523142857142857,
 'Norway': 3.979142857142857,
 'Latvia': 1.969142857142857,
 'Finland': 1.7531428571428571,
 'Hungary': 1.3015714285714286}

# list of colors for European Curves
colors = ['black',
 '#411900',
 'maroon',
 'brown',
 'crimson',
 '#cd5909',
 'darkorange',
 'goldenrod',
 'gold',
 'yellow',
 'indigo',
 'slateblue',
 'blue',
 'steelblue',
 'cornflowerblue',
 'deepskyblue',
 'cyan',
 'lime',
 'green',
 'darkgreen']



#==============================================================================
#                       Plotting European Covid Cases
#==============================================================================

#y max value for plots, Same for US plot
ymax = 600
# list of patches to create legend
epatches = []
 
plt.ylim(0,ymax)    # set y axis range
plt.title('Covid-19 Cases per Million of European Countries') # create title
plt.xlabel('Date')  # create x axis label
plt.ylabel('New Cases Per Million People')  # create y axis label

# initialize a count to iterate though curve colors
ct = 0
# initialize a rank count for legend
r = 1
# iterate through 20 european countries
for i in euro_20:
    # create temporary DataFrame for current country from european dataframe
    temp_df = euro.loc[euro['Country'] == i]
    # plot 7 day average vs time, use current color in list
    plt.plot(temp_df['Date'], temp_df['7 Day Average Per Million'], color = colors[ct])
    # increase count to iterate through curve colors
    ct = ct + 1

# add European average to plot as black dotted line
plt.plot(eu[0], eu[1], color = 'black', linestyle= '--')

# create list of patches to make legend
p = 0
# iterate through 20 countries
for i in euro_20:
    # label for current country is rank followed by name (ex: 33. Italy)
    elab = str(r) + '. ' + i
    epatches.append(mpatches.Patch(color = colors[p], label = elab))
    # p is used to iterate through colors
    p = p + 1
    # skip to r = 30 from r = 10
    if r != 10:
        r = r + 1
    else:
        r = 30

# notes for chart
txt = '''NOTES:
-Only Countries in the top
 and bottom 10 in current 
 cases are shown
 -European average denoted by
 dotted black line
 -New cases per million are 
 represented by a 7 Day
 average
 -Vatican and Malta were excluded
 from graph due to population size
 -Plot created using python
 package MatPlotLib'''

# text of sources
sources = '''COVID DATA: https://covid.ourworldindata.org/data/owid-covid-data.csv
EUROPEAN COUNTRY POPULATIONS: https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'''

fig = plt.gcf()
# create notes and source captions in specific locations 
fig.text(.91, .065, txt, ha='left')
fig.text(.5875, -.05, sources, ha='center')
# rotate date ticks for readability
plt.xticks(rotation=45)
ax = plt.gca()
# set x axis range
plt.xlim(55, drange[1])
labels = ax.get_xaxis().get_ticklabels()
# Set all labels to invisible
for j in labels:
    j.set_visible(False)
# Reset only every 20th label to visable
for j in labels[::20]:
    j.set_visible(True)
fig = plt.gcf()
# resize plot
fig.set_size_inches(10, 8, forward=True)
# create legend from list of patches
plt.legend(handles = epatches, bbox_to_anchor = (1.0075,.9875))

plt.show()

#==============================================================================
#                         Plotting US Covid Cases
#==============================================================================
plt.ylim(0,ymax) # set y axis range
plt.title('Covid-19 Cases per Million of US States')     # create title
plt.xlabel('Date')  # create x axis label
plt.ylabel('New Cases Per Million') # create y axis label
# initialize new list of patches for US tabl legend
patches = []

# iterate though all states
for i in st:
    # test to see if states are in top or bottom 10
    if i in cmax or i in cmin:
        # create temporary DF for states we want to plot
        temp_df = st_df.loc[st_df['state'] == i]
        # plot 7 day av versus time
        plt.plot(temp_df['date'], temp_df['7 Day Average'], color = st_col[i])
    else:
        continue

# plot US average as black dotted line
plt.plot(us[0],us[1], color = 'black', linestyle = ':')

# create legend labels
r = 1
q = 41
# if state in top 10 in active cases
for i in cmax:
    lab = str(r) + '. ' + i # EX label: 1. Florida
    # add patches to a list
    patches.append(mpatches.Patch(color = st_col[i], label = lab))
    # iterate through ranks
    r = r + 1
# if state in bottom 10 in cases
for i in cmin:
    lab = str(q) + '. ' + i # EX label: 1. Florida
    # add patches to existing list of US patches
    patches.append(mpatches.Patch(color = st_col[i], label = lab))
    # iterate through ranks, this could be done the same way done for Europe
    q = q + 1
    
txt = '''NOTES:
-Only States in the top
 and bottom 20% percentile
 are shown
 -US average denoted by
 dotted black line
 -New cases per million are 
 represented by a 7 Day
 average
 -Plot created using python
 package MatPlotLib'''

sources = '''COVID DATA: https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv
STATE POPULATIONS: https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population'''

fig = plt.gcf()
# set chart size
fig.set_size_inches(10, 8, forward=True)
# create text captions
fig.text(.91, .10, txt, ha='left')
fig.text(.5875, -.05, sources, ha='center')
# create legend using list of patches
plt.legend(handles = patches, bbox_to_anchor = (1.0075,.275))
ax = plt.gca()
# set x axis range
plt.xlim(0, drange[1])
# rotate x labels
plt.xticks(rotation=45)
labels = ax.get_xaxis().get_ticklabels()
# set all labels to invisible
for j in labels:
    j.set_visible(False)
# reset every 14th label to visible
for j in labels[::14]:
    j.set_visible(True)
plt.show()


