# Author: Yuwen Chang, NYU CUPS, September 2017
##############################
# Code written for HW2 of PUI2017
# https://github.com/ywnch/PUI2017_ywc249/HW2_ywc249
##############################
# put MTA API key and bus route as input arguments:
# i.e. run the code as:
# 	python show_bus_locations_ywc249.py <MTA_KEY> <BUS_LINE>
##############################

# ensure compatibility and allow reading line input args
from __future__ import print_function
import sys

# check input args
if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python show_bus_locations_ywc249.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

# import packages
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

import os
import json
import numpy as np
import pandas as pd
import pylab as pl

# read args and generate url to fetch data from
apikey = sys.argv[1]
bus = sys.argv[2]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey, bus)
print("API URL: \n" + url)

# fetch data
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

data2 = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

# parse route info: line number, active vehicles
print("Bus Line: " + bus)
print("Number of Active Buses: " + str(len(data2)))

# parse vehicle info: location (lat, long)
i = 1
for v in data2:
    line = v['MonitoredVehicleJourney']['LineRef']
    lt = v['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    lng = v['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    vrf = v['MonitoredVehicleJourney']['VehicleRef']
    vrf = vrf.split("_")[1]
    print("Bus %s (#%s) is at latitude %s and longitude %s"%(i, vrf, lt, lng))
    i += 1