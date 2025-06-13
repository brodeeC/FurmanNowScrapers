"""
Definining database using sqlAlchemy to further abstract away SQL Queries.
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
    lastUpdated = db.Column(db.DateTime, default=datetime.utcnow)
