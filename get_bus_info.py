import requests
import json
import sys
import csv


#The inputs at the command line are for the user's MTA key and the busline 
key = sys.argv[1]
busline = sys.argv[2]
nameofcsv = sys.argv[3]

#Points the script to the right MTA API.  URLlib2 did not install on my machine, so I used the "requests" libary to create a request object.        
url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" %(key, busline)
request = requests.get(url)
#Stores the request object as a JSON file
data = request.json()


    #Code to grab test file from hard drive 
    #jsonFile = open("C:\\Users\\Max 'the facts'\\Desktop\\Principals of Urban Infomatics\\Week 2\\bus.json", 'r')
    #data = json.load(jsonFile)

#Parises the JSON file to discover the right nested dictionary.  The Dictionary "VehicleActivity" has entires for each active bus.
eachbus = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]

#with open(sys.argv[3], 'wb') as csvFile:
with open(nameofcsv, 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
        writer.writerow(headers)

        for bus in eachbus:
            if bus["MonitoredVehicleJourney"]["OnwardCalls"] == {}:
                Latitude = bus["MonitoredVehicleJourney"]["VehicleLocation"][u'Latitude']
                Longitude = bus["MonitoredVehicleJourney"]["VehicleLocation"][u'Longitude']
                stopname = "N/A"
                stopstatus = "N/A"
            else:
                stopname = bus["MonitoredVehicleJourney"]["OnwardCalls"]['OnwardCall'][0]["StopPointName"]
                stopstatus = bus ["MonitoredVehicleJourney"]["OnwardCalls"]['OnwardCall'][0]["Extensions"]["Distances"]["PresentableDistance"]
                Latitude = bus["MonitoredVehicleJourney"]["VehicleLocation"][u'Latitude']
                Longitude = bus["MonitoredVehicleJourney"]["VehicleLocation"][u'Longitude']
                
            writer.writerow([Latitude, Longitude, stopname, stopstatus])    