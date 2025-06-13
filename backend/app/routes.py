from flask import Flask, jsonify, requests, Blueprint
from app import db
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
    ShuttleStop,
    Weather,
    Image
)

bp = Blueprint('api', __name__, url_prefix='/FUNow/api')

## TODO: Go through PHP files and see how they're set up. Also set up database for these routes.
## TODO: Implement API Key for security and to hide API 

@bp.route("/athleticsGet", methods=["Get"])
def athleticsGet():
    print('Athletics')

@bp.route("/hoursGet", methods=["Get"])
def hoursGet():
    print('Hours')

@bp.route("/buildingGet", methods=["Get"])
def buildingGet():
    print('Buildings')

@bp.route("/clpGet", methods=["Get"])
def clpGet():
    print('CLPs')

@bp.route("/contactsGet", methods=["Get"])
def contactsGet():
    print('Contacts')

@bp.route("/dhMenuGet", methods=["Get"])
def dhMenuGet():
    print('DHMenu')

@bp.route("/healthSafetyGet", methods=["Get"])
def healthSafetyGet():
    print('healthSafety')

@bp.route("/importantDateGet", methods=["Get"])
def importantDateGet():
    print('importantDateGet')

@bp.route("/importantLinksGet", methods=["Get"])
def importantLinksGet():
    print('importantLinksGet')

@bp.route("/newsContentGet", methods=["Get"])
def newsContentGet():
    print('newsContentGet')

@bp.route("/newsPublishersGet", methods=["Get"])
def newsPublishersGet():
    print('newsPublishersGet')

@bp.route("/shuttleGet", methods=["Get"]) # TODO: Check php, has a variable in it.
def shuttleGet():
    print('shuttleGet')

@bp.route("/vehicleNamesGet", methods=["Get"])
def vehicleNamesGet():
    print('vehicleNamesGet')

@bp.route("/stopsGet", methods=["Get"])
def stopsGet():
    print('stopsGet')

@bp.route("/weatherGet", methods=["Get"])
def weatherGet():
    print('weatherGet')

@bp.route("/weatherImagesCurrent", methods=["Get"])
def weatherImagesCurrent():
    print('weatherImagesCurrent')