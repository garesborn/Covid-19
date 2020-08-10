# =============================================================================
#                Creating a method to convert country names
# =============================================================================
# due to some countries being referred to by a number of names from source to
# source, a method was created to convert names to one common title

#initialize function
def name_conv(name):
    # Compile lists of all countries alternative names
    drc = ['DR Congo','Congo-Kinshasa', 'Congo (Kinshasa)', 'Congo, Dem. Rep. of', 'Congo, Dem Rep of' , 'Democratic Republic of the Congo', 'Congo, Democratic Republic of']
    rc = ['Congo', 'Congo-Brazzaville', 'Congo (Brazzaville)', 'Republic of the Congo','Congo, Rep of','Congo Rep. of', 'Congo, Republic of the', 'Republic of the Congo','Congo, Republic of', 'Congo Republic of']
    cv = ['Cape Verde', 'Cabo Verde']
    ky = ['Kyrgyzstan', 'Kyrgyz Republic']
    stp = ['Sao Tome and Principe', 'São Tomé and Príncipe']
    cdv = ["Côte d'Ivoire", "Cote d'Ivoire", "Ivory Coast"]
    nk = ['North Korea', "Democratic People's Republic of Korea", "DPRK", "Korea, North"]
    sk = ['South Korea', " Republic of Korea", "Korea, South"]
    skn = ["St. Kitts and Nevis", "Saint Kitts and Nevis","St Kitts and Nevis" ]
    svg = ['Saint Vincent and the Grenadines', 'St Vincent and the Grenadines','St. Vincent and the Grenadines']
    sl = ["Saint Lucia", "St. Lucia", "St Lucia"]
    es = ["Eswatini", 'Swaziland', 'Eswatini', 'Eswatini (Swaziland)']
    sy = ['Syria', 'Syrian Arab Republic']
    svk = ['Slovakia', 'Slovak Republic']
    vi = ["Vietnam", "Socialist Republic of Vietnam"]
    ru = ['Russia', 'Russian Federation']
    ye = ['Yemen', 'Republic of Yemen']
    my = ['Myanmar', 'Burma']
    br = ['Brunei','Brunei Darussalam']
    ba = ['Bahamas', "Bahamas, The", "The Bahamas"]
    ga = ['Gambia', 'Gambia, The', 'The Gambia', "Gambia, The"]
    ch = ['China', "People's Republic of China"]
    uk = ['United Kingdom', 'Great Britain']
    
    titles = [drc, rc, cv, ky, stp, cdv, nk, sk, skn, svg, sl, es, sy, svk, vi, ru, ye, my, ba, ga, ch, uk]
    
    # iterate through alternative names
    for i in titles:
        # if convertable name is found in list
        if name in i:
            # replace name with first name in list
            res = i[0]
            break
        else:
            # if not found to be convertable, return input
            res = name
    #return converted name or input name       
    return res