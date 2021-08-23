import secrets
import os

class Base:
    FLASK_APP = os.environ.get('FLASK_APP')
    SQLACHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = secrets.token_hex(16)

class Development(Base):
    FLASK_ENV = os.environ.get("FLASK_ENV")
    DATABASE = os.environ.get("DATABASE")
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

class Staging(Base):
    DATABASE = ""
    POSTGRES_USER = ""
    POSTGRES_PASSWORD = ""
    SQLALCHEMY_DATABASE_URI = ""

class Production(Base):
    DATABASE = "d28660h2fk15fb"
    POSTGRES_USER = "ipktrlbhmvmouo"
    POSTGRES_PASSWORD = "6b3e06372c7bd922870a305b2927632a4b25e482ecd9a949d275011209be2830"
    SQLALCHEMY_DATABASE_URI= "postgresql://ipktrlbhmvmouo:6b3e06372c7bd922870a305b2927632a4b25e482ecd9a949d275011209be2830@ec2-54-236-137-173.compute-1.amazonaws.com:5432/d28660h2fk15fb"
