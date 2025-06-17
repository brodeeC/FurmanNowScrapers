import requests
from bs4 import BeautifulSoup
import pymysql.cursors
import re
import datetime

from Utilities.WebConnectors import formConnections

TODAY = datetime.datetime.now().strftime("%Y-%m-%d")
url = 'https://furman.cafebonappetit.com/cafe/' + TODAY

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

#UPDATE THE DATABASE
# filename = '/home/csdaemon/aux/userCred.txt'
# file = open(filename, 'r')
# credentials = file.readlines()
# username = credentials[0].strip()
# password = credentials[1].strip()
# connection = pymysql.connect(host='localhost',
#          user=username, password=password,
#          db='FUNOW',
#          charset='utf8mb4',
#          cursorclass=pymysql.cursors.DictCursor)
connection = formConnections()

try:
    with connection.cursor() as cursor:
        removeSQL = "DELETE FROM DHmenu;"
        cursor.execute(removeSQL)
        for meal in menu:
            for item in menu[meal]:
                name = item[0]
                station = item[1]
                sql = "insert DHmenu (`meal`, `itemName`, `station`) values (%s, %s, %s)"
                cursor.execute(sql, (meal, name, station))
    connection.commit()
except:
    connection.rollback()
    print(cursor.error)
finally:
    connection.close()


#try:
#	for name in fullnames:
#			sql = "insert `foodService` (`fullname`) values (%s)"
#			cursor.execute(sql, (name))
#		connection.commit()
#	i = 0
#	for name in D:
#		with connection.cursor() as cursor:
#			sql = "SELECT id from foodService where fullname = (%s)"
#			cursor.execute(sql, name)
#			id = cursor.fetchone()
#			id = id['id']
#		for j in range(0, len(D[name][0])):
#			with connection.cursor() as cursor:
#				sql = "insert `times` (`id`, `meal`, `start`, `end`) values (%s, %s, %s, %s)"
#				cursor.execute(sql, (id, meals[i][j], starts[i][j], ends[i][j]))
#		connection.commit()
#		i += 1
#except:
#	connection.rollback()
#finally:
#	connection.close()