#!/bin/sh
/usr/local/bin/python3 /app/AthleticsScraper.py ; /usr/local/bin/python3 /app/dhmenu.py ; /usr/local/bin/python3 /app/diningHours.py ; 
/usr/local/bin/python3 /app/eventsScraper.py ; /usr/local/bin/python3 /app/HoursOpenScrapers.py ; /usr/local/bin/python3 /app/ImportantDScraper.py ;
/usr/local/bin/python3 /app/LibrariesHoursScraper.py ; /usr/local/bin/python3 /app/NewsScraper.py ; /usr/local/bin/python3 /app/RouteScraper.py ; 
/usr/local/bin/python3 /app/VehicleScraper.py ; /usr/local/bin/python3 /app/DBCleaner.py ; /usr/local/bin/python3 /app/WeatherScraper.py ;