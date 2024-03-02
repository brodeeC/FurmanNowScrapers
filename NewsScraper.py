# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:14:53 2024

@author: mdavi
"""

import feedparser
from TimeClasses import Article
from WebConnectors import Scraper, formConnections, youTubePullLatest
from dateutil.parser import parse as parseTime
from bs4 import BeautifulSoup as soup
from abc import abstractmethod
import json

PALADIN_FEED = "https://thepaladin.news/feed/"
CHRISTO_FEED = "https://christoetdoctrinae.com/articles?format=rss"
PRESIDENT_FEED = "https://www.furman.edu/about/president/communications/feed"
FURMAN_NEWS_FEED = "https://www.furman.edu/news/feed"

NEWS_TABLE = "newsContent"

NewsSources = {
    "Paladin" :     {"id": 1, "name": "The Paladin"},           ## Online
    "FUNC" :        {"id": 2, "name": "FUNC"},                  ## Online
    "Echo" :        {"id": 3, "name": "The Echo"},                  ## TO-DO
    "Knightly" :    {"id": 4, "name": "Knightly News"},         ## Online
    "Christo" :     {"id": 5, "name": "Christo et Doctrinae"},  ## Online
    "FHR" :         {"id": 6, "name": "Furman Humanities Review"},  ## TO-DO
    "News" :        {"id": 7, "name": "Furman in the News"},    ## Online
    "President" :   {"id": 8, "name": "President's Page"},      ## Online
    "Magazine" :    {"id": 9, "name": "Furman Magazine"},           ## TO-DO
}

class NewsScraper(Scraper):
    @abstractmethod
    def getTableID(self) -> int:
        raise NotImplementedError("Must override 'getTableID'.")

class ChristoScraper(Scraper):
    
    def getTableID(self):
        return NewsSources["Christo"]["id"]
    
    def getImage(entry):
        for link in entry.media_content:
            if "image" in link["type"]:
                return link["url"]
            
    def cleanDescription(description):
        noBreaks = description.split("\n")
        return " ".join(e.strip() for e in noBreaks)
        
    
    def _pull(self):
        articles = []
        site = ChristoScraper.getSite(CHRISTO_FEED)
        feed = feedparser.parse(site.content)
        
        for entry in feed.entries:
            articles.append(
                Article(
                    title = entry.title,
                    author = entry.author,
                    description = ChristoScraper.cleanDescription(entry.description),
                    mediatype = Article.LINK,
                    link = entry.link,
                    publisherID = self.getTableID(),
                    section = "",
                    publishDate = parseTime(entry.published),
                    imagelink = ChristoScraper.getImage(entry)
                    )
                )
        return articles
        
class PaladinScraper(NewsScraper):

    def getTableID(self):
        return NewsSources["Paladin"]["id"]
    
    def getSection(entry):
        for tag in entry["tags"]:
            if tag["term"] != "Showcase":
                return tag["term"]

    def _pull(self):
        articles = []
        site = PaladinScraper.getSite(PALADIN_FEED)
        feed = feedparser.parse(site.content)
        
        for entry in feed.entries:
            articles.append(
                Article(
                    title = entry.title,
                    author = entry.author,
                    description = entry.description,
                    mediatype = Article.LINK,
                    link = entry.link,
                    publisherID = self.getTableID(),
                    section = PaladinScraper.getSection(entry),
                    publishDate = parseTime(entry.published),
                    imagelink =  ""
                    )
                )
        return articles
    
class PresidentScraper(NewsScraper):
    
    def getTableID(self):
        return NewsSources["President"]["id"]

    def getImage(entry):
        for link in entry.links:
            if "image" in link.type:
                return link.href

    def _pull(self):
        articles = []
        site = Scraper.getSite(PRESIDENT_FEED)
        feed = feedparser.parse(site.content)
        
        for entry in feed.entries:
            articles.append(
                Article(
                    title = entry.title,
                    author = "Office of the President",
                    description = "",
                    mediatype = Article.LINK,
                    link = entry.link,
                    publisherID = self.getTableID(),
                    section = "",
                    publishDate = parseTime(entry.published),
                    imagelink =  PresidentScraper.getImage(entry)
                    )
                )
        return articles
    
class FurmanNewsScraper(NewsScraper):
    
    def getTableID(self):
        return NewsSources["News"]["id"]
            
    def getImage(entry):
        for link in entry.links:
            if "image" in link.type:
                return link.href
            
    def getSummary(entry):
        summarySoup = soup(entry.summary, features="html.parser")
        summary = summarySoup.findAll("p")[0].contents
        return summary
                        
    def _pull(self):
        articles = []
        site = Scraper.getSite(FURMAN_NEWS_FEED)
        feed = feedparser.parse(site.content)
        
        for entry in feed.entries:
            articles.append(
                Article(
                    title = entry.title,
                    author = entry.author,
                    description = FurmanNewsScraper.getSummary(entry),
                    mediatype = Article.LINK,
                    link = entry.link,
                    publisherID = self.getTableID(),
                    section = "",
                    publishDate = parseTime(entry.published),
                    imagelink =  FurmanNewsScraper.getImage(entry)
                    )
                )
        return articles
    

class FUNCScraper(NewsScraper):
    
    def getTableID(self):
        return NewsSources["FUNC"]["id"]
    
    def _pull(self):
        articles = []
        req = youTubePullLatest("UC3UaWOCIldF5_qWnCYEt0RQ")
        feed = json.loads(req.content)["items"]
        
        for entry in feed:
            if "upload" not in entry["contentDetails"]:
                continue
            articles.append(
                Article(
                    title = entry["snippet"]["title"].title(),
                    author = "FUNC Team",
                    description = entry["snippet"]["description"],
                    mediatype = Article.VIDEO,
                    link = "https://youtu.be/" + entry["contentDetails"]["upload"]["videoId"],
                    publisherID = self.getTableID(),
                    section = "",
                    publishDate = parseTime(entry["snippet"]["publishedAt"]),
                    imagelink = ""
                    )
                )
        return articles
            
class KnightlyNewsScraper(Scraper):
    
    def getTableID(self):
        return NewsSources["Knightly"]["id"]
    
    def getDescription(entry):
        desc = entry["snippet"]["description"]
        trunDesc = desc.split("\n\n")
        stories = trunDesc[0].split("\n");
        for i, v in enumerate(stories):
            if len(v) > 0 and i < len(stories) - 1 and v[-1] not in ".;,!?:":
                stories[i] = v.strip() + ";"
        return " ".join(stories)
        
    def _pull(self):
        articles = []
        req = youTubePullLatest("UCiKdNbjss18h2LI1eesPRbA", 20)
        feed = json.loads(req.content)["items"]
        
        for entry in feed:
            if "upload" not in entry["contentDetails"]:
                continue
            articles.append(
                Article(
                    title = entry["snippet"]["title"].title(),
                    author = "Knightly News Team",
                    description = KnightlyNewsScraper.getDescription(entry),
                    mediatype = Article.VIDEO,
                    link = "https://youtu.be/" + entry["contentDetails"]["upload"]["videoId"],
                    publisherID = self.getTableID(),
                    section = "",
                    publishDate = parseTime(entry["snippet"]["publishedAt"]),
                    imagelink = ""
                    )
                )
        return articles
    
def purgeOldEvents(connection, publisherID):
    sql = f"DELETE FROM `{NEWS_TABLE}` WHERE `publisherID` = {publisherID}"
    with connection.cursor() as cursor:
        try:
            cursor.execute(sql)
            connection.commit()     
        except:
            connection.rollback()
            print("Failed to purge.")
        
    
def main():
    newsScrapers = [PaladinScraper(), ChristoScraper(), PresidentScraper(),
                    FurmanNewsScraper(), KnightlyNewsScraper(), FUNCScraper()]
    articles = []
    for scraper in newsScrapers:
        articles += scraper.tryPull()
        
    connection = formConnections()
    for scraper in newsScrapers:
        if not scraper.didFail():
            purgeOldEvents(connection, scraper.getTableID())
    for artic in articles:
        artic.insertInto(NEWS_TABLE, connection)
    
if __name__ == "__main__":
    main()