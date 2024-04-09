# -*- coding: utf-8 -*-
"""
Scrapes Academic Dates from
Created on Mon Jul 12 13:42:51 2021

@author: btison
"""
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
import pymysql
import feedparser
import re
from Utilities.WebConnectors import Scraper
from datetime import datetime
import datetime
import pytz

syncDin = "https://furman.campuslabs.com/engage/events.rss"
clp = "https://25livepub.collegenet.com/calendars/clp.rss"

#Convert EVENT time strings in GMT to eastern times
def gmtToEst (timestr):
    gmt = pytz.timezone('GMT')
    eastern = pytz.timezone('US/Eastern')
    date = datetime.datetime.strptime(timestr,'%a, %d %b %Y %H:%M:%S GMT')
    dategmt = gmt.localize(date)
    est = dategmt.astimezone(eastern)
    return est

def getSoup(link):
    """ Given a link, instantiate the page_soup parser and return it """
    # open connection w/ main page, read html
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(link,headers=hdr)
    uClient = urlopen(req)
    page_html = uClient.read()
    uClient.close()

    # instantiate html parser w/ html string, return
    page_soup = soup(page_html, features="html.parser")
    return page_soup

def clean(inputString):
    """ This is our generic cleaner to remove junk & HTML tags that are not used """
    junkTags = ['<h3 class="cta_blocks__title">','</h3>', '<p>', '</p>','864.522.2000', '</strong>', '<strong>',
                '<li>','</li>', '<span>', '</span>', '<span class="sr-only">', '<span aria-hidden="true">', 'Mon - Thu','\xa0']
    whitespaceTags = ['<br/>']
    for i in junkTags:
        inputString = (inputString.replace(i,''))
    for i in whitespaceTags:
        inputString = inputString.replace(i, ' ')
    inputString = inputString.replace('&amp;','&')
    inputString = inputString.replace('  ', ' ')
    return inputString
    
def to24hourFormat(st):
    st = st.strip()
    try:  #with space & am/pm "7:30 pm"
        st24 = datetime.datetime.strptime(st,"%I:%M %p")
    except:
        try: #with no space, but am/pm "7:20am"
            st24 = datetime.datetime.strptime(st,"%I:%M%p")
        except:
            try: #with no am/pm  "7:10"
                st24 = datetime.datetime.strptime(st,"%I:%M")
            except:
                try: #with only Hour and am/pm  "7am"
                    st24= datetime.datetime.strptime(st,"%I%p")
                except:
                    try:  #with only Hour,space,am/pm:  "7 am"
                        st24= datetime.datetime.strptime(st,"%I %p")
                    except:
                        try:  #with only Hour only  "7"
                            st24= datetime.datetime.strptime(st,"%I")
                        except: #unknown time format
                            print ("ERROR:Unknown time format:",st)
                            return "00:01:00"
    #print (st24.strftime("%H:%M:%S"))
    x = st24.strftime("%H:%M:%S")
    return x
    
def convertTime2(time):
    start = time[:time.find("&")]
    end = time[time.rfind(";")+1:]
    
    os=start
    oe=end
    s2=to24hourFormat(start)
    end = to24hourFormat(end)
            
    if s2 > end:
        start = to24hourFormat(start+"pm")
        db = ("A"+start)
    elif s2[0:2]<"12" and "am" in oe:
        start = to24hourFormat(start+"pm")
        db = ("C"+start)
        if start > end:
            start = to24hourFormat(os)
    elif s2[0:2]<"12" and s2 < "09:31:00":
        start = to24hourFormat(start+"pm")
        db = ("B"+start)
        if start > end:
            start = to24hourFormat(os)
    else:
        start = to24hourFormat(start)
        db = ("D"+start)

    #print(start+"-"+end)
    return start+"-"+end
    
    # adjust for 12:30-1:00pm style formats
    #assumes nothing starts before 5AM !!!
    s2=to24hourFormat(start)
    if s2 < "05:00:00": #REALLY early start times are probably wrong
        start = to24hourFormat(start+"pm")  #assume it means afternoon
    else:
        start = to24hourFormat(start)

    end = to24hourFormat(end)
    print ("T"+start+"-"+end)
    return start+"-"+end
    
def convertDate2(date):
    months = {"January":"01","February":"02","March":"03","April":"04","May":"05","June":"06","July":"07","August":"08","September":"09","October":"10","November":"11","December":"12"}
    month = date[:date.find(" ")]
    month = months[month]
    day = date[date.find(" ")+1:date.find(",")]
    year = date[date.find(",")+2:]
    return year+"-"+month+"-"+day

def getSyncDin():
    listDict = {}
    eventDict = {}
    site = Scraper.getSite(syncDin)
    feed = feedparser.parse(site.content)
    for entry in feed.entries:
        eventDict = {}
        cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        title = entry.title
        
        ##Attempt to sanitize data - NEEDS IMPROVEMENTS
        title = title.replace("'","")
        title = title.replace("¡","")
        title = title.replace("’","")
        title = title.replace("ñ","n")
        title = title.replace("é","e")
        title = title.replace("–","-")
        
        title = re.sub(cleanr, "", title)
        eventDict["title"] = title
        desc = entry.summary
        startIndex = desc.find("<p>")
        endIndex = desc.find("</p>")
        desc = desc[startIndex+3:endIndex]
        desc = re.sub(cleanr, "", desc)
        desc = desc.replace("'","")
        eventDict["description"] = desc
        loc = entry.location
        loc = loc.replace("'","")
        eventDict["location"] = loc
        
        #Date-times are GMT which need to be converted: -6 or -5 hours
        val = gmtToEst(entry.start)
        eventDict["date"] = val.strftime("%Y-%m-%d")
        eventDict["start"] = val.strftime("%H:%M:%S")
        val = gmtToEst(entry.end)
        eventDict["end"] = val.strftime("%H:%M:%S")
    
        org = entry.host
        org = org.replace("'","")
        eventDict["organization"] = org
        eventDict["eventType"] = "syncDIN"
        listDict[entry.title] = eventDict
    #print(listDict)
    return listDict

def getCLPLinks():
    listDict = {}
    eventDict = {}
    site = Scraper.getSoup(clp)
    print(site.prettify())
    feed = feedparser.parse(site.prettify(formatter='html'))
    for entry in feed.entries:
        # print(entry.keys())
        eventDict = {}
        cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        title = entry.title
        
        ### attempt to sanitize  NEEDS IMPROVEMENT
        title = title.replace("'","")
        title = title.replace("¡","")
        title = title.replace("’","")
        title = title.replace("ñ","n")
        title = title.replace("é","e")
        title = title.replace("–","-")
        
        title = re.sub(cleanr, "", title)
        eventDict["title"] = title
        desc = entry.summary
        #print("Summary:",desc)
        
        if desc.find(',') <= 10: # No location given
            eventDict["location"] = ""
        else: # Location given
            eventDict["location"] = desc[:desc.find("<br/>")-1]
            desc = desc[desc.find(">")+1:]
            
        date = desc[desc.find(",")+2:]
        date = date[:date.find(" ",date.find(",")+2)-1]
        eventDict["date"] = convertDate2(date)
        desc = desc[desc.find(",")+1:]
        desc = desc[desc.find(",")+1:]
        desc = desc[desc.find(",")+2:]
    
        time = convertTime2(desc[:desc.find(" ")])
        eventDict["start"] = time[:time.find("-")]
        eventDict["end"] = time[time.find("-")+1:]
        desc = desc[desc.find("<p>")+3:]
        
        #print (eventDict["title"],time)
        
        description = desc[:desc.find("</p>")]
        cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
        description = re.sub(cleanr, "", description)
        description = description.replace("'","")
        eventDict["description"] = description 
        
        organ = desc[desc.find("Organization"):]
        eventDict["organization"] = organ[organ.find(";")+1:organ.find("<br/>")]
        eventDict["organization"] = eventDict["organization"].replace("&amp;","&")
        
        eventDict["eventType"] = "CLP"
        listDict[entry.title] = eventDict
    #print(listDict)
    return listDict
    
def main():
    syncDinDict = getSyncDin()
    clpDict = getCLPLinks()
    
    #code to add to DB
    filename = '/home/csdaemon/aux/userCred.txt'
    file = open(filename, 'r')
    credentials = file.readlines()
    username = credentials[0].strip()
    password = credentials[1].strip()

    connection = pymysql.connect(host='cs.furman.edu',
                user=username,
                password=password,
                db='FUNOW',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)
    
    try:
            with connection.cursor() as cursor:
                removeSQL = "DELETE FROM clps;"
                cursor.execute(removeSQL)
                id = 1
                for name,event in syncDinDict.items():
                    insert =  "INSERT INTO clps (id,title,description,location,date,start,end,organization,eventType) "
                    vals = "VALUES ('"+str(id)+"', '"+event["title"]+"', '"+event["description"]+"', '"+event["location"]+"', '"+event["date"]+"', '"+event["start"]+"', '"+event["end"]+"', '"+event["organization"]+"', '"+event["eventType"]+"');"
                    insertSQL = insert+vals
                    id += 1
                    cursor.execute(insertSQL)
                    print(f'&:{event["title"]} @ {event["start"]} on {event["date"]}')
                for name,event in clpDict.items():
                    insert =  "INSERT INTO clps (id,title,description,location,date,start,end,organization,eventType) "
                    vals = "VALUES ('"+str(id)+"', '"+event["title"]+"', '"+event["description"]+"', '"+event["location"]+"', '"+event["date"]+"', '"+event["start"]+"', '"+event["end"]+"', '"+event["organization"]+"', '"+event["eventType"]+"');"
                    insertSQL = insert+vals
                    id += 1
                    cursor.execute(insertSQL)
                    print(f'+:{event["title"]} @ {event["start"]} on {event["date"]}')
            connection.commit()
    finally:
            connection.close()
    

#if __name__ == "__main__":
#   main()
main()
