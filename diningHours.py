import requests
from bs4 import BeautifulSoup
import pymysql.cursors
import re
from datetime import datetime
import calendar
from pytz import timezone

from Utilities.WebConnectors import formConnections

tz = timezone('EST')
dt = datetime.now(tz)


def findDay(dt):
    dayOfWeek = dt.weekday()
    return (calendar.day_name[dayOfWeek])

CURRENT_WEEKDAY_INT = dt.weekday()
CURRENT_WEEKDAY_STRING = findDay(dt)[0:3]
url = 'https://furman.cafebonappetit.com'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, features="html.parser")

# filename = '/home/csdaemon/aux/userCred.txt' 
# file = open(filename, 'r')
# credentials = file.readlines()
# username = credentials[0].strip()
# password = credentials[1].strip()

# connection = pymysql.connect(host='localhost', user=username, password=password, db='FUNOW',
# charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
connection = formConnections()

fullnames = []
meals = []
starts = []
ends = []
i = 0
j = 0
p = re.compile('pm')

for a in soup.find_all('div', attrs={'class':'c-accordion__row site-panel__cafeinfo-row'}):
    mealsTemp = []
    startsTemp = []
    endsTemp = []
    fullnames.append(a.find(attrs={'data-name':'title'}).string.strip())
    meals.append('')
    starts.append('')
    ends.append('')
    if a.find(attrs={'class':'site-panel__cafeinfo-header-extra site-panel__cafeinfo-header-extra--closed'}) != None:
        meals[i] = ['']
        starts[i] = ['']
        ends[i] = ['']
        i += 1
        continue
    cont = a.find('ul', attrs={'class':'site-panel__cafeinfo-dayparts'})
    if cont != None:
        cont = cont.find_all('li', attrs={'class':'site-panel__cafeinfo-dayparts-item'})
        for item in cont:
            mealsTemp.append(item.find('div', attrs={'class':'site-panel__cafeinfo-daypart-name'}).string)
            time = item.find('div', attrs={'class':'site-panel__cafeinfo-daypart-status'}).string
            time = re.split("Served from | - ", time)
            time = list(filter(None,time))
            #print(time)
            for k in range(0,2):
                time[k] = re.split(":| ", time[k])
                if time[k][2] == "pm" and time[k][0] != '12':
                    time[k][0] = int(time[k][0]) + 12
            startsTemp.append(str(time[0][0]) + ':' + str(time[0][1]))
            endsTemp.append(str(time[1][0]) + ':' + str(time[1][1]))
    else:
        startsTemp.append("00:00")
        endsTemp.append("00:00")
    if len(mealsTemp) < 2:
        meals[i] = ['Open']
    else:
        meals[i] = mealsTemp
    starts[i] = startsTemp
    ends[i] = endsTemp
    i += 1
    

D = {}
for i in range (0, len(fullnames)):
	D[fullnames[i]] = [meals[i], starts[i], ends[i]]
print(D)

try:
    for name in D:
        with connection.cursor() as cursor:
            try:
                sql = 'SELECT id FROM "foodService" WHERE fullname = %s'
                cursor.execute(sql, (name,))
                result = cursor.fetchone()
                
                if not result:
                    continue  
                    
                id = result[0]  
                
                sql = 'DELETE FROM "times" WHERE id = %s'
                cursor.execute(sql, (id,))
                
                for j in range(len(D[name][0])):
                    if not D[name][1][j]:  
                        sql = """INSERT INTO "times" 
                                (id, "dayOfWeek", "dayOrder") 
                                VALUES (%s, %s, %s)"""
                        cursor.execute(sql, (id, "Mon-Sun", 0))
                    else:
                        sql = """INSERT INTO "times" 
                                (id, meal, start_time, end_time, "dayOfWeek", "dayOrder") 
                                VALUES (%s, %s, %s, %s, %s, %s)"""
                        cursor.execute(sql, (
                            id, 
                            D[name][0][j], 
                            D[name][1][j], 
                            D[name][2][j], 
                            "Mon-Sun", 
                            0
                        ))
                
                connection.commit()
            
            except Exception as e:
                connection.rollback()
                print(f"Error processing {name}: {str(e)}")
                raise  
finally:
    connection.close()