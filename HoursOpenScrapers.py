# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:56:40 2020

@author: Ethan
This script will scrape hours from several webpages, format/clean them, and update the database.
"""

from dateutil.parser import parse
import datetime 
from Utilities.TimeClasses import Schedule, TimeRange
import re
import Utilities.WebConnectors as WebConnectors
from typing import List
from abc import abstractmethod


# list of links we need hours data from
links = {"trone":"https://www.furman.edu/campus-life/trone-student-center/",
"library":"https://libguides.furman.edu/library/hours",
"earle":"https://www.furman.edu/offices-services/student-health-center/hours-and-locations/",
"PAC":"https://www.furman.edu/campus-recreation/facilities-hours/",
"Enrollment":"https://www.furman.edu/enrollment-services/contact/",
"Counseling":"https://www.furman.edu/counseling-center/appointment/",
"Bon Appetit": "https://furman.cafebonappetit.com/cafe/"}

SCHEDULE_TABLE = "buildingHours"
BUILDING_INFO_TABLE = "buildingLocations"

class TimesScraper(WebConnectors.Scraper):
    """
    """
    def parseDaysFromRange(dayRange):
        
        if "–" not in dayRange and "-" not in dayRange:
            return [Schedule.dayNameOf(dayRange.strip())]
        
        days = dayRange.split("–" if "–" in dayRange else "-")
        start = Schedule.dayNameOf(days[0])
        end = Schedule.dayNameOf(days[1])
        started = False
        dayList = []
        for day in Schedule._daysOfWeek * 2:
            if day == start:
                started = True
            if started:
                dayList.append(day)
                if day == end:
                    break
        return dayList
    
    """ 
        Parses a time in the formatting of "7 am - 3 pm" or variants 
        thereof (such as using "a.m.", "to" instead of "-", "noon" for 12 pm, etc.)
        into 24-hour HH:MM:SS format. If time range is "closed" or non-valid,
        will return 00:00:00 for both values. 
        
        Attributes:
            timeRanges: str encoding a range of times, of the general
                form "Start am - End pm". The following formats are correctly parsed:
                    8-11am
                    9am-3pm
                    9:00 am - 3:00 pm
                    3-5pm
                    closed
                    9 am to 11 am, 12:30 pm to 11 pm
                    5am to noon
                    
               The following formats are not correctly parsed:
                   0500 - 1800
                   8-11
    """
    def parseTimeOpened(timeRanges: str):
        
        timeRanges = timeRanges.lower()
        
        ## Scans string for each element in non-primary elements in list
        ## and replaces with first element in list.
        ## E.g. [["a","A", "@"]] would look for all "A" and "@", then replace them
        ## with "a"  
        eqivs = [["12 am - 12 am", "closed"],
                 [",", "&", "and", ";"],
                 ["-", "–", "to"],
                 ["12 pm", "noon"],
                 ["","."]]    
        for eqv in eqivs:
            for ele in eqv[1:]:
                timeRanges = timeRanges.replace(ele, eqv[0])
                
        ## Commas delimit a split time range, i.e. 8 am - 5 pm, 7 pm - 9:30 pm
        timeRanges = timeRanges.split(",")
        times = []
        for t in timeRanges:
            ## Dashes seperate start and stop time, i.e. 8 am - 5 pm
            splits = t.split("-")
            try:
                ## If am/pm is not provided for opening time, i.e. 12 - 3pm,
                ## use the pm if closing time has pm in it, otherwise 
                ## uses am (i.e. 8-11 is assumed to mean in the morning)
                if all(a not in splits[0] for a in ["am", "pm"]):
                    if "pm" in splits[1]:
                        splits[0] += "pm"
                    else:
                        splits[0] += "am"
                        if "am" not in splits[1]:
                            splits[1] += "am"
                if all(a not in splits[1] for a in ["am", "pm"]) \
                        and "pm" in splits[0] :
                    splits[1] += "pm"
                
                ## Parses times, builds TimeRange, and adds to open time lists.
                v = TimeRange(parse(splits[0]), parse(splits[1]))
                times.append(v)
            except Exception as e:
                print(e)
                print(timeRanges)
                print("Failed to parse open-close times; placing failed time.")
                times.append(TimeRange.Failed())
        return times
    
    @abstractmethod
    def _pull() -> List[Schedule]:
        raise NotImplementedError()
        
## TODO: Change Bell Tower Bookstore
## -> Bell Tower Bookstore & Bistro in buildingLocations table
class TroneScraper(TimesScraper):    
    
    def parseTroneTitle(container):
        title = container.find("h2", {"class", "module-content-block-cta-contents-title m-0"})
        title = title.string.strip()
        return title
    
    """ Pulls opening times from Trone's website for Trone, Bookstore, and P2X """
    def _pull(self) -> List[Schedule]:
         page_soup = TroneScraper.getSoup(links["trone"])
         containers = page_soup.find_all("div",{"class","module-content-block-cta"})
         schedules = []
         for c in containers:
             title = TroneScraper.parseTroneTitle(c)
             
             ## Skips these cases because they either don't have times
             ## or because more accurate times are gotten from Bon Appetit's site.
             if title.lower() == "Plan an Event".lower() or \
                   "paladen" in title.lower() or \
                   "paddock" in title.lower():
                 continue
             sched = Schedule(title)
             hoursText = str(c.find("p").get_text())
             dayRangeTexts = hoursText.split("\n")
             for d in dayRangeTexts:
                 info = d.split(":")
                 dayNames = TroneScraper.parseDaysFromRange(info[0])
                 timeRange = TroneScraper.parseTimeOpened(info[1])
                 for t in timeRange:
                     sched.addDayRangeTime(dayNames, t)
             schedules.append(sched)
         return schedules
     
class EarleScraper(TimesScraper):
    
    """ Pulls opening hours from Earle Health"""
    def _pull(self) -> List[Schedule]:
         """ Returns hours info for Earle """
         sched = Schedule("Earle Health Center")
         page_soup = EarleScraper.getSoup(links["earle"])
         container = page_soup.find("div",{"class","module-content-block-wysiwyg"})
         pTags = container.find_all("p")
         ## Only gets first two tags
         for tag in pTags[0:2]:
             ## Removes unnecessary elements, no clue how
             [s.extract() for s in tag(['strong'])]
             ## Cleans string
             tag = str(tag.get_text()) \
                         .replace("<br/>","\n") \
                         .replace("864.522.2000", "") \
                         .strip() \
                         .split("\n")
    
             timePeriod = tag[0].strip()
             for dayrange in tag[1:]:
                 text = dayrange.replace("&", ",") \
                                .split(",")
                 daysOpened = EarleScraper.parseDaysFromRange(text[0])
                 for times in text[1:]:
                     timeRange = EarleScraper.parseTimeOpened(text[1])
                     sched.addDayRangeTime(daysOpened, 
                        timeRange, period = timePeriod if \
                            timePeriod != "Academic Year" else Schedule._defaultPeriod)
         return [sched]

class PACScraper(TimesScraper):
    
    def _parseRow(row, sched):
        dayrange = row.find("th").get_text()
        days = PACScraper.parseDaysFromRange(dayrange)
        cells = row.find_all("td")
        for cel in cells:
            period = cel('div')[0].extract().get_text()
            timerange = cel.get_text().strip()
            timeRange = PACScraper.parseTimeOpened(timerange)
            if period == "Fall/Spring":
                sched.addDayRangeTime(days, timeRange)
            else:
                sched.addDayRangeTime(days, timeRange, period = period)
    
    def _parseTable(table):
        tab = table.find("table")
        name = table.find("div",attrs={"class":"col-12 table-header-title"}) \
                    .get_text() \
                    .strip()
        if name == "Fitness Center Hours":
            name = "The PAC"
        if name == "Aquatic Hours":
            name = "Aquatic Center"
        sched = Schedule(name)
        
        rows = tab.find("tbody") \
                  .find_all("tr")
        for r in rows:
            PACScraper._parseRow(r, sched)
        return sched
        
    """ Pulls opening hours from the PAC's website for the main gym and the aquatic center. """
    def _pull(self) -> List[Schedule]:
        scheds = []
        page_soup = PACScraper.getSoup(links["PAC"])
        containers = page_soup.find_all("div",attrs={"aria-label": "table"})
        for c in containers:
            scheds.append(PACScraper._parseTable(c))
        return scheds


class EnrollmentScraper(TimesScraper):
    """ Pulls opening hours for Enrollment Services. """ 
    def _pull(self) -> List[Schedule]:
        sched = Schedule("Enrollment Services")
        page_soup = EnrollmentScraper.getSoup(links["Enrollment"])
        container = page_soup.find("div",attrs={"class":"module-content-block-wysiwyg"})
        pTags = container.find_all("p")
        text = pTags[1]
        [s.extract() for s in text(['strong','p'])]
        text = text.get_text() \
                     .strip() \
                     .split("\n")
        for line in text:
            line = line.split(",")
            days = EnrollmentScraper.parseDaysFromRange(line[0])  
            hours = [EnrollmentScraper.parseTimeOpened(a) for a in line[1:]]
            for h in hours:
                for t in h:
                    sched.addDayRangeTime(days, t)
            
        return [sched]

class CounselingScraper(TimesScraper):
    """ Pulls hours info for counseling center """
    def _pull(self) -> List[Schedule]:
        sched = Schedule("Counseling Center")
        page_soup = CounselingScraper.getSoup(links["Counseling"])
        container = page_soup.find("div",attrs={"class":"module-content-block-wysiwyg"})
        lines = container.find_all(["p", "h2"])
        ln = -1
        for i, line in enumerate(lines):
            if line.name == 'h2' and "hours" in line.get_text().lower():
                ln = i + 1
                break
        times = lines[ln].get_text() \
                        .split("\n")
        for i, t in enumerate(times):
            times[i] = re.split("\xa0", t)[0] \
                         .replace(";", ",") \
                         .replace("and", "-") \
                         .split(",")
            days = CounselingScraper.parseDaysFromRange(times[i][0])
            ranges = ",".join(times[i][1:])
            ranges = CounselingScraper.parseTimeOpened(ranges)
            sched.addDayRangeTime(days, ranges)
        return [sched]


class BonAppetitScraper(TimesScraper):
    """ Parses the hours for the restraunts listed on the Bon Appetit website. """
    def _parseHours(scheds, soup, dayOfWeek):
        
        hours = soup.find("div",attrs={"class":"site-panel__cafeinfo-inner"})
        locations = hours.find_all("div", attrs={"class":"c-accordion__row site-panel__cafeinfo-row"})
        for loc in locations:
            title = loc.find("span", attrs={"data-name":"title"}) \
                        .getText() \
                        .strip()
            if title == "P-Den":
                title = "PalaDen"
            if title not in scheds:
                scheds[title] = Schedule(title)
                
            dayParts = loc.find_all("li", attrs={"class":"site-panel__cafeinfo-dayparts-item"})
            for dp in dayParts:
                time = dp.find("div", attrs={"class":"site-panel__cafeinfo-daypart-status"}) \
                            .getText() \
                            .lower() \
                            .replace("served from", "") \
                            .strip()
                ranges = BonAppetitScraper.parseTimeOpened(time)
                scheds[title].addDayRangeTime([dayOfWeek], ranges)
                
    """ Pulls hours for all Bon Appetit restraunts listed on their website. """
    def _pull(self) -> List[Schedule]:
        scheds = {}
        today = datetime.date.today()
        for days in range(0,7):
            day = today + datetime.timedelta(days=days)
            date = day.strftime("%Y-%m-%d")
            soup = BonAppetitScraper.getSoup(f'{links["Bon Appetit"]}{date}/')
            BonAppetitScraper._parseHours(scheds, soup, day.strftime("%A"))
        return [v for s, v in scheds.items()]

def main():
    
    scrapers = [TroneScraper(), PACScraper(), EarleScraper(),
                EnrollmentScraper(), CounselingScraper(), 
                BonAppetitScraper()]
    """ Here, we read all pages, and deal with the database """
    # each page is read w/ separate functions because of their formatting

    connection = WebConnectors.formConnections()

    for scraper in scrapers:
        newscheds = scraper.tryPull()        
        for n in newscheds:
        
            parsesuccess = not scraper.didFail() and n.noFails()
            print('----------------------------')
            print(n.name)
            print("Successful parse." if parsesuccess else "Failed in parsing.")
            if not parsesuccess:
                continue
            
            if connection is None:
                continue
            updatesuccess = n.updateInto(SCHEDULE_TABLE, BUILDING_INFO_TABLE, connection, onlyMainSchedule=True)
            print("Successful update." if updatesuccess else "Failed to update.")
            
    if connection != None:
        connection.close()


if __name__ == "__main__":
    main()


