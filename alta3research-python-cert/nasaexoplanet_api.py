#!/usr/bin/env python3
"""Nasa Exoplanet API
Per https://exoplanetarchive.ipac.caltech.edu/docs/program_interfaces.html#data documenting how to access the API

1. (Required) Start with the base URL: https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?

2. (Required) Add the text that specifies which data table to query. In this example, we select the Kepler Objects of Interest (KOI) Cumulative Table, which is entered as cumulative:

https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative
   
   Description:
   A script to interact with an "open" api"""

# imports always go at the top of your code
#import json
import csv
import requests

"""
In this example, we specify data only for objects with a Kepler disposition of candidate (like 'CANDIDATE') with an orbital period (koi_period) more than 300 days and a planet radius (koi_prad) less than 2. Note the separator between the table and column parameters is an ampersand (&), and there are spaces before and after "and." Also, the Kepler disposition value is in all caps (i.e., 'CANDIDATE') because it appears as such in the database, and database values are case-sensitive. If in doubt, check the interactive table to see how the value appears in the data column. Lastly, the database value must be contained in single quotation marks ( ' ).
"""
#reduced the data with select of select few fileds via API call. There is a lot of data fileds. (select=kepid,kepoi_name,kepler_name)
#API = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&where=koi_disposition like 'CANDIDATE' &where=koi_period>300,koi_prad<2&order=koi_period&select=kepid,kepoi_name,kepler_name&format=json"
##API = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&where=koi_disposition like 'CANDIDATE' &where=koi_period>300,koi_prad<2&order=koi_period&select=kepid,kepoi_name,kepler_name&table=q1_q16_koi&format=json"
#API = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&where=koi_disposition like 'CANDIDATE' &where=koi_period>300,koi_prad<2&order=koi_period&select=kepid,kepoi_name,kepler_name&table=q1_q16_koi&format=JSON"
######API = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&where=koi_disposition like 'CANDIDATE' &where=koi_period>300,koi_prad<2&order=koi_period&select=kepid,kepoi_name,kepler_name&table=q1_q16_koi"
API = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&where=koi_disposition like 'CANDIDATE' &where=koi_period>300,koi_prad<2&order=koi_period&select=kepid,kepoi_name&table=q1_q16_koi"
#API = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&where=koi_disposition like 'CANDIDATE' &where=koi_period>300,koi_prad<2&order=koi_period&format=json"

def main():
    """Run time code"""

    # create resp, which is our request object
    resp = requests.get(f"{API}")  # This "f" string reads: API 
#resp is a dump out of the exoplanetarchive but it is all within 1 line in a dataset
#Now we want to break that 1 line json into lines for each kepid entry.
    #print( dir(resp) ) ##Print the methods available
####    for kepids in resp:
#    for kepids in resp.items():
#        print(kepids, end='\n')
##         print(kepids) 
##        kepids = str(kepids)
##        rows = json.loads(print(f"{kepids}") )
####        print({kepids})
    print('Kepler Data from API for Candidate exoplanets\n')
    print("_______________________________________\n")

    for kepids in resp:
#        print(kepids , end='\n')
####        keplerrow = kepids.splitlines() #cleans up /n lines in csv format from api
####        print(keplerrow , end='\n') #removes /n from end of lines 
####        print(kepids) #removes /n from end of lines 
        print(str(kepids.decode("utf-8")), end='\n' ) #removes end=/n from end of lines #The decode is to remove a encoded b' in the beginning of the line formatting from the API. I had to add decoding for utf-8 to remove it to read correctly. reference https://stackoverflow.com/questions/64388725/how-to-remove-b-from-the-beginning-of-each-line-of-string-read-from-file
#Had to also force the print to string type
        print("_______________________________________\n")
#    for kepids in resp :
#        print(str(kepids))

#        print(kepids)
#        print(kepids[kepid])
        #print(b("kepid","kepoi_name","kepler_name","koi_disposition","koi_pdisposition"), end=":\n") 


if __name__ == "__main__":
    main()

