# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 12:11:24 2024

@author: mdavi
"""
#WEb import program to pull a JSON file directly from server
#and load into database important fields
#Date: Summer 2021
#Original Author: BCatron
#Reads results from the AJAX source which Furmanpaladins.com uses for their calendar
#Parses the JSON results and update the database

#Example for one day https://furmanpaladins.com/services/responsive-calendar.ashx?type=events&sport=0&location=all&date=2021-08-13T00%3A00%3A00
#for this date
from WebConnectors import Scraper
import requests
from collections.abc import Iterable
from datetime import datetime
from datetime import date
from datetime import timedelta
import pymysql.cursors
import sys
from SQLQueryClasses import Insertable
from WebConnectors import formConnections
from dataclasses import dataclass
from dataclass_builder import (dataclass_builder, build)
from dateutil.parser import parse as parseDate

RECENT_DAYS_BACK = 3               #pick up events this old
OLD_DAYS_BACK = RECENT_DAYS_BACK-4  #will delete events older than this

Cursor = ""

@dataclass
class AthleticEvent(Insertable):
    date : datetime
    start : str
    sport : str
    sportAbbrev : str
    opponent : str
    locIndicator : str
    location : str
    conference : bool
    noplayText : str
    resultStatus : str
    resultFurScore : str
    resultOppScore : str
    prescoreInfo : str
    postscoreInfo : str
    sportURL : str
    
    def insertInto(self, table, connection, commit=True):
        try:
            attrs = [["eventdate", self.date.strftime("%Y-%m-%d %H:%M:%S")],
                     ["time", self.start],
                     ["conference", self.conference],
                     ["location_indicator", self.locIndicator],
                     ["location", self.location],
                     ["sportTitle", self.sport],
                     ["sportShort", self.sportAbbrev],
                     ["opponent", self.opponent],
                     ["noplayText", self.noplayText],
                     ["resultStatus", self.resultStatus],
                     ["resultUs", self.resultFurScore],
                     ["resultThem", self.resultOppScore],
                     ["prescore_info", self.prescoreInfo],
                     ["postscore_info", self.postscoreInfo],
                     ["url", self.sportURL]]
            AthleticEvent._insertIntoHelper(table, connection, attrs, commit)
        except pymysql.Error as e:
            print(e.args[0], e.args[1])
            print("Athletics event insertion failed:"+self.date+" "+self.sport)
        return
    
AthleticEventBuilder = dataclass_builder(AthleticEvent)

class AthleticsScraper(Scraper):
    

    ##Takes one JSON event
    def _processEvent(event):
        
        def maybeGetValStr(dct, *keys, default=""):
            return Scraper.maybeGetValue(dct, *keys, default=default)
        
        builder = AthleticEventBuilder()
        date = maybeGetValStr(event, "date")
        builder.date = parseDate(date)
        builder.start = maybeGetValStr(event, "time", default="All Day")
        
        builder.conference = maybeGetValStr(event, "conference")   #true or false
        
        builder.locIndicator = maybeGetValStr(event, "location_indicator") #H or A
        builder.location =  maybeGetValStr(event, "location")     #ignore if Home game
        builder.sport =     maybeGetValStr(event, "sport", "title")       #ex Men's Soccer
        builder.sportAbbrev = maybeGetValStr(event, "sport", "abbreviation")   #ex: MSOC
        builder.opponent =  maybeGetValStr(event, "opponent", "title")  
        builder.noplayText = maybeGetValStr(event, "noplay_text")       #ex: postponed or canceled (Sic)
       
        if builder.noplayText == "Canceled":
            builder.noplayText = "Cancelled"
            
        builder.resultStatus = maybeGetValStr(event, "result", "status") # W, L, or T
        builder.resultFurScore = maybeGetValStr(event, "result", "team_score") # Furman's Score
        builder.resultOppScore = maybeGetValStr(event, "result", "opponent_score") # Opponent's Score
        builder.prescoreInfo = maybeGetValStr(event, "result", "prescore_info") # ? no examples
        builder.postscoreInfo = maybeGetValStr(event, "result", "postscore_info") # i.e. Double Overtime
        builder.sportURL = maybeGetValStr(event, "result", "recap", "url", default="null") # Relavent link to news items
                
        return build(builder)
    
    def _pull(self):
        
        recent = str(date.today()- timedelta(days=RECENT_DAYS_BACK))
        athleticsURL = 'https://furmanpaladins.com/services/responsive-calendar.ashx?'\
                      +'type=events&sport=0&location=all&date='\
                      +recent\
                      +'T00%3A00%3A00'
                      
        # Making a get request - change User-agent to anything other than Python to allow
        response = requests.get(athleticsURL, headers={'User-Agent': 'Custom'})
          
        # check for good request response
        if response.status_code != 200:
            print ("Athletics unable to access URL" + response.status_code)
            return []

        jsonResponse = response.json()

        games = []
        #### add each event to database
        for adate in jsonResponse:
            events = adate["events"]   #list of events for a day
            if isinstance(events, Iterable):
               for ev in events:
                   games.append(AthleticsScraper._processEvent(ev))
        return games


def main():
    #BEGIN ---------------------------------------------
    #how far back to grab data

    events = AthleticsScraper().tryPull()
    #####connect to database for initial removal of old, old data
    connection = formConnections()
    try:
        with connection.cursor() as cursor:
            ### SHOULD WE DELETE ALL??  to prevent duplicates???
            sql = "DELETE FROM athletics"   #" WHERE eventDate<'"+olddate+"';"
            cursor.execute(sql)
        for e in events:
            e.insertInto("athletics", connection, commit=False)
        connection.commit()
    except:
        print ("Database connection/removal failed")
        sys.exit()
        ######               
    print(f"Athletics updated: {date.today()}")
    
if __name__ == "__main__":
    main()


