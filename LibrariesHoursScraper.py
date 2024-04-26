# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:00:42 2024

@author: mdavi
"""

# Library hours requester 

import requests
import json
import datetime
from HoursOpenScrapers import TimesScraper
from Utilities.WebConnectors import getLibraryAPIToken, formConnections
from Utilities.TimeClasses import Schedule, TimeRange
from typing import List
from dateutil.parser import parse

SCHEDULE_TABLE = "buildingHours"
BUILDING_INFO_TABLE = "buildingLocations"

class LibrariesScraper(TimesScraper):
    def _getLastSunday() -> datetime.date:
        today = datetime.date.today()
        index = (today.weekday() + 1) % 7
        lastSun = today - datetime.timedelta(index)
        return lastSun
    
    def _buildTimeRangeFromJSON(jsonDct) -> List[TimeRange]:
        ranges = []
        if jsonDct is None:
            return [TimeRange.Failed()]
                
        status = TimesScraper.maybeGetValue(jsonDct, "status") 
        hours =  TimesScraper.maybeGetValue(jsonDct, "hours")
        if status is None:
            return [TimeRange.Failed()]
        elif status == "closed" or hours is None or hours == {}:
            return [TimeRange.Closed()]
        
        for rngs in hours:
            start = TimesScraper.maybeGetValue(rngs, "from")
            close = TimesScraper.maybeGetValue(rngs, "to")
            
            if start is not None and close is not None:
                ranges.append(TimeRange(parse(start), parse(close)))
            else:
                ranges.append(TimeRange.Closed())
        return ranges
        
        
    def _buildLibraryScheduleFromJSON(jsonDct): 
        if jsonDct is None:
            return None
        
        name = TimesScraper.maybeGetValue(jsonDct, "name")
        dates = TimesScraper.maybeGetValue(jsonDct, "dates")
        
        if name is None:
            name = "Failed"
        
        sched = Schedule(name)
        if dates is None:
            sched.addDayRangeTime(Schedule._daysOfWeek, TimeRange.Failed())
            
        for d, hours in dates.items():
            ranges = LibrariesScraper._buildTimeRangeFromJSON(hours)
            day = parse(d)
            sched.addDayRangeTime(day.strftime("%A"), ranges)
        return sched
        
    def _getJson():
        accessToken = getLibraryAPIToken()
        oauthHeader = {"Authorization" : "Bearer " + str(accessToken)}
        
        # Request string has ID of libraries 
        # 10143 = Duke, 10144 = Music, 10146 = Science, 10147 = Special Collections
        # Followed by query string and then "from" and "to" in 'YYYY-MM-DD'. 
        # Query automatically uses today's date if one isn't specified.

        lastSunday = LibrariesScraper._getLastSunday()
        nextSaturday = lastSunday + datetime.timedelta(6)
        lmString = lastSunday.strftime("%Y-%m-%d")
        nsString = nextSaturday.strftime("%Y-%m-%d")

        hoursRequest = f"https://libcal.furman.edu/1.1/hours/10143,10144,10146,10147?from={lmString}&to={nsString}"
        hoursReqResp = requests.get(hoursRequest,headers=oauthHeader, timeout=2)
        hours = json.loads(hoursReqResp.content)
        return hours

    
    def _pull(self) -> List[Schedule]:
        scheds = []
        jsonHours = LibrariesScraper._getJson()
        for lib in jsonHours:
            scheds.append(LibrariesScraper._buildLibraryScheduleFromJSON(lib))
        return scheds
    
def main():
    a = LibrariesScraper()
    scheds = a.tryPull()
    
    for sched in scheds:
        parsesuccess = False if sched is None else sched.noFails()
        
        if sched is None:
            continue
        print('----------------------------')
        print(sched.name)
        print("Successful parse." if parsesuccess else "Failed in parsing.")
        if not parsesuccess:
            continue
        
        connection = formConnections()
        if connection is None:
            continue
        updatesuccess = sched.updateInto(SCHEDULE_TABLE, BUILDING_INFO_TABLE, connection, onlyMainSchedule=True)
        print("Successful updated." if updatesuccess else "Failed to update.")
            
    if connection != None:
        connection.close()
    
if __name__ == "__main__":
    main()
