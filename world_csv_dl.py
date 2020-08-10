import pandas as pd
import sqlite3 as sql
from world_pops import euro_pops as eu

#Open csv and convert to Pandas DF
url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
df = pd.read_csv(url)
#Show top 5 lines of DF
print(df.head())

response = ['Taiwan', 'South Korea', 'Singapore', 'New Zealand', 'Australia', 'Canada', 'Germany', 'Iceland',
            'United Arab Emirates', 'Greece', 'Argentina']

#List of European Countries
ct = ['Albania',
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

cts = ['Afghanistan',
 'Albania',
 'Algeria',
 'Andorra',
 'Angola',
 'Anguilla',
 'Antigua and Barbuda',
 'Argentina',
 'Armenia',
 'Aruba',
 'Australia',
 'Austria',
 'Azerbaijan',
 'Bahamas',
 'Bahrain',
 'Bangladesh',
 'Barbados',
 'Belarus',
 'Belgium',
 'Belize',
 'Benin',
 'Bermuda',
 'Bhutan',
 'Bolivia',
 'Bonaire Sint Eustatius and Saba',
 'Bosnia and Herzegovina',
 'Botswana',
 'Brazil',
 'British Virgin Islands',
 'Brunei',
 'Bulgaria',
 'Burkina Faso',
 'Burundi',
 'Cambodia',
 'Cameroon',
 'Canada',
 'Cape Verde',
 'Cayman Islands',
 'Central African Republic',
 'Chad',
 'Chile',
 'China',
 'Colombia',
 'Comoros',
 'Congo',
 'Costa Rica',
 "Cote d'Ivoire",
 'Croatia',
 'Cuba',
 'Curacao',
 'Cyprus',
 'Czech Republic',
 'Democratic Republic of Congo',
 'Denmark',
 'Djibouti',
 'Dominica',
 'Dominican Republic',
 'Ecuador',
 'Egypt',
 'El Salvador',
 'Equatorial Guinea',
 'Eritrea',
 'Estonia',
 'Ethiopia',
 'Faeroe Islands',
 'Falkland Islands',
 'Fiji',
 'Finland',
 'France',
 'French Polynesia',
 'Gabon',
 'Gambia',
 'Georgia',
 'Germany',
 'Ghana',
 'Gibraltar',
 'Greece',
 'Greenland',
 'Grenada',
 'Guam',
 'Guatemala',
 'Guernsey',
 'Guinea',
 'Guinea-Bissau',
 'Guyana',
 'Haiti',
 'Honduras',
 'Hong Kong',
 'Hungary',
 'Iceland',
 'India',
 'Indonesia',
 'International',
 'Iran',
 'Iraq',
 'Ireland',
 'Isle of Man',
 'Israel',
 'Italy',
 'Jamaica',
 'Japan',
 'Jersey',
 'Jordan',
 'Kazakhstan',
 'Kenya',
 'Kosovo',
 'Kuwait',
 'Kyrgyzstan',
 'Laos',
 'Latvia',
 'Lebanon',
 'Lesotho',
 'Liberia',
 'Libya',
 'Liechtenstein',
 'Lithuania',
 'Luxembourg',
 'Macedonia',
 'Madagascar',
 'Malawi',
 'Malaysia',
 'Maldives',
 'Mali',
 'Malta',
 'Mauritania',
 'Mauritius',
 'Mexico',
 'Moldova',
 'Monaco',
 'Mongolia',
 'Montenegro',
 'Montserrat',
 'Morocco',
 'Mozambique',
 'Myanmar',
 'Namibia',
 'Nepal',
 'Netherlands',
 'New Caledonia',
 'New Zealand',
 'Nicaragua',
 'Niger',
 'Nigeria',
 'Northern Mariana Islands',
 'Norway',
 'Oman',
 'Pakistan',
 'Palestine',
 'Panama',
 'Papua New Guinea',
 'Paraguay',
 'Peru',
 'Philippines',
 'Poland',
 'Portugal',
 'Puerto Rico',
 'Qatar',
 'Romania',
 'Russia',
 'Rwanda',
 'Saint Kitts and Nevis',
 'Saint Lucia',
 'Saint Vincent and the Grenadines',
 'San Marino',
 'Sao Tome and Principe',
 'Saudi Arabia',
 'Senegal',
 'Serbia',
 'Seychelles',
 'Sierra Leone',
 'Singapore',
 'Sint Maarten (Dutch part)',
 'Slovakia',
 'Slovenia',
 'Somalia',
 'South Africa',
 'South Korea',
 'South Sudan',
 'Spain',
 'Sri Lanka',
 'Sudan',
 'Suriname',
 'Swaziland',
 'Sweden',
 'Switzerland',
 'Syria',
 'Taiwan',
 'Tajikistan',
 'Tanzania',
 'Thailand',
 'Timor',
 'Togo',
 'Trinidad and Tobago',
 'Tunisia',
 'Turkey',
 'Turks and Caicos Islands',
 'Uganda',
 'Ukraine',
 'United Arab Emirates',
 'United Kingdom',
 'United States',
 'United States Virgin Islands',
 'Uruguay',
 'Uzbekistan',
 'Vatican',
 'Venezuela',
 'Vietnam',
 'Western Sahara',
 'World',
 'Yemen',
 'Zambia',
 'Zimbabwe']

euro_ct = []
euro_date = []
euro_ncases = []
euro_tcases = []
euro_ncpm = []
av7 = []
euro_av7 = []

exclusions = ('Vatican', 'San Marino', 'Faroe Islands', 'Gibraltar', 'Guernsey', 'Isle of Man', 'Jersey','Kosovo', 'Macedonia', 'Moldova')


#==============================================================================
#               Create data for 7 Day average for each country
#==============================================================================
df = df.sort_values(['location', 'date'])

#Parse through european countries (Vatican excluded)
for i in cts:
    #Create temporary DF for current country
    temp_df = df.loc[df['location'] == i]
    temp_df = temp_df.reset_index(drop = True)
    #Print to confirm
    #print(temp_df)
    #Iterate through DF 
    for j in temp_df.index:
        #ignore when there isn't a full week of data
        if j-7 < 0:
            av7.append(None)
        #Once there is a full week of data, find the 7 day average
        else:
            av7.append((sum(temp_df['new_cases_per_million'][j-7:j]))/7)

#---confirm the length of av7 list is the same as the existing df---
#print(len(euro))
#print(len(euro_av7))

#add new column to DF
df['7 Day Average Per Million'] = av7

#==============================================================================
#                   Create DataFrame for European Data
#==============================================================================

#Iterate through DF
for i in df.index:
    #Select only European Countries
    #(exclude the Vatican because per million metrics are outliers)
    if df['continent'][i] == 'Europe' and df['location'][i] in ct:
        #Append Country, Date of data, New cases per mil, and new cases to respective lists
        euro_ct.append(df['location'][i])
        euro_date.append(df['date'][i])
        euro_ncpm.append(df['new_cases_per_million'][i])
        euro_ncases.append(df['new_cases'][i])
        euro_tcases.append(df['total_cases'][i])
        euro_av7.append(df['7 Day Average Per Million'][i])

#Create DF from lists w/ exclusions        
euro = pd.DataFrame({'Country': euro_ct, 'Date': euro_date, 'Total Cases': euro_tcases, "New cases": euro_ncases,
                     'New Cases per Million': euro_ncpm, '7 Day Average Per Million': euro_av7})

#-----Create dictionary of Euro Country Pops-----
euro_pops = {}
for i in eu.index:
    euro_pops[eu['Country'][i]]= eu['Population'][i]


#------------------------------------------------------------------------------
#                  Find peak and current cases for Countries
#------------------------------------------------------------------------------
peaks = {}      #peak of each country
dpeaks = {}     #date of peak
euro_ac = {}    #current 7 day average of new cases
euro_tc = {}    #current total cases
for i in euro_pops:
    temp_df = euro.loc[euro['Country'] == i]
    temp_df = temp_df.reset_index(drop = True)
    peak = 0
    dpeak = None
    for j in temp_df.index:
        if temp_df['7 Day Average Per Million'][j] > peak:
            peak = temp_df['7 Day Average Per Million'][j]
            dpeak = temp_df['Date'][j]
    peaks[i] = peak
    dpeaks[i] = dpeak

# iterate through DF
for i in euro.index:
    # try/except used to ignore last data point where [i+1] cannot be performed
    try:
        # if datapoint is last of given state
        if euro['Country'][i] != euro['Country'][i+1] and euro['Country'][i] in ct:
            # add current 7 day av
            euro_ac[euro['Country'][i]]= euro['7 Day Average Per Million'][i]
            euro_tc[euro['Country'][i]] = euro['Total Cases'][i]
        else:
            pass
    except:
        euro_ac[euro['Country'][i]]= euro['7 Day Average Per Million'][i]
        euro_tc[euro['Country'][i]] = euro['Total Cases'][i]

euro_cur = pd.DataFrame(euro_ac.items(), columns = ['Country', 'Current 7 Day Average Per Million'])
euro_tot = pd.DataFrame(euro_tc.items(), columns = ['Country', 'Current Total Cases'])
peak = pd.DataFrame(peaks.items(), columns = ['Country', 'Peak'])
dpeak = pd.DataFrame(dpeaks.items(), columns = ['Country', 'Date of Peak'])

euro_cur = pd.merge(euro_cur, euro_tot, on = 'Country', how = 'left')
euro_cur = pd.merge(euro_cur, peak, on = 'Country', how = 'left')
euro_cur = pd.merge(euro_cur, dpeak, on = 'Country', how = 'left')
        
#transferring data to sql database table
#connect to doc
conn = sql.connect('Covid.db')
c = conn.cursor()
#convert euro DF to SQL DB
euro.to_sql('EURO_DATA', conn, if_exists = 'replace', index = False)
#convert World DF to SQL DB
df.to_sql('WORLD_DATA', conn, if_exists = 'replace', index = False)
euro_cur.to_sql('EURO_Current_Stats', conn, if_exists = 'replace', index = False)
conn.close()