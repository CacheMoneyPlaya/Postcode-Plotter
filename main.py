import argparse
import pandas as pd
import numpy as np
from geopy import geocoders  
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pgeocode
import gmplot


data_set = None
filtered_data_set = None
parser = argparse.ArgumentParser(description='Process data')
parser.add_argument('-file', '--file', help='Pass in excel file containing postcodes')
latitude = []
longitude = []

def handleArg():
    args = parser.parse_args()
    data_set = pd.read_excel(args.file, header=None).values.tolist()
    data_set = np.concatenate( data_set, axis=0 )
    data_set = list(filter(lambda p: not p.startswith('0'), data_set))
    for index, p in enumerate(data_set):
        if (p.find(' ') == -1):
            first = p[:-3]
            second = p[len(first):]
            data_set[index] = first + ' ' + second
    return data_set
    
def getLatitudeLongitude():
    print('starting lat and long process')
    nomi = pgeocode.Nominatim('GB')
    for p in filtered_data_set:
        if(np.isnan(nomi.query_postal_code(p).latitude) == False or np.isnan(nomi.query_postal_code(p).longitude) == False):
            latitude.append(nomi.query_postal_code(p).latitude)
            longitude.append(nomi.query_postal_code(p).longitude)
    print(longitude, latitude)

def plotPostCodes():
    gmap = gmplot.GoogleMapPlotter(51.45523, -2.59665, 18)
    gmap.scatter( latitude, longitude, '#ff0000', size = 1000, marker = False)
    gmap.draw("CCOB.html")
    
if (__name__ == "__main__"):
    print('Starting analysis')
    filtered_data_set = handleArg()
    getLatitudeLongitude()
    plotPostCodes()
