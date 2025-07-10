"""
Flask routes to support a backend for Furman Now app.
Each route returns data necessary for hooks in the React-Native app.

"""

from flask import jsonify, Blueprint, render_template
from backend.app import db
from sqlalchemy.orm import Session
from sqlalchemy import select, desc
from datetime import datetime
import pytz
from backend.app.models import (
    BuildingHours,
    BuildingLocation,
    Athletics,
    CLP,
    Contact,
    DHMenu,
    HealthSafety,
    ImportantDate,
    ImportantLink,
    NewsContent,
    NewsPublisher,
    Shuttle,
    VehicleName,
    Stop,
    StopsDistance,
    Weather,
    StopWithDistance,
    parkingZones,
    userRatings
)

bp = Blueprint('api', __name__, url_prefix='/FUNow/api')
SESSION: Session = db.session

## TODO: Implement API Key for security and to hide API 
## Link if needed to look back: https://cs.furman.edu/~csdaemon/FUNow/stopsGet.php

@bp.route('/privacyPolicy', methods=["GET"])
def privacyPolicy():
    return render_template('privacyPolicy.html')

@bp.route("/athleticsGet", methods=["GET"])
def athleticsGet():
    results = SESSION.execute(select(Athletics)).scalars().all()
    return jsonify({'format':'athletics', 'results': [entry.to_dict() for entry in results] if results else None})

@bp.route("/hoursGet", methods=["GET"])
def hoursGet():
    results = SESSION.execute(select(BuildingHours)).scalars().all()
    return jsonify({"format":"hours","results":[entry.to_dict() for entry in results]})

@bp.route("/buildingGet", methods=["GET"])
def buildingGet():
    results = SESSION.execute(select(BuildingLocation)).scalars().all()
    return jsonify({"format":"buildings","results": [entry.to_dict() for entry in results]})

@bp.route("/clpGet", methods=["GET"])
def clpGet():
    results = SESSION.execute(select(CLP)).scalars().all()
    return jsonify({"format":"clp","results": [entry.to_dict() for entry in results]})

@bp.route("/contactsGet", methods=["GET"])
def contactsGet():
    results = SESSION.execute(select(Contact)).scalars().all()
    return jsonify({"format":"contacts","results": [entry.to_dict() for entry in results]})

@bp.route("/dhMenuGet", methods=["GET"])
def dhMenuGet():
    results = SESSION.execute(select(DHMenu)).scalars().all()
    return jsonify({"format":"dhMenu","results": [entry.to_dict() for entry in results]})

@bp.route("/healthSafetyGet", methods=["GET"])
def healthSafetyGet():
    results = SESSION.execute(select(HealthSafety)).scalars().all()
    return jsonify({"format":"healthSafety","results": [entry.to_dict() for entry in results]})

@bp.route("/importantDateGet", methods=["GET"])
def importantDateGet():
    results = SESSION.execute(select(ImportantDate)).scalars().all()
    return jsonify({"format":"importantDate","results": [entry.to_dict() for entry in results]})

@bp.route("/importantLinksGet", methods=["GET"])
def importantLinksGet():
    results = SESSION.execute(select(ImportantLink)).scalars().all()
    return jsonify({"format":"importantLinks","results": [entry.to_dict() for entry in results]})

@bp.route("/newsContentGet", methods=["GET"])
def newsContentGet():
    results = SESSION.execute(select(NewsContent).order_by(desc(NewsContent.publishdate))).scalars().all()
    return jsonify({"format":"newsContent","results": [entry.to_dict() for entry in results]})

@bp.route("/newsPublishersGet", methods=["GET"])
def newsPublishersGet():
    results = SESSION.execute(select(NewsPublisher)).scalars().all()
    return jsonify({"format":"newsPublishers","results": [entry.to_dict() for entry in results]})

@bp.route("/shuttleGet", methods=["GET"]) 
def shuttleGet():
    results = SESSION.execute(select(Shuttle)).scalars().all()
    return jsonify({"format":"shuttles","results": [entry.to_dict() for entry in results]})

@bp.route("/vehicleNamesGet", methods=["GET"])
def vehicleNamesGet():
    results = SESSION.execute(select(VehicleName)).scalars().all()
    return jsonify({"format":"VehicleNames","results": [entry.to_dict() for entry in results]})

@bp.route("/stopsGet", methods=["GET"])
def stopsGet():
    results = SESSION.execute(select(StopWithDistance)).scalars().all()
    return jsonify({"format":"stops","results": [entry.to_dict() for entry in results]})

@bp.route("/weatherGet", methods=["GET"])
def weatherGet():
    results = SESSION.execute(select(Weather)).scalars().all()
    return jsonify({"format":"weather","results": [entry.to_dict() for entry in results]})

@bp.route("/parkingZonesGet", methods=["GET"])
def parkingZonesGet():
    results = SESSION.execute(select(parkingZones)).scalars().all()
    return jsonify({"format":"zones", "results": [entry.to_dict() for entry in results]})

@bp.route("/userRatingsGet", methods=["GET"])
def userRatingsGet():
    results = SESSION.execute(select(userRatings)).scalars().all()
    return jsonify({"format":"ratings", "results":[entry.to_dict() for entry in results]})

# Sends up an image folder and name to build image link on the frontend
@bp.route("/weatherImagesCurrent", methods=["GET"]) 
def weatherImagesCurrent():
    IMAGE_MAP = {
        'rain': ['RainyFountain.jpg'],
        'snow': ['AdmissionsSnow.jpg', 'BellTowerCircleSnow.jpeg', 'ClarkMurphySnow.webp'],
        '01': ['BellTowerCircleSnow.jpeg', 'GatesInSnow.jpg'],
        '02': ['ClarkMurphySnow.webp'],
        '03': ['Ampatheater Aerial.jpg', 'DHInBloom.jpeg', 'FootballStadium.jpg'],
        '04': ['Dining Hall Entrence.jpg', 'SpringRoseGarden.jpg'],
        '05': ['Farm Aerial.jpg', 'RoseGarden.jpg'],
        '06': ['FurmanBloomsLibrary.jpg', 'FurmanSunset.jpg', 'PlaceOfPeace.jpg'],
        '07': ['FurmanBelltowerLowAngle.jpg', 'PlaceOfPeaceSummer.jpg'],
        '08': ['FurmanBelltowerLowAngle.jpg', 'FurmanMallAerial.jpg'],
        '09': ['BellTowerSeptember.jpg', 'Fall Heron At Lake.jpg', 'FurmanLibraryDay.jpg'],
        '10': ['BellTowerFall.jpg', 'GateHouse.jpg'],
        '11': ['FoggyFurman.webp', 'FurmanFallBellTower.jpg', 'FurmanLibraryReflective.jpg'],
        '12': ['AdmissionsSnow.jpg', 'FurmanMallSnow.jpg'],
    }
    now = datetime.now(pytz.timezone('America/New_York'))
    month = now.strftime('%m')

    weather = Weather.query.order_by(Weather.id).first()
    if not weather:
        return jsonify({"error": "No weather data"}), 500

    # Determine folder
    emoji = weather.emoji
    if emoji in ['0x1F326', '0x26C8', '0x1F327']:
        folder = 'rain'
    elif emoji == '0x1F328':
        folder = 'snow'
    else:
        folder = month  

    # Use the image map to build full URLs
    filenames = IMAGE_MAP.get(folder, [])
    links = [
        f"{folder}/{filename}"
        for filename in filenames
    ]
    
    return jsonify({
        "format": "images",
        "results": {
            "generated": now.strftime('%Y-%m-%d %H:%M:%S'),
            "links": links
        }
    })
