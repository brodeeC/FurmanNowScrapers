import os

## Set up dotenv and Secret key if necessary
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///backend/database/FUNow.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # RATE_LIMITS = {    TODO: Limiter?
    #     'default': '300 per day, 100 per hour',
    #     'search': '10 per minute'
    # }