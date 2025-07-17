import sqlite3
import requests
from bs4 import BeautifulSoup
import pymysql.cursors
import re
import datetime
import zlib

from Utilities.WebConnectors import formConnections

TODAY = datetime.datetime.now().strftime("%Y-%m-%d")
url = 'https://furman.cafebonappetit.com/cafe/' + TODAY

def getID(meal, name, station):
    itemStr = f'{meal}{name}{station}'
    return zlib.crc32(itemStr.encode('utf-8')) % 2147483647

r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, features="html.parser")

#Create dictionary of list Breakfast:[(item,station),(item,sta)],Lunch:[
menu = {}

for mealBlock in soup.find_all('section', attrs={'class':re.compile("^panel s-wrapper site-panel site-panel--daypart")}):
        mealMenu = []  #list of main elements on menu
        mealName = mealBlock.find('h2', attrs={'class':'panel__title site-panel__daypart-panel-title'}).string
#        print(mealName)
      
        #only scrape the first tab's worth of data - no "additional"s
        mealSpecialsTab = mealBlock.find('div',attrs={'class':'site-panel__daypart-tab-content'})
        #for each 'item' on the main menu for this meal...
        for item in mealSpecialsTab.find_all ('div',            attrs={'class':'site-panel__daypart-item'}):
#            itemNameArray = []
            
            #find item's title
            for string in item.find('button', attrs={'class':'h4 site-panel__daypart-item-title'}).stripped_strings:
                itemName = string
#                print ("   "+itemName)

            
            #find item's station
            itemStation = item.find('div', attrs={'class':'site-panel__daypart-item-station'}).string
            itemStation = itemStation.replace("@","")
            itemStation = itemStation.title()
            
            mealMenu.append((itemName, itemStation))
            
        menu[mealName] = mealMenu
            
#print(menu)

connection = formConnections()

with connection.cursor() as cursor:
    try:
        cursor.execute('DELETE FROM "DHmenu"')
        for meal in menu:
            for item in menu[meal]:
                name = item[0]
                station = item[1]
                itemID = getID(meal, name, station)
                
                sql = """
                    INSERT INTO "userRatings" ("itemID") 
                    VALUES (%s)
                    ON CONFLICT ("itemID") DO NOTHING
                """
                cursor.execute(sql, (itemID,))

                sql = """
                    INSERT INTO "DHmenu" 
                    ("itemID", "meal", "itemName", "station") 
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(sql, (itemID, meal, name, station))
                
        connection.commit()
    except Exception as e:
        connection.rollback()
        raise Exception(f"Database operation failed: {str(e)}")