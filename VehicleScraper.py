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
from dataclasses import dataclass
import Utilities.WebConnectors as WebConnectors
from Utilities.PositionClasses import Directioned
from Utilities.SQLQueryClasses import Insertable, Queriable, Clearable
from RouteScraper import RouteScraper


# This link appears to be the realtime link to the 503 bus location
#updated every 30 seconds
# https://trackgreenlink.com/simple/regions/89/routes/4417/direction/12705
#
##URL_GREENLINK_503_TIMES = ##"https://trackgreenlink.com/simple/regions/89/routes/4417/direction/12705"
##URL_GREENLINK_MAIN = "https://trackgreenlink.com"
SHUTTLE_URL = "https://furmansaferide.ridesystems.net/Services/JSONPRelay.svc/GetMapVehiclePoints?apiKey=8882812681"
URL_GREENLINK_LOCATION = "https://greenlink.cadavl.com:4437/SWIV/GTA/proxy/restWS/topo/vehicules"

SHUTTLE_LOCATION_TABLE = "shuttleLocations"
STOPS_DIST_TABLE = "stopsDistanceTable"

@dataclass
class Vehicle(Insertable, Directioned):
    name : str
    speed : int
    nextStopDist : int = None
    nextStopID : int = None
    
    def NoVehic():
        return Vehicle(0, 0, 0, "", 0)
    
    def __post_init__(self):
        self.updated = datetime.datetime.now()

    def updateInto(self, table, connection):
        query = f"UPDATE `{table}` SET latitude = %s, longitude = %s, direction = %s, speed = %s, updated = %s, nextStopDistance = %s, nextStopID = %s WHERE vehicle = %s"
        fields = (self.lat, self.lon, self.heading, self.speed, self.updated, self.nextStopDist, self.nextStopID, self.name)
        Vehicle.query(connection, (query, fields))
        connection.commit()
        
    def insertInto(self, table, connection, commit=True):
        attrs = [["vehicle", self.name],
                 ["latitude", self.lat],
                 ["longitude", self.lon],
                 ["speed", self.speed],
                 ["direction", self.heading],
                 ["nextStopDistance", self.nextStopDist],
                 ["nextStopID", self.nextStopID],
                 ["updated", self.updated]]
        print(attrs)        
        if self.capacity is not None:
            attrs.append(["capacity", self.capacity])
            
        Vehicle._insertIntoHelper(table, connection, attrs, commit)

        
class ShuttleScraper(WebConnectors.Scraper):
    
    def _parseVehicle(jsonDct) -> Vehicle:
        name = ShuttleScraper.maybeGetValue(jsonDct, "Name")
        #Handle names
        if name == "Campus Shuttle":
            name = "Daily Shuttle"
        elif name == "Furman Trolley":
            name = "Downtown Trolley"
        elif name == "Saferide":
            name = "SafeRide"
            
        return Vehicle( 
                ShuttleScraper.maybeGetValue(jsonDct, "Latitude"),
                ShuttleScraper.maybeGetValue(jsonDct, "Longitude"),
                ShuttleScraper.maybeGetValue(jsonDct, "Heading"),
                name,
                ShuttleScraper.maybeGetValue(jsonDct, "GroundSpeed")
               )
            
    def _pull(self):
        vehicles = []
        page_soup = ShuttleScraper.getSite(SHUTTLE_URL)
        j = json.loads(page_soup.text)
        
        for vehicle in j:
            vehicles.append(ShuttleScraper._parseVehicle(vehicle))
        return vehicles    
    
class BusScraper(WebConnectors.Scraper):
    def __init__(self, busID):
        self.busID = busID
        
    def _pull(self):
        vehicles = []
        try:
            page_soup = BusScraper.getSoup(URL_GREENLINK_LOCATION)
            buses = json.loads(page_soup.text)
        except:
            print("Json parsing failed; ensure webpage has not been moved.")  
            return
        
        buses = BusScraper.maybeGetValue(buses, "vehicule", default=None)
        if buses is None:
            print("Json search failed to find expected 'vehicule' entry; ensure webpage has not been changed.")
            return
        
        for b in buses:
            if BusScraper.maybeGetValue(b, "conduite", "idLigne", default=None) != self.busID:
                continue
            vehicles.append(
                Vehicle(
                         BusScraper.maybeGetValue(b, "localisation", "lat"),
                         BusScraper.maybeGetValue(b, "localisation", "lng"),
                         BusScraper.maybeGetValue(b, "localisation", "cap"),
                         "503 Bus", 
                         BusScraper.maybeGetValue(b, "conduite", "vitesse"),
                        )
                )
        return vehicles


def main():
    shutRoute = RouteScraper.loadRouteFromJSONFile("/home/csdaemon/aux/ShuttleRoute.json")
    busRoute = RouteScraper.loadRouteFromJSONFile("/home/csdaemon/aux/503Route.json")
    
    shut = []
    shut += [(s, shutRoute) for s in ShuttleScraper().tryPull()]
    shut += [(b, busRoute) for b in BusScraper(busRoute.lineID).tryPull()]
            
    connection = WebConnectors.formConnections()
    
    for shuttle, route in shut:
        stopDists = route.distToStops(shuttle)
        shuttle.nextStopID = stopDists[0][0].stopOrderID
        shuttle.nextStopDist = stopDists[0][1]
        print(shuttle)
        shuttle.updateInto(SHUTTLE_LOCATION_TABLE, connection)
        Clearable._clearHelper(STOPS_DIST_TABLE, connection, [["lineID", route.lineID]])
        for stops in stopDists:
            attrs = [["stopOrderID", stops[0].stopOrderID],
                     ["lineID", stops[0].lineID],
                     ["distFromVehicle", stops[1]]]
            Insertable._insertIntoHelper(STOPS_DIST_TABLE, connection, attrs)
        
    clearOutdated = f"UPDATE `{SHUTTLE_LOCATION_TABLE}` SET latitude=%s, longitude=%s, direction=%s, speed=%s, updated=%s WHERE updated < (NOW() - INTERVAL 3 MINUTE)"
    var = (None, None, None, None, datetime.datetime.now())
    Queriable.query(connection, (clearOutdated, var))
    connection.close()

if __name__ == "__main__":
    main()
