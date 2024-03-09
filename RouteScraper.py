
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 22:21:32 2024

@author: mdavi
"""

import json
from typing import List, Union, Tuple
import polyline
from Utilities.WebConnectors import Scraper
from Utilities.SQLQueryClasses import Insertable
from Utilities.PositionClasses import Positioned, Directioned

GREENLINK_WEBSITE = "https://greenlink.cadavl.com:4437/SWIV/GTA"
URL_GREENLINK_STOPS_AND_ROUTE_AND_ID = "https://greenlink.cadavl.com:4437/SWIV/GTA/proxy/restWS/topo"

SHUTTLE_WEBSITE = "https://furmansaferide.ridesystems.net/routes"
CAMPUS_SHUTTLE_STOPS_AND_ROUTE = "https://furmansaferide.ridesystems.net/Services/JSONPRelay.svc/GetStops?apiKey=8882812681"
CAMPUS_SHUTTLE_ID = "https://furmansaferide.ridesystems.net/Services/JSONPRelay.svc/GetRoutes?apiKey=8882812681"

ROUTE_TABLE = 'routes'

class LinePoint(Directioned):
    def __init__(self, orderID, lat, lon, lineName, isStop = False, heading = None, distance = None):
        super().__init__(lat, lon, heading)
        self.orderID = orderID
        self.lineName = lineName
        self.isStop = isStop
        self.distance = distance
        
    def correctHeading(self, after : Positioned):
        self.heading = LinePoint.headingBetween(self, after)
        
    def distFromStart(self, before : "LinePoint"):
        self.distance = LinePoint.distBetween(self, before) + before.distance
    
    def toJSONdict(self):
        return { "orderID" : self.orderID,
               "lat" : self.lat,
               "lon" : self.lon,
               "heading" : self.heading,
               "lineName" : self.lineName,
               "isStop" : self.isStop,
               "distance" : self.distance}
    
    def fromJSONdict(dct):
        if dct["isStop"] == True:
            return LineStop.fromJSONdict(dct)
        return LinePoint(dct["orderID"],
                        dct["lat"],
                        dct["lon"],
                        dct["lineName"],
                        isStop = dct["isStop"], 
                        heading = dct["heading"],
                        distance = dct["distance"])
    

class LineStop(LinePoint, Insertable):
    def __init__(self, orderID, lat, lon, lineName, stopName, stopOrderID, heading=None):
        super().__init__(orderID, lat, lon, lineName, isStop = True, heading=heading, distance=0)
        self.stopName = stopName
        self.stopOrderID = stopOrderID
        
    def insertInto(self, table):
        pass
    
    def toJSONdict(self):
        dct = super().toJSONdict()
        dct["stopName"] = self.stopName
        dct["stopOrderID"] = self.stopOrderID
        return dct
        
    def fromJSONdict(dct):
        return LineStop(dct["orderID"],
                        dct["lat"],
                        dct["lon"],
                        dct["lineName"],
                        dct["stopName"],
                        dct["stopOrderID"],
                        heading=dct["heading"])
    
        
class RouteScraper(Scraper, Insertable):
    lineName : str
    lineIdentifier : Union[int, str]
    idInTable : int
    lineID : int
    lineRoute: List[LinePoint]
    website: str
    routePolyline: str
    
    def __init__(self, lineName, lineIdentifier, idInTable):
        self.lineName = lineName
        self.lineIdentifier = lineIdentifier
        self.idInTable = idInTable
        self.lineID = None
        self.lineRoute = None
    
    def insertInto(self, table, connection, commit=True):
        pline = []
        for p in self.lineRoute:
            pline.append((p.lat, p.lon))
        
        encodedPolyline = polyline.encode(pline)
        self.routePolyline = encodedPolyline
        
        attrs = [["id", self.idInTable ],
                  ["shuttleName", self.lineName],
                  ["shuttleIDExternal", self.lineID],
                  ["routePolyline", self.routePolyline],
                  ["website", self.website]]
        
        RouteScraper._insertIntoHelper(table, connection, attrs, commit)
                
    def saveRouteToJSONFile(self, filepath):
        dct = {"lineName" : self.lineName,
               "lineIdentifier" : self.lineIdentifier,
               "idInTable" : self.idInTable,
               "lineID" : self.lineID,
               "website" : self.website,
               "lineRoute" : [a.toJSONdict() for a in self.lineRoute]}
        
        with open(filepath, "w") as outfile:
            json.dump(dct, outfile, indent=2)
        
    def loadRouteFromJSONFile(filepath):
        with open(filepath, "r") as infile:
            json_object = json.load(infile)
            
        route = RouteScraper(json_object["lineName"], json_object["lineIdentifier"], json_object["idInTable"])
        route.lineID = json_object["lineID"]
        route.website = json_object["website"]
        route.lineRoute = [LinePoint.fromJSONdict(r) for r in json_object["lineRoute"]]
        return route
    
    def distToStops(self, vehic : Directioned) -> List[Tuple[LineStop, int]]:        
        minDist = 1
        minInd = -1
        for i, pnt in enumerate(self.lineRoute):
            dist = LinePoint.distBetween(vehic, pnt)
            relativeHeading = (vehic.heading - pnt.heading) % 360
            if dist < 0.05 and (relativeHeading > 270 or relativeHeading < 90) :
                if dist < minDist:
                    minDist = dist
                    minInd = i
            elif minDist < 1:
                break
        
        distanceIntoRoute = self.lineRoute[minInd].distance
        
        stopDists = []
        for stop in self.lineRoute[minInd:]:
            if stop.isStop:
                stopDists.append((stop, 
                                 stop.distance - distanceIntoRoute))
        for stop in self.lineRoute[:minInd]:
            if stop.isStop:
                stopDists.append((stop, 
                                 stop.distance + self.lineRoute[-1].distance - distanceIntoRoute))
                
        return stopDists            
                    
    
    def _pull(self):
        pass
    
        
class ShuttleRouteScraper(RouteScraper):
    
    website = SHUTTLE_WEBSITE

    def _getLineRoute(self, page_json) -> List[LinePoint]:
        def maybe(dct, key, default=None):
            return ShuttleRouteScraper.maybeGetValue(dct, key, default=default)
        
        points = []
        stopNumber = 0
        for stops in page_json:
            if maybe(stops, "RouteID", default=-1) == self.lineID:
                points.append(
                    LineStop(len(points), 
                              maybe(stops, "Latitude"),
                              maybe(stops, "Longitude"),
                              self.lineName,
                              maybe(stops, "Description"),
                              stopNumber))
                stopNumber += 1
                for p in maybe(stops, "MapPoints", []):
                    points.append(
                        LinePoint(
                            len(points),
                            p["Latitude"],
                            p["Longitude"],
                            self.lineName
                            )
                        )
        
        points[0].distance = 0
        for p in range(1, len(points)):
            points[p].distFromStart(points[p-1])
            
        points[-1].correctHeading(points[0])
        ## Carried out in reverse order so that the heading to the 
        ## next stop is able to be calculated
        for p in range(len(points)-2, -1, -1):
            points[p].correctHeading(points[p + 1])
        
        return points
    
    def _getRouteNumber(self):
        page_soup = ShuttleRouteScraper.getSoup(CAMPUS_SHUTTLE_ID)
        page_json = json.loads(page_soup.text)
        for shut in page_json:
            if ShuttleRouteScraper.maybeGetValue(shut, "Description") == self.lineIdentifier:
                return ShuttleRouteScraper.maybeGetValue(shut, "RouteID")
        
    def _pull(self):
        page_soup = ShuttleRouteScraper.getSoup(CAMPUS_SHUTTLE_STOPS_AND_ROUTE)
        page_json = json.loads(page_soup.text)
        self.lineID = self._getRouteNumber()
        self.lineRoute = self._getLineRoute(page_json)
        return self.lineRoute
        

class BusRouteScraper(RouteScraper):
    
    website = GREENLINK_WEBSITE
    
    def _getRouteSegs(self, page_json) -> List[LinePoint]:
        segs = []
        for entry in BusRouteScraper.maybeGetValue(page_json, "topo", default=[]):
            lines = BusRouteScraper.maybeGetValue(entry, "ligne")
            if lines is None:
                continue
            for line in lines:
                if BusRouteScraper.maybeGetValue(line, "idLigne") == self.lineID:
                    for sect in BusRouteScraper.maybeGetValue(line, "itineraire"):
                        segs.append([])
                        for entry in BusRouteScraper.maybeGetValue(sect, "troncons", default=[]):
                            segs[-1].append(
                                LinePoint(
                                    len(segs[-1]),
                                    BusRouteScraper.maybeGetValue(entry, "debut", "lat"),
                                    BusRouteScraper.maybeGetValue(entry, "debut", "lng"),
                                    self.lineName
                                    )
                                )
                    break
        return segs
    
    def _segsToRoute(self, segs: List[List[LinePoint]]) -> List[LinePoint]:
        ## This is a mess and I'm sorry to do it to you.
        ## The GreenLink doesn't provide an entire circuit;
        ## instead, it has a line with several additional 
        ## segments that are for locations where the bus does
        ## not follow its identical path back.
        ## To create a circuit, we need to take the original path,
        ## stick a reversed copy of it onto it, find the sections
        ## that are supposed to be replaced, and replace them.
        ## I do so in a four-step process
        ## 1. Assumes first section is main route & take a reversed
        ##    copy of it.
        ## 2. Begins working backwards with each additional segment,
        ##    repeating points backwards until you find the point closest
        ##    to the start or end of a new segment
        ## 3. That segment takes over until its end, at which point the 
        ##    closest point on the original line picks back up 
        ## 4. Repeat for all segments
        
        points = []
        for p in segs[0]:
            points.append(p)
            
        backwardsMain = segs[0][::-1]
        lastPoint = 0
        
        for seg in segs[1:]:
            reverseSeg = False
            minDist = 1
            minInd = lastPoint
            
            # Finds the earliest point on the main route 
            # that is closest to either the start or end of the 
            # segment
            for i, p in enumerate(backwardsMain[lastPoint:]):
                toStart = LinePoint.distBetween(seg[0], p) 
                toEnd = LinePoint.distBetween(seg[-1], p) 
                if toStart < 0.05 or toEnd < 0.05:
                    if min(toStart, toEnd) < minDist:
                        if toEnd < toStart:
                            reverseSeg = True
                        minDist = min(toStart, toEnd)
                        minInd = lastPoint + i
                elif (toEnd if reverseSeg else toStart) > 0.05 and minDist < 1:
                    break
            
            # Inserts the points on the reversed list, from the
            # last point used to the new index where the 
            # segment will take over, followed, by the points 
            # on the segment, into the route point list
            for p in backwardsMain[lastPoint:minInd]    \
                            + seg[::-1 if reverseSeg else 1]:
                points.append(
                    LinePoint(
                        len(points),
                        p.lat,
                        p.lon,
                        p.lineName
                        )
                    )
            
            ## Finds the closest point to the terminus, for
            ## use in the next loop
            terminus = seg[0] if reverseSeg else seg[-1]
            minTermDist = 1
            minTermInd = minInd
            for i, p in enumerate(backwardsMain[minInd:]):
                toTerminus = LinePoint.distBetween(terminus, p)
                if toTerminus < 0.05:
                    if toTerminus < minTermDist:
                        minTermDist = toTerminus
                        minTermInd = minInd + i
                elif toTerminus > 0.05 and minTermDist < 1:
                    break
            lastPoint = minTermInd
            
        ## Adds all final points until it reaches the beginning:
        for p in backwardsMain[lastPoint:]:
            points.append(
                LinePoint(
                    len(points),
                    p.lat,
                    p.lon,
                    p.lineName
                    )
                )
        
        return points
    
    def _getRouteStops(self, page_json) -> List[LineStop]:
        def maybe(dct, *keys, default=None):
            return ShuttleRouteScraper.maybeGetValue(dct, *keys, default=default)
        
        stops  = []
        for entry in maybe(page_json, "topo", default=[]):
            unparsedStops = maybe(entry, "pointArret")
            if unparsedStops is None:
                continue
            for stop in unparsedStops:
                lines = maybe(stop, "infoLigneSwiv")
                if lines is None:
                    continue
                for line in lines:
                    if maybe(line, "idLigne") == self.lineID:
                        stops.append(
                            LineStop(-1, 
                                      maybe(stop, "localisation", "lat"),
                                      maybe(stop, "localisation", "lng"),
                                      self.lineName,
                                      maybe(stop, "nomCommercial"),
                                      -1))
        return stops
        
    def _stopsIntoRoute(self, route, stops):
        ## Add stops to route
        for stop in stops:
            minDist = 1
            minInd = -1
            for i, p in enumerate(route):
                toStop = LinePoint.distBetween(stop, p)
                if toStop < 0.05:
                    headToStop = LinePoint.headingBetween(p, stop)
                    if toStop < minDist and (headToStop - p.heading) % 360 < 180:
                        minDist = toStop
                        minInd = i
                elif toStop > 0.05 and minDist < 1:
                    break
            if minInd != -1:
                route[minInd] = LineStop(
                        minInd,
                        stop.lat, 
                        stop.lon,
                        stop.lineName,
                        stop.stopName,
                        -1
                    )
                route[minInd].correctHeading(route[(minInd + 1) % len(route)])

        numStop = 0
        for p in route:
            if isinstance(p, LineStop):
                p.stopOrderID = numStop
                numStop += 1
                
        return route
 
    def _getBusRoute(self, page_json) -> List[LinePoint]:
        
        segs = self._getRouteSegs(page_json)
        stops = self._getRouteStops(page_json)
        
        route = self._segsToRoute(segs)
         
        route[-1].correctHeading(route[0])
        for i in range(len(route) - 2, -1, -1):
            route[i].correctHeading(route[i + 1])
            
        points = self._stopsIntoRoute(route, stops)
        
        # Makes sure there is a stop at the start of the circuit
        count = 0
        while not isinstance(points[0], LineStop) and count < len(points):
            points.append(points.pop(0))
            count += 1
    

        points[0].distance = 0
        for i in range(1, len(points)):
            points[i].distFromStart(points[i - 1])
        
        return points
        
    def _getBusID(self, page_json):
        for entry in page_json["topo"]:
            lines = BusRouteScraper.maybeGetValue(entry, "ligne")
            if lines is None:
                continue
            for line in lines:
                lineName = BusRouteScraper.maybeGetValue(line, "nomCommercial")
                if lineName is None:
                    continue
                if lineName == self.lineIdentifier:
                    return BusRouteScraper.maybeGetValue(line, "idLigne")
        return None    
            
    def _pull(self):
        page_soup = BusRouteScraper.getSoup(URL_GREENLINK_STOPS_AND_ROUTE_AND_ID)
        page_json = json.loads(page_soup.text)
        self.lineID = self._getBusID(page_json)
        self.lineRoute = self._getBusRoute(page_json)
        return self.lineRoute
                   
        
def main():
    a = ShuttleRouteScraper("Campus Shuttle", "Furman University Shuttle", 2)
    a.tryPull()
    a.saveRouteToJSONFile("./ShuttleRoute.json")
    
    b = BusRouteScraper("503 Bus", "503", 2)
    b.tryPull()
    b.saveRouteToJSONFile("./503Route.json")
    
    
    
if __name__ == "__main__":
    main()