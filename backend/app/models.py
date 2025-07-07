"""
Defining database using SQLAlchemy to further abstract away SQL Queries.
"""
from app import db
from datetime import datetime


class BuildingLocation(db.Model):
    __tablename__ = 'buildingLocations'

    buildingID = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    nickname = db.Column(db.Text)
    category = db.Column(db.Text)
    hasHours = db.Column(db.Integer, default=0)
    website = db.Column(db.Text)
    location = db.Column(db.Text)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    polyline = db.Column(db.Text)
    description = db.Column(db.Text)
    frequency = db.Column(db.Integer, default=0)
    last_updated = db.Column(db.DateTime, default=datetime.now)

    hours = db.relationship("BuildingHours", backref="location", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "buildingID": self.buildingID,
            "name": self.name,
            "nickname": self.nickname,
            "category": self.category,
            "hasHours": self.hasHours,
            "website": self.website,
            "location": self.location,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "polyline": self.polyline,
            "description": self.description,
            "frequency": self.frequency,
            "last_updated": self.last_updated.isoformat() if self.last_updated else None,
        }


class BuildingHours(db.Model):
    __tablename__ = 'buildingHours'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    buildingID = db.Column(db.Integer, db.ForeignKey('buildingLocations.buildingID'), nullable=False)
    day = db.Column(db.Text, nullable=False)
    dayorder = db.Column(db.Integer, nullable=False)
    Start = db.Column(db.Time)
    End = db.Column(db.Time)
    lastUpdated = db.Column(db.DateTime, default=datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "buildingID": self.buildingID,
            "day": self.day,
            "dayorder": self.dayorder,
            "Start": self.Start.isoformat() if self.Start else None,
            "End": self.End.isoformat() if self.End else None,
            "lastUpdated": self.lastUpdated.isoformat() if self.lastUpdated else None,
        }


class Athletics(db.Model):
    __tablename__ = 'athletics'

    id = db.Column(db.Integer, primary_key=True)
    eventdate = db.Column(db.Text, nullable=False)
    time = db.Column(db.Text)
    conference = db.Column(db.Text)
    location_indicator = db.Column(db.Text)
    location = db.Column(db.Text)
    sportTitle = db.Column(db.Text)
    sportShort = db.Column(db.Text)
    opponent = db.Column(db.Text)
    noplayText = db.Column(db.Text)
    resultStatus = db.Column(db.Text)
    resultUs = db.Column(db.Text)
    resultThem = db.Column(db.Text)
    prescore_info = db.Column(db.Text)
    postscore_info = db.Column(db.Text)
    url = db.Column(db.Text)
    lastUpdated = db.Column(db.DateTime, default=datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "eventdate": self.eventdate,
            "time": self.time,
            "conference": self.conference,
            "location_indicator": self.location_indicator,
            "location": self.location,
            "sportTitle": self.sportTitle,
            "sportShort": self.sportShort,
            "opponent": self.opponent,
            "noplayText": self.noplayText,
            "resultStatus": self.resultStatus,
            "resultUs": self.resultUs,
            "resultThem": self.resultThem,
            "prescore_info": self.prescore_info,
            "postscore_info": self.postscore_info,
            "url": self.url,
            "lastUpdated": self.lastUpdated.isoformat() if self.lastUpdated else None,
        }


class CLP(db.Model):
    __tablename__ = 'clps'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.Text)
    date = db.Column(db.Text, nullable=False)
    start = db.Column(db.Time)
    end = db.Column(db.Time)
    organization = db.Column(db.Text)
    eventType = db.Column(db.Text)
    lastUpdated = db.Column(db.DateTime, default=datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "location": self.location,
            "date": self.date,
            "start": self.start.isoformat() if self.start else None,
            "end": self.end.isoformat() if self.end else None,
            "organization": self.organization,
            "eventType": self.eventType,
            "lastUpdated": self.lastUpdated.isoformat() if self.lastUpdated else None
        }


class Contact(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    buildingID = db.Column(db.Integer, nullable=False)
    room = db.Column(db.Text)
    name = db.Column(db.Text, nullable=False)
    number = db.Column(db.Text, nullable=False)
    lastUpdated = db.Column(db.DateTime, default=datetime.now)
    priorityLevel = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "buildingID": self.buildingID,
            "room": self.room,
            "name": self.name,
            "number": self.number,
            "lastUpdated": self.lastUpdated.isoformat() if self.lastUpdated else None,
            "priorityLevel": self.priorityLevel
        }


class DHMenu(db.Model):
    __tablename__ = 'dhMenu'

    id = db.Column(db.Integer, primary_key=True)
    meal = db.Column(db.Text, nullable=False)
    station = db.Column(db.Text, nullable=False)
    itemName = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "meal": self.meal,
            "station": self.station,
            "itemName": self.itemName
        }


class HealthSafety(db.Model):
    __tablename__ = 'healthSafety'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    shortName = db.Column(db.Text)
    content = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)
    icon = db.Column(db.Text)
    priority = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "shortName": self.shortName,
            "content": self.content,
            "type": self.type,
            "icon": self.icon,
            "priority": self.priority
        }


class ImportantDate(db.Model):
    __tablename__ = 'importantDates'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    date = db.Column(db.Text, nullable=False)
    startTime = db.Column(db.Time)
    endTime = db.Column(db.Time)
    category = db.Column(db.Text)
    description = db.Column(db.Text)
    term = db.Column(db.Text)
    lastUpdated = db.Column(db.DateTime, default=datetime.now)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "date": self.date,
            "startTime": self.startTime.isoformat() if self.startTime else None,
            "endTime": self.endTime.isoformat() if self.endTime else None,
            "category": self.category,
            "description": self.description,
            "term": self.term,
            "lastUpdated": self.lastUpdated.isoformat() if self.lastUpdated else None
        }


class ImportantLink(db.Model):
    __tablename__ = 'importantLinks'

    id = db.Column(db.Integer, primary_key=True)
    priority = db.Column(db.Integer)
    name = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "priority": self.priority,
            "name": self.name,
            "content": self.content,
            "type": self.type
        }


class NewsContent(db.Model):
    __tablename__ = 'newsContent'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    author = db.Column(db.Text)
    description = db.Column(db.Text)
    media = db.Column(db.Text)
    linktocontent = db.Column(db.Text, nullable=False)
    publisherID = db.Column(db.Integer)
    section = db.Column(db.Text)
    publishdate = db.Column(db.DateTime)
    imagelink = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "description": self.description,
            "media": self.media,
            "linktocontent": self.linktocontent,
            "publisherID": self.publisherID,
            "section": self.section,
            "publishdate": self.publishdate.isoformat() if self.publishdate else None,
            "imagelink": self.imagelink
        }


class NewsPublisher(db.Model):
    __tablename__ = 'newsPublishers'

    publisherID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text)
    studentRun = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "publisherID": self.publisherID,
            "name": self.name,
            "link": self.link,
            "image": self.image,
            "studentRun": self.studentRun
        }


class Shuttle(db.Model):
    __tablename__ = 'shuttleLocations'

    id = db.Column(db.Integer, primary_key=True)
    vehicle = db.Column(db.Text, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    speed = db.Column(db.Float)
    direction = db.Column(db.Text)
    nextStopDistance = db.Column(db.Float)
    updated = db.Column(db.DateTime, nullable=False)
    nextStopID = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "vehicle": self.vehicle,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "speed": self.speed,
            "direction": self.direction,
            "nextStopDistance": self.nextStopDistance,
            "updated": self.updated.isoformat() if self.updated else None,
            "nextStopID": self.nextStopID
        }


class VehicleName(db.Model):
    __tablename__ = 'vehicleNames'

    vehicleIndex = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    shortName = db.Column(db.Text)
    serviceTimes = db.Column(db.Text)
    locations = db.Column(db.Text)
    colorRed = db.Column(db.Float)
    colorGreen = db.Column(db.Float)
    colorBlue = db.Column(db.Float)
    iconName = db.Column(db.Text)
    routePolyline = db.Column(db.Text)
    website = db.Column(db.Text)
    color = db.Column(db.Text)
    averageSpeed = db.Column(db.Integer)
    averageStopSeconds = db.Column(db.Integer)
    message = db.Column(db.Text)

    def to_dict(self):
        return {
            "vehicleIndex": self.vehicleIndex,
            "name": self.name,
            "shortName": self.shortName,
            "serviceTimes": self.serviceTimes,
            "locations": self.locations,
            "colorRed": self.colorRed,
            "colorGreen": self.colorGreen,
            "colorBlue": self.colorBlue,
            "iconName": self.iconName,
            "routePolyline": self.routePolyline,
            "website": self.website,
            "color": self.color,
            "averageSpeed": self.averageSpeed,
            "averageStopSeconds": self.averageStopSeconds,
            "message": self.message
        }


class StopsDistance(db.Model):
    __tablename__ = 'stopsDistanceTable'

    lineID = db.Column(db.Integer, primary_key=True, nullable=False)
    stopOrderID = db.Column(db.Integer, primary_key=True, nullable=False)
    distFromVehicle = db.Column(db.Float, default=None)
    updated = db.Column(db.Text, nullable=False, server_default=db.text('CURRENT_TIMESTAMP'))
    vehicleStopsUntil = db.Column(db.Integer, default=None)

    def to_dict(self):
        return {
            "lineID": self.lineID,
            "stopOrderID": self.stopOrderID,
            "distFromVehicle": self.distFromVehicle,
            "updated": self.updated,
            "vehicleStopsUntil": self.vehicleStopsUntil
        }


class Stop(db.Model):
    __tablename__ = 'stopsTable'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lineID = db.Column(db.Integer, nullable=False)
    stopOrderID = db.Column(db.Integer, nullable=False)
    stopName = db.Column(db.Text, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    distFromStart = db.Column(db.Float, nullable=False)
    updated = db.Column(db.Text, nullable=False, server_default=db.text('CURRENT_TIMESTAMP'))

    def to_dict(self):
        return {
            "id": self.id,
            "lineID": self.lineID,
            "stopOrderID": self.stopOrderID,
            "stopName": self.stopName,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "distFromStart": self.distFromStart,
            "updated": self.updated
        }


class Weather(db.Model):
    __tablename__ = 'weather'

    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Text, nullable=False)
    start = db.Column(db.Text, nullable=False)
    end = db.Column(db.Text, nullable=False)
    isDayTime = db.Column(db.Integer, nullable=False)
    tempCurrent = db.Column(db.Integer)
    tempHi = db.Column(db.Integer)
    tempLo = db.Column(db.Integer)
    unit = db.Column(db.Text)
    precipitationPercent = db.Column(db.Integer)
    windSpeed = db.Column(db.Text)
    windDirection = db.Column(db.Text)
    shortForecast = db.Column(db.Text)
    detailedForecast = db.Column(db.Text)
    alert = db.Column(db.Text)
    emoji = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "day": self.day,
            "start": self.start,
            "end": self.end,
            "isDayTime": self.isDayTime,
            "tempCurrent": self.tempCurrent,
            "tempHi": self.tempHi,
            "tempLo": self.tempLo,
            "unit": self.unit,
            "precipitationPercent": self.precipitationPercent,
            "windSpeed": self.windSpeed,
            "windDirection": self.windDirection,
            "shortForecast": self.shortForecast,
            "detailedForecast": self.detailedForecast,
            "alert": self.alert,
            "emoji": self.emoji
        }
    
class StopWithDistance(db.Model):
    __tablename__ = 'stop_with_distance'

    lineID = db.Column(db.Text, primary_key=True)
    stopOrderID = db.Column(db.Integer, primary_key=True)
    distFromStart = db.Column(db.Float)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    stopName = db.Column(db.Text)
    updated = db.Column(db.DateTime)
    distFromVehicle = db.Column(db.Float)
    vehicleStopsUntil = db.Column(db.Integer)

    def to_dict(self):
        return {
            "lineID": self.lineID,
            "stopOrderID": self.stopOrderID,
            "distFromVehicle": self.distFromVehicle,
            "updated": self.updated,
            "vehicleStopsUntil": self.vehicleStopsUntil,
            "distFromStart": self.distFromStart,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "stopName": self.stopName
        }
    
class parkingZones(db.Model):
    __tablename__ = 'parkingZones'

    id = db.Column(db.Integer, primary_key=True)
    zoneName = db.Column(db.Text)
    boundry = db.Column(db.Text)
    yellow = db.Column(db.Integer)
    green = db.Column(db.Integer)
    blue = db.Column(db.Integer)
    silver = db.Column(db.Integer)
    orange = db.Column(db.Integer)
    purple = db.Column(db.Integer)
    lightPurple = db.Column(db.Integer)
    public_col = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            'zoneName': self.zoneName,
            'boundry': self.boundry,
            'yellow': self.yellow == 1,
            'green': self.green == 1,
            'blue': self.blue == 1,
            'silver': self.silver == 1,
            'orange': self.orange == 1,
            'purple': self.purple == 1,
            'lightPurple': self.lightPurple == 1,
            'public_col': self.public_col == 1
        }
