# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:14:53 2024

@author: mdavi
"""

import feedparser
from Utilities.WebConnectors import Scraper, formConnections, youTubePullLatest
from Utilities.SQLQueryClasses import Insertable
from dateutil.parser import parse as parseTime
from datetime import datetime, timedelta
from bs4 import BeautifulSoup as soup
from abc import abstractmethod
import json
from dataclasses import dataclass
from typing import ClassVar
from pdf2image import convert_from_path
import os

@dataclass
class Article(Insertable):
    
    title: str
    author: str
    description: str
    mediatype: str
    link: str
    publisherID: int
    section: str
    publishDate: datetime
    imagelink: str = None
    
    LINK : ClassVar[str] = "link"
    VIDEO : ClassVar[str] = "video"
    
    def insertInto(self, table, connection, commit = True):
        attrs = [["title", self.title],
                 ["author", self.author],
                 ["description", self.description],
                 ["media", self.mediatype],
                 ["linktocontent", self.link],
                 ["publisherID", self.publisherID],
                 ["section", self.section],
                 ["publishdate", self.publishDate.strftime("%Y-%m-%d %H:%M:%S")],
                 ["imagelink", self.imagelink]]
        Article._insertIntoHelper(table, connection, attrs, commit)
        
    def __lt__(self, other): 
        return self.publishDate < other.publishDate

PALADIN_FEED = "https://thepaladin.news/feed/"
CHRISTO_FEED = "https://christoetdoctrinae.com/articles?format=rss"
PRESIDENT_FEED = "https://www.furman.edu/about/president/communications/feed"
FURMAN_NEWS_FEED = "https://www.furman.edu/news/feed"
TOCQUEVILLE_BLOG_FEED = "https://www.furman.edu/academics/tocqueville-program/lectures/feed"
RILEY_BLOG_FEED = "https://www.furman.edu/riley/posts/feed"
RILEY_NEWS_FEED = "https://www.furman.edu/riley/news/feed"
ECHO_FEED = "https://scholarexchange.furman.edu/echo/all.rss"

FUNC_YOUTUBE_CHANNEL_ID = "UC3UaWOCIldF5_qWnCYEt0RQ"
KNIGHTLY_YOUTUBE_CHANNEL_ID = "UCiKdNbjss18h2LI1eesPRbA"
TOCQUEVILLE_YOUTUBE_CHANNEL_ID = "UCGwVaOolYr8YhU8xP0reIQw"
RILEY_YOUTUBE_CHANNEL_ID = "UCg_pCJrojA3kwdYGRl_OPEw"

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
    "Tocqueville" : {"id": 10, "name": "The Tocqueville Center"},# Online
    "Riley" :       {"id": 11, "name": "The Riley Institute"},  ## Online
    "Hill" :        {"id": 12, "name": "The Hill Institute"},       ## TO-DO
    "Shi" :         {"id": 13, "name": "The Shi Center"},           ## TO-DO
    }


class NewsScraper(Scraper):
    @abstractmethod
    def getTableID(self) -> int:
        raise NotImplementedError("Must override 'getTableID'.")
    
    def youTubeFilterForVideos(req):
        entries = json.loads(req.content)["items"]
        return filter(lambda entry: "upload" in entry["contentDetails"], entries)

    def parseYouTubeToArticle(entry, authName, tableID):
        return Article(
            title = entry["snippet"]["title"],
            author = authName,
            description = entry["snippet"]["description"],
            mediatype = Article.VIDEO,
            link = "https://youtu.be/" + entry["contentDetails"]["upload"]["videoId"],
            publisherID = tableID,
            section = None,
            publishDate = parseTime(entry["snippet"]["publishedAt"]),
            imagelink = None
        )
    
    def getPDFintoPNG(source, fileName):
        pdfTempFile = f"/home/csdaemon/pdf_of_{fileName}.pdf"
        with open(pdfTempFile, 'wb') as pdf:
            resp = Scraper.getSite(source)
            pdf.write(resp.content)
        page = f"FUNow/articleImages/{fileName}"
        convert_from_path(pdfTempFile, 
                          output_folder="/home/csdaemon/www/FUNow/articleImages/", 
                          output_file=fileName, 
                          single_file=True, 
                          dpi=300, 
                          fmt='png')
        os.remove(pdfTempFile)
        imagelink = f"https://cs.furman.edu/~csdaemon/{page}.png"
        return imagelink

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
                    section = None,
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
            
    def getImage(articleLink):
        page_soup = PaladinScraper.getSoup(articleLink)
        div = page_soup.find("div",attrs={"class": "sno-story-photo-image-area"})
        return div.find("img")["src"]
        
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
                    imagelink =  PaladinScraper.getImage(entry.link)
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
        summary = summarySoup.findAll("p")[0].contents[0]
        return summary
    
    def getLink(entry):
        # We can either use the Furman News link or the link that they are 
        # sending people to. If the latter exists, and the story is shorter than
        # two paragraphs (the feed always has a third, disclaimer at the bottom),
        # we prioritize it.
        pageLink = entry.link
        contentSoup = soup(entry.content[0]["value"], features="html.parser")
        try:
            lines = contentSoup.find_all("p")            
            links = []
            
            for n in lines:
                for potLnk in n.find_all("a"):
                    if "href" in potLnk.attrs and "furman.edu" not in potLnk["href"]:
                        links.append(potLnk["href"])
                        
            if len(lines) <= 3 and len(links) == 1:
                return links[0]
            else:
                return pageLink
            
        except Exception as e:
            print(e)
            return pageLink
                        
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
                    link = FurmanNewsScraper.getLink(entry),
                    publisherID = self.getTableID(),
                    section = None,
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
        req = youTubePullLatest(FUNC_YOUTUBE_CHANNEL_ID)
        feed = FUNCScraper.youTubeFilterForVideos(req)
        
        for entry in feed:
            articles.append(
                FUNCScraper.parseYouTubeToArticle(
                    entry, "FUNC Team", self.getTableID()
                    )
                )
        return articles
            
class KnightlyNewsScraper(NewsScraper):
    
    def getTableID(self):
        return NewsSources["Knightly"]["id"]
    
    def cleanDescription(desc):
        trunDesc = desc.split("\n\n")
        stories = trunDesc[0].split("\n")
        for i, v in enumerate(stories):
            if len(v) > 0 and i < len(stories) - 1 and v[-1] not in ".;,!?:":
                stories[i] = v.strip() + ";"
        return " ".join(stories)
        
    def _pull(self):
        articles = []
        req = youTubePullLatest(KNIGHTLY_YOUTUBE_CHANNEL_ID, 20)
        feed = KnightlyNewsScraper.youTubeFilterForVideos(req)
        
        for entry in feed:
            curArt = KnightlyNewsScraper.parseYouTubeToArticle(
                entry, "Knightly News Team", self.getTableID()
            )
            curArt.description = KnightlyNewsScraper.cleanDescription(curArt.description)
            articles.append(curArt)
        return articles

class TocquevilleScraper(NewsScraper):
    def getTableID(self):
        return NewsSources["Tocqueville"]["id"]
    
    def getSummary(blogEntry):
        summarySoup = soup(blogEntry.summary, features="html.parser")
        summary = summarySoup.findAll("p")[0].contents[0]
        return summary
    
    def getImage(blogEntry):
        for link in blogEntry.links:
            if "image" in link.type:
                return link.url

    def _pullYoutube(self):
        articles = []
        req = youTubePullLatest(TOCQUEVILLE_YOUTUBE_CHANNEL_ID)
        feed = TocquevilleScraper.youTubeFilterForVideos(req)

        for entry in feed:
            articles.append(
                TocquevilleScraper.parseYouTubeToArticle(
                    entry, "Tocqueville Center Staff", self.getTableID()
                    )
                )
        
        return articles
            
    def _pullBlog(self):
        articles = []
        site = Scraper.getSite(TOCQUEVILLE_BLOG_FEED)
        feed = feedparser.parse(site.content)

        for entry in feed.entries:
            articles.append(
                Article(
                    title = entry.title,
                    author = entry.author,
                    description = TocquevilleScraper.getSummary(entry),
                    mediatype = Article.LINK,
                    link = entry.link,
                    publisherID = self.getTableID(),
                    section = None,
                    publishDate = parseTime(entry.published),
                    imagelink =  TocquevilleScraper.getImage(entry)
                )
            )
        return articles

    def _pull(self):
        articles = []
        try:
            articles += self._pullYoutube()
        except Exception as e:
            print(e)
        
        try:
            articles += self._pullBlog()
        except Exception as e:
            print(e)
            
        articles.sort(reverse=True)
        return articles[:10]

class RileyScraper(NewsScraper): 
    def getTableID(self) -> int:
        return NewsSources["Riley"]["id"]
    
    def getSummary(blogEntry):
        summarySoup = soup(blogEntry.summary, features="html.parser")
        summary = summarySoup.findAll("p")[0].contents[0]
        return summary
    
    def getImage(entry):
        for link in entry.links:
            if "image" in link.type:
                return link.url
    
    def _pullYoutube(self):
        articles = []
        req = youTubePullLatest(RILEY_YOUTUBE_CHANNEL_ID)
        feed = RileyScraper.youTubeFilterForVideos(req)

        for entry in feed:
            articles.append(
                RileyScraper.parseYouTubeToArticle(
                    entry, "Riley Institue Staff", self.getTableID()
                    )
                )
        
        return articles
    
    def _pullBlog(self):
        articles = []
        site = Scraper.getSite(RILEY_BLOG_FEED)
        feed = feedparser.parse(site.content)

        for entry in feed.entries:
            articles.append(
                Article(
                    title = entry.title,
                    author = entry.author,
                    description = RileyScraper.getSummary(entry),
                    mediatype = Article.LINK,
                    link = entry.link,
                    publisherID = self.getTableID(),
                    section = None,
                    publishDate = parseTime(entry.published),
                    imagelink =  RileyScraper.getImage(entry)
                )
            )
        return articles
    
    def _pullNews(self):
        articles = []
        site = Scraper.getSite(RILEY_NEWS_FEED)
        feed = feedparser.parse(site.content)

        for entry in feed.entries:
            articles.append(
                Article(
                    title = entry.title,
                    author = entry.author,
                    description = RileyScraper.getSummary(entry),
                    mediatype = Article.LINK,
                    link = entry.link,
                    publisherID = self.getTableID(),
                    section = None,
                    publishDate = parseTime(entry.published),
                    imagelink =  RileyScraper.getImage(entry)
                )
            )
        return articles
    
    def _pull(self):
        articles = []
        try:
            articles += self._pullYoutube()
        except Exception as e:
            print(e)
        
        try:
            articles += self._pullBlog()
        except Exception as e:
            print(e)
            
        articles.sort(reverse=True)
        return articles[:10]
       
class EchoScraper(NewsScraper):
    
    def __init__(self, grabCover=False):
        self.grabCover = grabCover
        
    def getTableID(self): 
        return NewsSources["Echo"]["id"]
    
    def cleanParseTime(date):
        date = date.lower()
        if "est" in date:
            date = date[:-3] + "UTC-0500"
        if "edt" in date:
            date = date[:-3] + "UTC-0400"
        if "pst" in date:
            date = date[:-3] + "UTC-0800"
        if "pdt" in date:
            date = date[:-3] + "UTC-0700"
        return parseTime(date)
    
    def _pull(self):
        articles = []
        site = Scraper.getSite(ECHO_FEED)
        feed = feedparser.parse(site.content)
        date = EchoScraper.cleanParseTime(feed['feed']['updated'])
        
        if True:#datetime.now().astimezone() - date > timedelta(hours=4):
            firstArticleTime = EchoScraper.cleanParseTime(feed.entries[0]["published"])
            for article in filter(lambda a: firstArticleTime - EchoScraper.cleanParseTime(a["published"]) < timedelta(days=30),feed.entries):
                page = Scraper.getSoup(article["link"])
                section = page.find("div", {"id": "document_type"}).find("p").text
                articles.append(
                        Article(
                            title = article["title"],
                            author = article["author"] if "author" in article else "The Echo",
                            description = article["summary"],
                            mediatype = Article.LINK,
                            link = article["link"],
                            publisherID = self.getTableID(),
                            section = section,
                            publishDate = EchoScraper.cleanParseTime(article["published"])
                            )
                    )
                
                if self.grabCover and article["title"] == "Cover":
                    pdf_link = page.find("a", {"id":"pdf"})["href"]
                    imageLink = NewsScraper.getPDFintoPNG(pdf_link, f"echo-cover-{article['published_parsed'].tm_year}-{article['published_parsed'].tm_mon}-{article['published_parsed'].tm_mday}")
                    articles[-1].imagelink = imageLink
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
    newsScrapers = [ChristoScraper(), PaladinScraper(), FUNCScraper(), FurmanNewsScraper(),
                    KnightlyNewsScraper(), PresidentScraper(), RileyScraper(), TocquevilleScraper(),
                    EchoScraper(True)]
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

