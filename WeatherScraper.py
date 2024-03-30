# -*- coding: utf-8 -*-
"""
Modified Jan 23 2024

@author: Michael Peeler

Created May 18 2021 

@author: BCatron

Scrapes weather information from api.weather.gov  (National Weather service) for
the Furman "gridpoint"
Updates a local JSON file with  {'format':'weather','results':'---','error':'???'}

Dependencies: urllib, json, time, pymysql, feedparser
"""

import json
import urllib.request
import feedparser
from Utilities.WebConnectors import Scraper, FailedWebPullException, formConnections
from Utilities.SQLQueryClasses import Clearable, Insertable
from dataclasses import dataclass
from math import floor
import traceback
from datetime import datetime

#find details at www.weather.gov/documentation/services-web-api
FORECAST_URL = "https://api.weather.gov/gridpoints/GSP/61,45/forecast?units=us"
CURRENT_TEMP_URL = "http://rss.accuweather.com/rss/liveweather_rss.asp?locCode=29613"
WEATHER_TABLE = "weather"

@dataclass
class Forecast(Clearable, Insertable):
    idnum : int
    day : str
    start : str
    end : str
    isDaytime : str
    currTemp : int
    highTemp : int
    lowTemp : int
    tempUnit : str
    precipPct : str
    windSpeed : str
    windDirection : str
    shortForecast : str
    detailedForecast : str
    alert : str
    emoji : str
    
    def updateInto(self, table, connection, commit=True):
        self.clearFrom(table, connection, False)
        self.insertInto(table, connection, False)
        if commit:
            connection.commit()
        
    def clearFrom(self, table, connection, commit=True):
        Clearable._clearHelper(table, connection, [["id", self.idnum]], commit)
        
    def insertInto(self, table, connection, commit=True):
        # List of all table field : forecast dictionary key pairs
        # Ex. value in forecast["number"] will be inserted into
        # the field "id" in the table.
        attrs = [["id",        self.idnum],
                 ["day",        self.day], 
                 ["start",      self.start],
                 ["end",        self.end],
                 ["isDayTime",  self.isDaytime],
                 ["tempCurrent", self.currTemp],
                 ["tempHi",     self.highTemp],
                 ["tempLo",     self.lowTemp],
                 ["unit",       self.tempUnit],
                 ["precipitationPercent", self.precipPct],
                 ["windSpeed",  self.windSpeed],
                 ["windDirection", self.windDirection],
                 ["shortForecast", self.shortForecast],
                 ["detailedForecast", self.detailedForecast],
                 ["alert",      self.alert],
                 ["emoji",      self.emoji]]
                
        Insertable._insertIntoHelper(table, connection, attrs, commit)
    

class WeatherScraper(Scraper):

    def _matchEmoji(forecast, isDaytime):
        # List of all strings we are checking for, and which emojis they correspond to.
        # Run in-order, so if one string is a substring of another, it should go later.
        # Final empty string is default emoji.
        
        day_emojis =     [["mostly sunny", "0x1F324"],  # Sun behind small cloud
                          ["partly sunny", "0x1F325"],  # Sun behind larger cloud
                          ["sunny", "0x1F31E"],         # Sun
                          ["partly cloudy", "0xF1324"], # Sun behind larger cloud
                          ["mostly cloudy", "0xF1325"], # Sun behind cloud
                          ["cloudy", "0x2601"],         # Cloud
                          [ ["scattered", "showers"], "0x1F326"],       # Sun behind rain clouds
                          [ ["thunderstorms", "showers"], "0x26C8"],    # Rain and thunder clouds
                          ["showers", "0x1F327"],       # Rain cloud
                          ["snow", "0x1F328"],          # Cloud with snow
                          ["DEFAULT", "0x1F31E"]]       # Sun, default
        
        night_emojis =  [["DEFAULT", "0x1F311"]]        # Moon, default
        
        forecast = forecast.lower()
        
        if isDaytime:
            for encode in day_emojis:
                # Turns single-element encodings into a list
                if type(encode[0]) is str:
                    encode[0] = [encode[0]]
                # Emoji is used if the description includes all elements of the encoding
                if all(strings in forecast for strings in encode[0]):
                    return encode[1]
        else:
            ## Displays phase of the moon at night.
            now = datetime.datetime.now()
            diff = now - datetime.datetime(2001, 1, 1)
            days = diff.days + (diff.seconds / 86400)
            lunations = (0.20439731 + (days * 0.03386319269)) % 1
            index = (lunations * 8) + 0.5
            index = floor(index)
            moonPhaseEmojis = ['0x1F311', # New Moon
                               '0x1F312', # Quarter Waxing
                               '0x1F313', # Half Waxing
                               '0x1F314', # Three-Quarters Waxing
                               '0x1F315', # Full
                               '0x1F316', # Three-Quarters Waning
                               '0x1F317', # Half Waning
                               '0x1F318'  # Quarter Waning
                               ]
            return moonPhaseEmojis[int(index) & 7]
                        
        # Returns default
        return day_emojis[-1][1] if isDaytime else night_emojis[-1][1]
    
    def _pullCurrentTemperature(pageURL):
        try:
            feed  = feedparser.parse(pageURL)
            entry = feed.entries[0].title
            temp  = entry.split(":")[-1]
            temp  = temp.replace(" ","") \
                        .replace("F","")
            return int(temp)
        except:
            raise FailedWebPullException("Current Temperature Web Pull Failed.")
    
    def _pairForecastData(first, second):
     
        temp1 = first["temperature"]
        temp2 = second["temperature"]
        if (temp1 > temp2):
          first["tempHi"], second["tempHi"] = temp1, temp1
          first["tempLo"], second["tempLo"] = temp2, temp2
        else:
          first["tempHi"], second["tempHi"] = temp2, temp2
          first["tempLo"], second["tempLo"] = temp1, temp1            
        return first, second  
    
    def _parsePrecipPct(detailedForecast):
        if detailedForecast.count("%") > 0:
            index = detailedForecast.index("%")
            precip = detailedForecast[index-2:index+1]
            return precip
        return ""           

    def _toForecast(pulled):
        keys = ["number", "name", "startTime", "endTime", "isDaytime",
                "tempCurrent", "tempHi", "tempLo", "temperatureUnit", 
                "precipitationPercent", "windSpeed", 
                "windDirection", "shortForecast",
                "detailedForecast", "alert", "emoji"]
        
        return Forecast(*tuple(Scraper.maybeGetValue(pulled, key) for key in keys))

    def _pull(self):
    #  Open URL from pageURL which should return a json    
        try:
          
          with urllib.request.urlopen(FORECAST_URL) as response:
              result = response.read()
           
          #convert to json   TODO: error handling/alert when converting to JSON
          encoding = response.info().get_content_charset('utf-8')
          jsondata = json.loads(result.decode(encoding))
        
          """
            key values of interest:
                'name'
                'startTime' - date: forecast applicable start date/time
                'shortForecast' - string: one or two words "Mostly Sunny" or "Clear"
                temperature - int: numeric format
                temperatureUnit - string:'F'  in our case
                isDayTime - boolean : 6am to 6pm is true
                windSpeed - string : short string of windspeed
                detailedForecast - string: long sentenct of temp and wind
          """
          per = jsondata['properties']["periods"]
          current = WeatherScraper._pullCurrentTemperature(CURRENT_TEMP_URL)

          first, second = WeatherScraper._pairForecastData(per[0], per[1])
          forecasts = []
          for pulled in [first, second]:
              
              pulled["tempCurrent"] = current
              pulled["isDaytime"] = bool(pulled["isDaytime"])
              pulled["emoji"] =  WeatherScraper._matchEmoji(pulled["detailedForecast"], pulled["isDaytime"])
              pulled["precipitationPercent"] = WeatherScraper._parsePrecipPct(pulled["detailedForecast"])
              pulled["alert"] = ""
              
              forecasts.append(WeatherScraper._toForecast(pulled))
              
          return forecasts
        except:
            traceback.print_exc()
            raise FailedWebPullException("Forecast Web Pull Failed.")

def main():

    forecast = WeatherScraper().tryPull()
    print(forecast)

    connection = formConnections()
    for f in forecast:
        f.updateInto(WEATHER_TABLE, connection)


if __name__ == "__main__":
    main()
