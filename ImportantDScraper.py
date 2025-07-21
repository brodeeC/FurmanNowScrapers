"""
Updated date scraper
This scraper uses beautiful soup to iterate over events and parse 
dates and times using functions from the old scraper.
"""


import feedparser
from bs4 import BeautifulSoup as soup
from html import unescape
from unicodedata import normalize
import re

from ImportantDateScraper import insertNewEvents, parseDate, parseStartEnd, purgeOldEvents, verifyWorking
from Utilities.TimeClasses import Event
from Utilities.WebConnectors import formConnections


def clean_field_value(text):
    if not text:
        return ''
    text = text.replace('\xa0', ' ')  # Convert non-breaking space
    text = re.sub(r'^[:\s]+', '', text)  # Remove leading colon and spaces
    return text.strip()

def parseItem(entry):
    raw_description = unescape(entry.get('description', ''))
    raw_description = normalize('NFKD', raw_description)
    souped = soup(raw_description, "html.parser")

    full_text = souped.get_text(separator=' ', strip = True)
    time_and_date = clean_field_value(full_text.split('Event Name')[0])

    fields = {}
    for b in souped.find_all("b"):
        label = b.get_text(strip = True).rstrip(':').lower()
        if b.next_sibling:
            raw_value = b.next_sibling
            value = clean_field_value(raw_value)
            fields[label] = value 

    dt = parseDate(time_and_date)
    time_range = parseStartEnd(time_and_date)

    event_name = fields.get("event name", '')
    term = f"  {event_name} "

    category = fields.get('organization', '')
    if category == "Registrar" or not category:
        category = "Academic Dates & Holidays"

    return Event(
        title = entry.get("title", "").strip(),
        date = dt,
        timeRange = time_range,
        description = "",
        category = category,
        term = term
    )

def parseEventsFromRSS(url):
    eventFeed = feedparser.parse(url)
    return [parseItem(entry) for entry in eventFeed.entries]


def main():
    URL = "https://25livepub.collegenet.com/calendars/university-academic-calendar.rss"
    eventFeed = parseEventsFromRSS(URL)
    status = verifyWorking(eventFeed)
    if status != "BROKEN":
        connection = formConnections()
        purgeOldEvents(connection)
        insertNewEvents(eventFeed, connection)
        connection.close()

if __name__ == '__main__':
    main()