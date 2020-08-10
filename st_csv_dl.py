import pandas as pd
import sqlite3 as sql
from state_pops import st_pops

#Open csv and convert to Pandas DF sorted by state and date
url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
st_df = pd.read_csv(url)
st_df = st_df.sort_values(by=['state', 'date']).reset_index(drop=True)

#list of state populations in millions
st_pops = {'Alabama': 4.903185,
 'Alaska': 0.731545,
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
 'Utah': 3.205958,
 'Vermont': 0.623989,
 'Virgin Islands': 0.106235,
 'Virginia': 8.535519,
 'Washington': 7.614893,
 'West Virginia': 1.792147,
 'Wisconsin': 5.822434,
 'Wyoming': 0.578759}

state = []
nc = []
us_ac = {}
us_tc = {}
codes = {}
dmin = st_df['date'][1]
dmax = dmin


#  Iterate through state data
for i in st_df.index:
#------------------------------------------------------------------------------
#                   Convert Total Cases to New Daily Cases
#------------------------------------------------------------------------------
    try:
        #Append current elements state value to state list
        state.append(st_df['state'][i])
        #If adjacent data points are from the same state
        if st_df['state'][i] == st_df['state'][i-1]:
            #append the difference between current and previous date (new cases that day) to nc list
            nc.append(int(st_df['cases'][i]-st_df['cases'][i-1]))

        #When data is from a new state
        else:
            #Append 1st data point for that state as new cases on day 1
            nc.append(int(st_df['cases'][i]))

    #NOTE: try/except used to ignore 1st instance in list where [i-1] cannot be performed
    except:
        nc.append(int(st_df['cases'][i]))
#------------------------------------------------------------------------------
#                 Find min and max dates for plot range
#------------------------------------------------------------------------------
    try:
        # if beginning of data set for new state
        # and data is from date before current minimum date
        if st_df['state'][i] != st_df['state'][i-1] and st_df['date'][i] < dmin:
            # replace min date
            dmin = st_df['date'][i]
    except:
        # min date already set to first date in table
        pass
    try:
        # if last date entry in current state data set
        # and entry is from date later than current max
        # NOTE: all state data sets should have same max date (in case datasets are incomplete)
        if st_df['state'][i] != st_df['state'][i+1] and st_df['date'][i] > dmax:
            dmax = st_df['date'][i]
    except:
        if st_df['date'][i] > dmax:
            dmax = st_df['date'][i]
    #add unique state codes into codes dictionary
    if st_df['fips'][i] not in codes:
        codes[st_df['fips'][i]]=[st_df['state'][i]]

#  Create new cases DF      
nc_df = pd.DataFrame({'state': state, 'date': st_df['date'],'New Cases': nc})

#  head is a variable to represent the 7 in 7 day average, 
#  but was also used in debugging hence the need for its flexibility
head = 7

av7 = []
tot7 = []
drange = [dmin, dmax]

# Iterate through alphabetically organized states in st_pops dictionary
for i in st_pops:
    peak = 0
#------------------------------------------------------------------------------
#                Convert New Daily Cases to 7 Day Average
#------------------------------------------------------------------------------
    #create temporary dataframe for current state
    temp_df = nc_df.loc[nc_df['state'] == i]
    temp_df = temp_df.reset_index(drop = True)
    # Iterate through data in temp df to create 7 day av
    for j in temp_df.index:
        # ignore data until we have 7 days to average
        if j-7 < 0:
            tot7.append(None)
            av7.append(None)
        else:
            # total last 7 days of cases
            rtot = sum(temp_df['New Cases'][j-7:j])
            # divide 7 day total by 7 days and by st population (in millions)
            av = sum(temp_df['New Cases'][j-7:j])/(7*st_pops[i])
            #append 7 day average per million
            av7.append(av)
            # append 7 day total
            tot7.append(rtot)
            #Note: if-statement used for debugging and to provide context to order of operations
            #if j == head:
                #print(i)
                #print('Pop:', st_pops[i])
                #print(temp_df['New Cases'][j-7:j])
                #print('Total:', rtot)
                #print('Tot type', type(rtot))
                #print("7 day av", av)

#Confirm that length of lists matches
#print(len(nc))
#print(len(av7))

# Create new DF with 7 day average
av_df = pd.DataFrame({'state': state, 'date': st_df['date'], '7 Day total': tot7,'7 Day Average': av7})

#------------------------------------------------------------------------------
#                           Find peak for state
#------------------------------------------------------------------------------
peaks = {}
dpeaks = {}
for i in st_pops:
    temp_df = av_df.loc[av_df['state'] == i]
    temp_df = temp_df.reset_index(drop = True)
    peak = 0
    dpeak = None
    for j in temp_df.index:
        if temp_df['7 Day Average'][j] > peak:
            peak = temp_df['7 Day Average'][j]
            dpeak = temp_df['date'][j]
    peaks[i] = peak
    dpeaks[i] = dpeak


# merge new cases and 7 day av  data to existing state DF
st_df = pd.merge(st_df, nc_df, on = ['state','date'], how = 'left')  
st_df = pd.merge(st_df, av_df, on = ['state','date'], how = 'left') 

# iterate through DF
for i in st_df.index:
    # try/except used to ignore last data point where [i+1] cannot be performed
    try:
        # if datapoint is last of given state
        if st_df['state'][i] != st_df['state'][i+1]:
            # add current 7 day av
            us_ac[st_df['state'][i]]= st_df['7 Day Average'][i]
            # add total cases to date
            us_tc[st_df['state'][i]]= st_df['cases'][i]/st_pops[st_df['state'][i]]
        else:
            pass
    except:
        # add current 7 day av
        us_ac[st_df['state'][i]]= st_df['7 Day Average'][i]
        # add total cases to date
        us_tc[st_df['state'][i]]= st_df['cases'][i]/st_pops[st_df['state'][i]]


#Convert dataframe to SQL database table
conn = sql.connect('Covid.db')    
c = conn.cursor()
st_df.to_sql('US_DATA', conn, if_exists = 'replace', index = False)

conn.close()

