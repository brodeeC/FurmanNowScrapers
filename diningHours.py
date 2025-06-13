import requests
from bs4 import BeautifulSoup
import pymysql.cursors
import re
from datetime import datetime
import calendar
from pytz import timezone

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

filename = '/home/csdaemon/aux/userCred.txt' ## BUG: File not found.
file = open(filename, 'r')
credentials = file.readlines()
username = credentials[0].strip()
password = credentials[1].strip()

connection = pymysql.connect(host='localhost', user=username, password=password, db='FUNOW',
charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

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
	#for name in fullnames:
	#	with connection.cursor() as cursor:
	#		sql = "insert `foodService` (`fullname`) values (%s)"
	##		cursor.execute(sql, (name))
	#	connection.commit()
	i = 0
	for name in D:
		with connection.cursor() as cursor:
			sql = "SELECT id from foodService where fullname = (%s)"
			cursor.execute(sql, name)
			id = cursor.fetchone()
			id = id['id']
			sql = "delete from `times` where `id` = (%s)"
			cursor.execute(sql, (id))
		for j in range(0, len(D[name][0])):
			print(j)
			with connection.cursor() as cursor:
				if  starts[i][j] == "":
					sql = "insert `times` (`id`, `dayOfWeek`, `dayOrder`) values (%s, %s, %s)"
					cursor.execute(sql, (id, "Mon-Sun", 0))
				else:
					sql = "insert `times` (`id`, `meal`, `start`, `end`, `dayOfWeek`, `dayOrder`) values (%s, %s, %s, %s, %s, %s)"
					cursor.execute(sql, (id, meals[i][j], starts[i][j], ends[i][j], "Mon-Sun", 0))
					print(meals[i][j])
				connection.commit()
				print('committed')
		i += 1
except Exception as e:
	connection.rollback()
	print(e)
finally:
	connection.close()

