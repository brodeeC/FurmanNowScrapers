"""
Defining database using SQLAlchemy to further abstract away SQL Queries.
"""
from app import db
from datetime import datetime


class BuildingLocation(db.Model):
    __tablename__ = 'buildingLocations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    buildingID = db.Column(db.Integer, unique=True, nullable=False)
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


class BuildingHours(db.Model):
    __tablename__ = 'buildingHours'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    buildingID = db.Column(db.Integer, db.ForeignKey('buildingLocations.id'), nullable=False)
    day = db.Column(db.Text, nullable=False)
    dayorder = db.Column(db.Integer, nullable=False)
    Start = db.Column(db.Time)
    End = db.Column(db.Time)
    lastUpdated = db.Column(db.DateTime, default=datetime.now)


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


class CLP(db.Model):
    __tablename__ = 'clp'

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


class Contact(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    buildingID = db.Column(db.Integer, nullable=False)
    room = db.Column(db.Text)
    name = db.Column(db.Text, nullable=False)
    number = db.Column(db.Text, nullable=False)
    lastUpdated = db.Column(db.DateTime, default=datetime.now)
    priorityLevel = db.Column(db.Integer)


class DHMenu(db.Model):
    __tablename__ = 'dhMenu'

    id = db.Column(db.Integer, primary_key=True)
    meal = db.Column(db.Text, nullable=False)
    station = db.Column(db.Text, nullable=False)
    itemName = db.Column(db.Text, nullable=False)


class HealthSafety(db.Model):
    __tablename__ = 'healthSafety'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    shortName = db.Column(db.Text)
    content = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)
    icon = db.Column(db.Text)
    priority = db.Column(db.Integer)


class ImportantDate(db.Model):
    __tablename__ = 'importantDate'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    date = db.Column(db.Text, nullable=False)
    startTime = db.Column(db.Time)
    endTime = db.Column(db.Time)
    category = db.Column(db.Text)
    description = db.Column(db.Text)
    term = db.Column(db.Text)
    lastUpdated = db.Column(db.DateTime, default=datetime.now)


class ImportantLink(db.Model):
    __tablename__ = 'importantLinks'

    id = db.Column(db.Integer, primary_key=True)
    priority = db.Column(db.Integer)
    name = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)


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


class NewsPublisher(db.Model):
    __tablename__ = 'newsPublishers'

    publisherID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text)
    studentRun = db.Column(db.Integer, nullable=False)


class Shuttle(db.Model):
    __tablename__ = 'shuttles'

    id = db.Column(db.Integer, primary_key=True)
    vehicle = db.Column(db.Text, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    speed = db.Column(db.Float)
    direction = db.Column(db.Text)
    nextStopDistance = db.Column(db.Float)
    updated = db.Column(db.DateTime, nullable=False)
    nextStopID = db.Column(db.Integer)


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


class ShuttleStop(db.Model):
    __tablename__ = 'shuttleStops'

    lineID = db.Column(db.Integer, primary_key=True)
    stopOrderID = db.Column(db.Integer, primary_key=True)
    distFromStart = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    stopName = db.Column(db.Text, nullable=False)
    distFromVehicle = db.Column(db.Float)
    updated = db.Column(db.Text, nullable=False)
    vehicleStopsUntil = db.Column(db.Text)


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


class Image(db.Model):
    __tablename__ = 'images'

    generated = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, primary_key=True)