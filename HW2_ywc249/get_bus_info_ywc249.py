# Author: Yuwen Chang, NYU CUPS, September 2017
##############################
# Code written for HW2 of PUI2017
# https://github.com/ywnch/PUI2017_ywc249/HW2_ywc249
##############################
# put MTA API key, bus route, and output csv file as input arguments:
# i.e. run the code as:
# 	python get_bus_info_ywc249.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv
##############################

# ensure compatibility and allow reading line input args
from __future__ import print_function
import sys

# check input args
if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python get_bus_info_ywc249.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()

# import packages
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

import os
import json
import pandas as pd

# read args and generate url to fetch data from
apikey = sys.argv[1]
bus = sys.argv[2]
file = sys.argv[3]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey, bus)
#print("API URL: \n" + url)

# fetch data
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# check if bus route exists
try:
    data2 = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
except:
    error = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['ErrorCondition']
    print(error['Description'])
    sys.exit()

# parse info
lat = []
lng = []
stop = []
status = []

for v in data2:
    #global lat, lng, stop, status

    # parse location
    lt = v['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    lg = v['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    lat.append(lt)
    lng.append(lg)

    # parse next stop info
    if 'OnwardCall' in v['MonitoredVehicleJourney']['OnwardCalls']:
        s = v['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]
        stt = s['Extensions']['Distances']['PresentableDistance']
        stp = s['StopPointName']
    else:
        stt = 'N/A'
        stp = 'N/A'
    status.append(stt)
    stop.append(stp)

# write data to dictionary, indexing from 1
d = {'Latitude': lat, 'Longitude': lng, 'Stop Name': stop, 'Stop Status': status}
df = pd.DataFrame(data = d)
df.index += 1

# write df to csv file
with open('%s'%(file), 'w') as f:
    df.to_csv('%s'%(file))