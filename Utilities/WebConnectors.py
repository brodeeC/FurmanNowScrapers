# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 23:57:41 2024

@author: mdavi
"""
import pymysql
from bs4 import BeautifulSoup as soup
import requests
from abc import ABC, abstractmethod
import traceback
import json
from typing import List


from Utilities.SQLiteCursorWrapper import SQLiteConnectionWrapper

class Scraper(ABC):
    
    failed : bool 
    found : bool
    
    def didFail(self):
        return self.failed
    
    def gotContent(self):
        return (not self.failed) and self.found
    
    def getSite(link):
        """ Given a link, instantiate the page_soup parser and return it """
        # open connection w/ main page, read html
        try:
            hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
            req = requests.get(link,headers=hdr, timeout=10)
            # instantiate html parser w/ html string, return
            return req
        except requests.exceptions.Timeout as e:
            raise FailedWebPullException(e)
        except ConnectionError as e:
            raise FailedWebPullException(e)        
    
    def getSoup(link):
        req = Scraper.getSite(link)
        page_soup = soup(req.content, features="html.parser")
        return page_soup
    
    @abstractmethod
    def _pull(self) -> List:
        raise NotImplementedError("Must override 'pull'.")
        
    def tryPull(self) -> List:
        pullResults = []
        self.failed = True
        try:
            pullResults = self._pull()
            self.failed = False
            self.found = len(pullResults) > 0 or (hasattr(self, 'found') and self.found)
        except NotImplementedError as e:
            print(e)
            print(f"_pull has not been implemented in {type(self)}; implement to scrape.")
        except FailedWebPullException as e:
            print(e)
            print(f"Failed in pulling with {type(self)}; website seems to have moved.")
            return []
        except Exception:
            traceback.print_exc()
            print(f"Failed in parsing page with {type(self)}; page may have been redesigned. Evaluate scraper.")
            return []
        return pullResults
    
    """
    Takes a dictionary parsed from JSon and an arbitrary number of keys and, if 
    an entry exists for that series, returns the value, otherwise returns None.
    Protected equivalent of dct[keys[0]][keys[1]]...[keys[n]]
    
    Attributes:
        dct : dict parsed from Json
        keys : str index keys for desired entry in dictionary
    """
    def maybeGetValue(dct, *keys, default=None): 
        if dct is None:
            return default
        for key in keys:
            if isinstance(dct, dict) and key in dct:
                dct = dct[key]
            else:
                return default
        return dct if dct is not None else default

def formConnections():
    # filename = '/home/csdaemon/aux/userCred.txt'
    # username = ''
    # password = ''
    # with open(filename, 'r') as file:
    #     credentials = file.readlines()
    #     username = credentials[0].strip()
    #     password = credentials[1].strip()
    
    # connection = pymysql.connect(host='cs.furman.edu', \
    #                              user=username, \
    #                              password=password, \
    #                              db='FUNOW', \
    #                              charset='utf8mb4', \
    #                              cursorclass=pymysql.cursors.DictCursor,
    #                              read_timeout = 2,
    #                              write_timeout = 2)

    return SQLiteConnectionWrapper("backend/database/FUNow.db") # Use local db to test scrapers and find bug.

def youTubePullLatest(channelID, numRequested = 10):
    filename = "/home/csdaemon/aux/youtubeAPICred.txt"
    with open(filename, "r") as file:
        apiKey = file.readlines()[0].strip()
        headers = {"Accept": "application/json", "Referer": "Mozilla"}
        req = requests.get("https://youtube.googleapis.com/youtube/v3/" +
                     "activities?part=contentDetails&part=id&part=snippet" + 
                     "&channelId=" + channelID + "&maxResults=" + str(numRequested) + "&key=" + 
                     apiKey,
                     headers=headers)
        return req

def getLibraryAPIToken():
    link = "https://libcal.furman.edu/1.1/oauth/token"
    filename = "backend/aux/libraryAPICred.txt" 
    file = open(filename, 'r')
    credentials = file.readlines()
    clientID = credentials[0].strip()
    clientSecret = credentials[1].strip()
    auth = {'client_id': clientID, 
            'client_secret' : clientSecret,
            'grant_type': 'client_credentials'}
    req = requests.post(link,data=auth, timeout=10)
    accessToken = json.loads(req.content)['access_token']
    
    return accessToken

class FailedConnectionException(Exception):
    pass

class FailedWebPullException(Exception):
    pass
