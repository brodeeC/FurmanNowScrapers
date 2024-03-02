# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 14:39:08 2024

@author: mdavi
"""

from datetime import datetime
from dataclasses import dataclass
from typing import List, ClassVar
from Utilities.SQLQueryClasses import Queriable, Insertable, Clearable, Selector
import traceback

@dataclass
class TimeRange():
    """ Class represents a range of times, i.e. 8 am to 5 pm,
        conceptualized as an opening and closing time. 
        
        Attributes:
            opn: datetime indicating the time the range begins 
                at, i.e. opening time
            close: datetime indicating the time the range ends
                at, i.e. closing time
            checkClosed: boolean indicating if 

        An input of 12 am to 12am,
        unless "checkClosed" is set to false. Recommended behavior
        is to use the singleton Closed() function to get a special closed
        instance. The singleton Failed() function similarly is recommended
        for if parsing has failed and a range indicating this is desired.
        
    """
    
    _closed: ClassVar = None   
    _failed: ClassVar = None
    
    opening: datetime
    closing: datetime
    
    def __init__(self, opn, close):
        self.opening = opn
        self.closing = close

    
    def __str__(self):
        return f'{self.openingStr()} to '\
                f'{self.closingStr()}'
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, othr):
        return TimeRange._timeEquals(self.opening, othr.opening) and \
                TimeRange._timeEquals(self.closing, othr.closing)
                
    def _timeEquals(first, second):
        return first.hour == second.hour and first.minute == second.minute
    
    """ Outputs the opening time in HH:MM:SS format. """
    def openingStr(self):
        return self.opening.strftime("%H:%M:%S")
    
    """ Outputs the closing time in HH:MM:SS format. """
    def closingStr(self):
        return self.closing.strftime("%H:%M:%S")
     
    """ Returns singleton instance of a range indicating a closed status. """               
    def Closed():
        if TimeRange._closed is None:
            TimeRange._closed = TimeRange(datetime(1970,1,1,0,0), 
                                datetime(1970,1,1,0,0))
        return TimeRange._closed
    
    """ Returns singleton instance of a range indicating a failed status. """               
    def Failed():
        if TimeRange._failed is None:
            TimeRange._failed = TimeRange(datetime(1970,1,1,12,34),
                                          datetime(1970,1,1,4,32))
        return TimeRange._failed
    
    """ Checks if an instance is closed. """
    def isClosed(self):
        return TimeRange.Closed() == self
    
    """ Checks if an instance is failed. """
    def isFailed(self):
        return TimeRange.Failed() == self

@dataclass        
class Schedule():
    """ Stores a weekly operational schedule for a location. 
    
    Attributes:
        name: str name of the location the schedule is for. 
        
    """
        
    _daysOfWeek : ClassVar = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    _defaultPeriod : ClassVar = "Regular Operation"
    
    _dayAbbrevs : ClassVar = \
        {"Monday":     ["monday", "mon", "m", "mn"], 
        "Tuesday":      ["tuesday", "tues", "tue", "t", "tu"],
        "Wednesday":    ["wednesday", "wed", "w", "wd"],
        "Thursday" :    ["thursday", "thurs", "thur", "thu", "th", "h"], 
        "Friday":       ["friday", "fri", "fr", "f"], 
        "Saturday":     ["saturday", "sat", "s"], 
        "Sunday":       ["sunday", "sun", "su", "u"]} 
        
    name : str
    
    def __post_init__(self):
        """ A Schedule holds a series of "time periods", which are diffierentiable 
            times for the schedule to be used. For instance, a regular operations
            period could have this week's hours, while a holidays period could have
            the hours for if a day is a holiday, or a summer period could have
            the summer hours. See _emptyTimePeriod() for more information."""
        self.schedule = {"Regular Operation" : Schedule._emptyTimePeriod()}
        
    """  Generates a "time period" with each day of the week being closed. 
        A "time period" is a dictionary with a key for each day of the week
        and an associated list of TimeRanges for open/close periods on each 
        day."""            
    def _emptyTimePeriod():
        return {d: [TimeRange.Closed()] for d in Schedule._daysOfWeek}
    
    """ Helper method for __str__, converts time period
        dictionary into a string. """
    def _timePeriodStr(dct):
        dctstr = ""
        for k, v in dct.items():
            dctstr += f"\t\t{k} : \n"
            if type(v) is type({}):
                dctstr += Schedule._dctStr(v)
            elif type(v) is type([]):
                for e in v:
                    dctstr += f"\t\t\t{str(e)} \n"
            else:
                dctstr += f"\t\t\t{str(v)} \n"
        return dctstr
            
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        strs = [f"\t{name}: \n{Schedule._timePeriodStr(per)}" for name, per in self.schedule.items()]
        periodStrings = "".join(strs)
        return str(self.name) + " - \n" + periodStrings
    
    """ Static function to transform an abbreviation of a day name into the
        full name. """ 
    def dayNameOf(day: str):
        day = day.lower() \
                 .strip()  \
                 .replace(".","")
        for i, d in Schedule._dayAbbrevs.items():
            if day in d:
                return i

    """ Checks if all entries in a Schedule have TimeRanges that are not
        copies of the Failed instance, i.e. no crashes have occurred in creating 
        the schedule.
    """
    def noFails(self):
        for ran, dct in self.schedule.items():
            for day, info in dct.items():
                for i, v in enumerate(info):
                    if self.schedule[ran][day][i] == TimeRange.Failed():
                        return False
        return True
        
    """ Adds a single, or a series, of TimeRanges into the schedule for a single,
        or series of, days. 
        
        Attributes:
            days: str or List[str] of days in the week that the time will
                be applied to
            ranges: TimeRange or List[TimeRange] of time ranges that 
                the location will be opened during; entry is added to all 
                days in use.
            period: str representing which "time period" these hours are
                for; a default time representing general operations is stored
                when no value is provided.
    """
    def addDayRangeTime(self, days: List[str], ranges: List[TimeRange], 
                        period: str = _defaultPeriod):
        
        # Checks if single entry or list, and transforms into list.
        ranges =  [ranges] if isinstance(ranges, TimeRange) else ranges
        days =    [days]   if isinstance(days,   str)       else days
        
        # Creates empty time period if period is a new entry
        if period not in self.schedule:
            self.schedule[period] = Schedule._emptyTimePeriod()
            
        # Adds all provided ranges to all provided days in the period.
        for d in days:
            for t in ranges:
                if self.schedule[period][d][0] == TimeRange.Closed() or \
                    self.schedule[period][d][0] == TimeRange.Failed():
                    self.schedule[period][d][0] = t
                else:
                    self.schedule[period][d].append(t)  
                    
    def _updatePeriodSchedule(cursor, insertTable, buildingID, sched, period):
        for day, times in sched.items():
            for ranges in times:
                attrs = [["buildingID", buildingID],
                         ["day", day],
                         ["dayorder", Schedule._daysOfWeek.index(day)]]
                if not ranges.isClosed() or ranges.isFailed():
                    attrs += [["start", ranges.openingStr()],
                              ["end", ranges.closingStr()]]
                Queriable.cursorQuery(cursor, 
                                      Insertable._formulateInsert(insertTable, attrs)
                                      )  
                
    def selectBuildingIDFrom(self, namesIDTable, cursor):
        try:
            Queriable.cursorQuery(cursor, 
                                  Selector._formulateSelect(
                                      namesIDTable,
                                      attrs = ["buildingID"],
                                      conds = [["name", self.name],
                                               ["nickname", self.name]]
                                      )
                                  )
            fetch = cursor.fetchone()
            if fetch is None or "buildingID" not in fetch:
                print(f"No entry in {namesIDTable} for {self.name}.")
                return None
            else:
                return fetch["buildingID"]
        except:
            traceback.print_exc()
            print(f"Crash selecting buildingID from {namesIDTable}")
            return None
        
    """ Updates the primary table with the contents from this schedule, including deleting
        old times for the location if they exist.         
        Attributes:
            insertTable: str with name of table in database that info will be added to
            namesIDTable: str with name of table in database that contains information
                about the locations on campus and the ID numbers for each location.
            connection: pymysql connection used to connect to, and add to, database.
    """            
    def updateInto(self, insertTable, buildingIDTable, connection, onlyMainSchedule=True):
        
        ## To-Do
        try:
            with connection.cursor() as cursor:
                self.buildingID = self.selectBuildingIDFrom(buildingIDTable, cursor)
                
                if self.buildingID is None:
                    print("Invalid buildingID provided.")
                    return False
                    
                Queriable.cursorQuery(cursor, 
                                      Clearable._formulateClear(
                                          insertTable,
                                          conds = [["buildingID", self.buildingID]],
                                          )
                                      )
                
                schedules = [("Main", self.schedule[Schedule._defaultPeriod])] if onlyMainSchedule else self.schedule.items()
                
                for period, entry in schedules:
                    Schedule._updatePeriodSchedule(cursor, insertTable,
                                                   self.buildingID, 
                                                   entry, period)
                              
                connection.commit()
                return True
        except Exception as e:
            traceback.print_exc()
            print(e, "error")
            connection.rollback()
            return False           
    
@dataclass
class Event(Insertable):
    
    title: str
    date: datetime
    timeRange: TimeRange
    description: str
    category: str
    term: str 
        
    def __str__(self):
        return  f"title: {self.title} | date:{self.date} | start:{self.timeRange.openingStr()} | end:{self.timeRange.closingStr()} | description:{self.description} | category:{self.category} | term:{self.term}"

    
    def insertInto(self, table, connection, commit=True):
        attrs = [["title",  self.title],
                 ["date",   self.date],
                 ["startTime", self.timeRange.openingStr()],
                 ["endTime", self.timeRange.closingStr()],
                 ["category", self.category],
                 ["term",   self.term],
                 ["description", self.description]]
        Event._insertIntoHelper(table, connection, attrs, commit)
       
