import pandas as pd
import sqlite3 as sql
from st_csv_dl import us_ac, us_tc
from state_pops import st_pops
from st_csv_dl import peaks, dpeaks

cc_pm = {} # initialize current case data dictionary

# populate dictionary with normalize total case data
for i in us_tc:
    cc_pm[i] = us_tc[i]/st_pops[i]

# create pandas DataFrames of each states total cases, active cases, peak and date of peak
tot_c = pd.DataFrame(list(cc_pm.items()), columns = ['State', 'Current Total Cases'])
cur_i = pd.DataFrame(list(us_ac.items()), columns = ['State', 'Current 7 Day Average Per Million'])
peak = pd.DataFrame(list(peaks.items()), columns = ['State', 'Peak'])
dpeak = pd.DataFrame(list(dpeaks.items()), columns = ['State', 'Date of Peak'])

# merge all pandas DFs into one dataframe
current = pd.merge(tot_c, cur_i, on = 'State', how = 'left')
peak = pd.merge(peak, dpeak, on = 'State', how = 'left')
current = pd.merge(current, peak, on = 'State', how = 'left')

#Convert dataframe to SQL database table
conn = sql.connect('Covid.db')    
c = conn.cursor()

current.to_sql('US_Current_Stats', conn, if_exists = 'replace', index = False)

conn.close()