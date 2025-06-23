"""
Flask routes to support a backend for Furman Now app.
Each route returns data necessary for hooks in the React-Native app.

"""

from flask import jsonify, Blueprint
from app import db
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import (
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
    Image,
    StopWithDistance
)

bp = Blueprint('api', __name__, url_prefix='/FUNow/api')
SESSION: Session = db.session

## TODO: Go through PHP files and see how they're set up. Also set up database for these routes.
## TODO: Implement API Key for security and to hide API 
## Link if needed to look back: https://cs.furman.edu/~csdaemon/FUNow/stopsGet.php

@bp.route("/athleticsGet", methods=["GET"])
def athleticsGet():
    results = SESSION.execute(select(Athletics)).scalars().all()
    return jsonify({'format':'athletics', 'results':[entry.to_dict() for entry in results]})

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
    results = SESSION.execute(select(NewsContent)).scalars().all()
    return jsonify({"format":"newsContent","results": [entry.to_dict() for entry in results]})

@bp.route("/newsPublishersGet", methods=["GET"])
def newsPublishersGet():
    results = SESSION.execute(select(NewsPublisher)).scalars().all()
    return jsonify({"format":"newsPublishers","results": [entry.to_dict() for entry in results]})

@bp.route("/shuttleGet", methods=["GET"]) # TODO: Check php, has a variable in it.
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
    return jsonify({"format":"weather","results": [entry.to_dict() for entry in results]})

@bp.route("/weatherGet", methods=["GET"])
def weatherGet():
    results = SESSION.execute(select(Weather)).scalars().all()
    return jsonify({"format":"weather","results": [entry.to_dict() for entry in results]})

# TODO: will need to change image links
# TODO: Use php to make SQL query
@bp.route("/weatherImagesCurrent", methods=["GET"]) 
def weatherImagesCurrent():
    results = SESSION.execute(select(Image)).scalars().all()
    return jsonify({"format":"images","results": [entry.to_dict() for entry in results]})
