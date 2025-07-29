from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from backend.app import routes
#from pathlib import Path   Needed for sqlite database
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    database_url = os.environ.get('DATABASE_URL')

    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)

    ## Defines path for a sqlite database
    # BASE_DIR = Path(__file__).resolve().parent.parent
    # DATABASE_PATH = BASE_DIR / 'database' / 'FUNow.db'

    # app.config.from_mapping(
    #     SQLALCHEMY_DATABASE_URI=f'sqlite:///{DATABASE_PATH}',
    #     SQLALCHEMY_TRACK_MODIFICATIONS=False
    # )

    db.init_app(app)

    # Enable full CORS for development
    CORS(app, resources={r"/FUNow/api/*": {"origins": "*"}})

    app.register_blueprint(routes.bp)

    return app
