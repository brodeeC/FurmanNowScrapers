# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:03:05 2024

@author: mdavi
"""

import feedparser
from datetime import date, timedelta
from dateutil.parser import parse as parseTime
from html import unescape
from unicodedata import normalize
from Utilities.TimeClasses import Event, TimeRange
from Utilities.WebConnectors import formConnections

START_STOP_TIME_STRING = " – "
IMPORTANT_DATES_TABLE = "importantDates"
WEBCALENDAR_LINK = "https://25livepub.collegenet.com/calendars/university-academic-calendar.rss"
FAILED_DATE_PARSE = "FAILED || DATE || PARSE"
END_TAG = "<br/>"


# Takes as input the "description" field of the RSS feed and determines
# which calendar the event belongs to; most fall under either "Registrar" or
# "Graduate Studies".
def parseCategory(description):
    
    org = "Organization</b>:"
    if org in description:
        trunc = sliceAfterSubstring(description, org) 
        trunc = sliceBeforeSubstring(trunc, END_TAG)
        if "pm" in trunc:
            print(description)
            print(trunc)
            print()
        return trunc.strip() if trunc.strip() != "Registrar" else "Academic Dates & Holidays"
    return "Academic Dates & Holidays"

def sliceBeforeSubstring(full, sub, reverse=False):
    if reverse:
        return full[:full.rfind(sub)]
    else:
        return full[:full.find(sub)]

def sliceAfterSubstring(full, sub, reverse=False):
    if reverse:
        return full[full.rfind(sub) + len(sub):]
    else:
        return full[full.find(sub) + len(sub):]

def parseDate(temporal):
    temp = sliceBeforeSubstring(temporal, ",", reverse=True)
    try:
        dt = parseTime(temp)
        dt = dt.strftime("%Y-%m-%d")
    except:
        dt = FAILED_DATE_PARSE
    return dt

def parseStartEnd(temporal):
    time = sliceAfterSubstring(temporal, ", ", reverse=True).strip()
    times = time.split(START_STOP_TIME_STRING)
    for i, t in enumerate(times):
        if "am" not in t and "pm" not in t and i < len(times) - 1:
            if "am" in times[i + 1]: 
                t += "am"
            if "pm" in times[i + 1]:
                t += "pm"
        try:
            times[i] = parseTime(t)
        except:
            return TimeRange.Failed()
    if len(times) == 1:
        return TimeRange(times[0], times[0])
    else:
        return TimeRange(times[0], times[1])

def parseDatetime(description):
    endString = f"{END_TAG}{END_TAG}"
    trunc = sliceBeforeSubstring(description, endString)
    trunc = unescape(trunc).strip()
    dt = parseDate(trunc)
    timeRange = parseStartEnd(trunc)
    return dt, timeRange

def parseDescript(description):
    if "<p>" in description:
        trunc = sliceAfterSubstring(description, "<p>")
        trunc = sliceBeforeSubstring(trunc, "</p>")
        trunc = trunc.strip()
        return trunc
    else:
        return ""

def parseTerm(description):
    term = sliceAfterSubstring(description, f"<b>Event Name</b>")
    term = sliceBeforeSubstring(term, END_TAG).replace(":", " ")
    term.strip()
    return term

def getFeed(link):
    eventFeed = feedparser.parse(link)
    return eventFeed

def parseEvents(eventFeed):
    parsed = []
    for entry in eventFeed.entries:
        raw =           unescape(entry["description"])
        raw =           normalize("NFKD", raw)
        title =        entry.title.replace("“", '"') \
            .replace('”', '"') \
            .replace('’', "'") \
            .replace("–", "-")
        dt, timeRange =  parseDatetime(raw)
        description =     parseDescript(raw)
        category =        parseCategory(raw)
        term =         parseTerm(raw)
        parsed.append(Event(title, dt, timeRange, description, category, term)) 
    return parsed

def purgeOldEvents(connection):
    sql = f"DELETE FROM `{IMPORTANT_DATES_TABLE}`"
    with connection.cursor() as cursor:
        try:
            cursor.execute(sql)
            connection.commit()     
        except:
            connection.rollback()
            print("Failed to purge.")

def insertNewEvents(events, connection):
    cutoffdate = date.today() - timedelta(7)
    for e in events:
        # Checks if the event is occuring at some point after one week ago; if so,
        # adds to database.  
        print(cutoffdate, parseTime(e.date).date())
        if cutoffdate - parseTime(e.date).date() < timedelta(0):
            e.insertInto(IMPORTANT_DATES_TABLE, connection)
            
def verifyWorking(events):
    event_count = len(events)
    failed_times = 0
    failed_dates = 0
    for e in events:
        if e.timeRange == TimeRange.Failed():
            failed_times += 1
        if e.date == FAILED_DATE_PARSE:
            failed_dates += 1
    pct_failed_time = 0 if event_count == 0 else round(100 * failed_times / event_count, 2)
    pct_failed_date = 0 if event_count == 0 else round(100 * failed_dates / event_count, 2)
    print(f"Time scraping failed in {failed_times} instances, representing {pct_failed_time} % ")
    print(f"Date scraping failed in {failed_dates} instances, representing {pct_failed_date} % ")

    
    if pct_failed_time == 0 and pct_failed_date:
        return "WORKING"
    elif pct_failed_time < 50 and pct_failed_date < 50:
        return "DAMAGED"
    else:
        return "BROKEN"
    
def main():
    eventFeed = getFeed(WEBCALENDAR_LINK)  
    events = parseEvents(eventFeed)
    status = verifyWorking(events)
    if status != "BROKEN":
        connection = formConnections()
        purgeOldEvents(connection)
        insertNewEvents(events, connection)
        connection.close()

if __name__ == "__main__":
    main()
