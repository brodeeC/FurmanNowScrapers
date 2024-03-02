# -*- coding: utf-8 -*-
"""

Created on Sat Jun  6 14:45:40 2020

@author: Ethan
Scrapes Greenlink webpage for time info on the 503 Bus.
Once ETAs are acquired, prints them and updates database.
Dependencies: BeautifulSoup, urllib, pymysql.

Modified on Wed Jan  24 2024

@author: Michael
Updated to work for new web locations, added in "Maybe" pattern 
to JSon tree access.
"""

import json
import datetime
import WebConnectors
from dataclasses import dataclass
from SQLQueryClasses import Insertable, Clearable

# This link appears to be the realtime link to the 503 bus location
#updated every 30 seconds
# https://trackgreenlink.com/simple/regions/89/routes/4417/direction/12705
#
##URL_GREENLINK_503_TIMES = ##"https://trackgreenlink.com/simple/regions/89/routes/4417/direction/12705"
##URL_GREENLINK_MAIN = "https://trackgreenlink.com"
SHUTTLE_URL = "https://furmansaferide.ridesystems.net/Services/JSONPRelay.svc/GetMapVehiclePoints?apiKey=8882812681"
URL_GREENLINK_LOCATION = "https://greenlink.cadavl.com:4437/SWIV/GTA/proxy/restWS/topo/vehicules"
ID_FOR_503_BUS = 17959
SHUTTLE_LOCATION_TABLE = "shuttleLocations"

@dataclass
class Vehicle(Clearable, Insertable):
    name : str
    latitude : int
    longitude : int
    speed : int
    heading : int
    eta : int = -1
    capacity : str = None
    
    def __post_init__(self):
        self.updated = datetime.datetime.now()

    def updateInto(self, table, connection):
        self.clearFrom(table, connection, commit=False)
        self.insertInto(table, connection, commit=False)
        connection.commit()
        
    def insertInto(self, table, connection, commit=True):
        attrs = [["vehicle", self.name],
                 ["latitude", self.latitude],
                 ["longitude", self.longitude],
                 ["speed", self.speed],
                 ["direction", self.heading],
                 ["estimatedTime", self.eta],
                 ["updated", self.updated]]
        
        if self.capacity is not None:
            attrs.append(["capacity", self.capacity])
            
        Vehicle._insertIntoHelper(table, connection, attrs, commit)
        
    def clearFrom(self, table, connection, commit=True):
        Vehicle._clearHelper(table, 
                             connection,
                             [["updated", "(NOW() - INTERVAL 3 MINUTE)", "<"],
                              ["vehicle", self.name, "=", "AND"]],
                             commit)
        
class ShuttleScraper(WebConnectors.Scraper):
    
    def _parseVehicle(jsonDct) -> Vehicle:
        name = ShuttleScraper.maybeGetValue(jsonDct, "Name")
        # Handle names
        if name == "Campus Shuttle":
            name = "Daily Shuttle"
        elif name == "Furman Trolley":
            name = "Downtown Trolley"
        elif name == "Saferide":
            name = "SafeRide"
            
        return Vehicle(name, 
                ShuttleScraper.maybeGetValue(jsonDct, "Latitude"),
                ShuttleScraper.maybeGetValue(jsonDct, "Longitude"),
                ShuttleScraper.maybeGetValue(jsonDct, "GroundSpeed"),
                ShuttleScraper.maybeGetValue(jsonDct, "Heading")
               )
            
    def _pull(self):
        vehicles = []
        page_soup = ShuttleScraper.getSoup(SHUTTLE_URL).text
        j = json.loads(page_soup)
        
        for vehicle in j:
            vehicles.append(ShuttleScraper._parseVehicle(vehicle))
        return vehicles    
    
class BusScraper(WebConnectors.Scraper):
    def _pull(self):
        vehicles = []
        try:
            page_soup = BusScraper.getSoup(URL_GREENLINK_LOCATION)
            buses = json.loads(page_soup.text)
        except:
            print("Json parsing failed; ensure webpage has not been moved.")  
            return []
        
        buses = ShuttleScraper.maybeGetValue(buses, "vehicule", default=None)
        if buses is None:
            print("Json search failed to find expected 'vehicule' entry; ensure webpage has not been changed.")
            return []
        
        for b in buses:
            if ShuttleScraper.maybeGetValue(b, "conduite", "idLigne", default=None) != ID_FOR_503_BUS:
                continue
            vehicles.append(
                Vehicle("503 Bus", 
                         ShuttleScraper.maybeGetValue(b, "localisation", "lat"),
                         ShuttleScraper.maybeGetValue(b, "localisation", "lng"),
                         ShuttleScraper.maybeGetValue(b, "conduite", "vitesse"),
                         ShuttleScraper.maybeGetValue(b, "localisation", "cap")
                        )
                )
                
        return vehicles

def main():
    shut = []
    shut += ShuttleScraper().tryPull()
    shut += BusScraper().tryPull()
            
    connection = WebConnectors.formConnections()
    for shuttle in shut:
        shuttle.updateInto(SHUTTLE_LOCATION_TABLE, connection)
    connection.close()

if __name__ == "__main__":
    main()