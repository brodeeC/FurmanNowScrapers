from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from pathlib import Path

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    BASE_DIR = Path(__file__).resolve().parent.parent
    DATABASE_PATH = BASE_DIR / 'database' / 'FUNow.db'

    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI=f'sqlite:///{DATABASE_PATH}',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    db.init_app(app)

    # Enable full CORS for development
    CORS(app, resources={r"/FUNow/api/*": {"origins": "*"}})

    from backend.app import routes
    app.register_blueprint(routes.bp)

    return app
