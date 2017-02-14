import os

class Config(object):
    DEBUG = True

    S3_KEY = os.environ["S3_KEY"]
    S3_SECRET = os.environ["S3_SECRET"]
    S3_UPLOAD_DIRECTORY = os.environ["S3_UPLOAD_DIRECTORY"]
    S3_BUCKET = os.environ["S3_BUCKET"]

    SECRET_KEY = os.environ["SECRET_KEY"]
    DEBUG = os.environ["DEBUG"]
    PORT = os.environ["PORT"]

    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]

    # SQLALCHEMY_DATABASE_URI = "sqlite:///db.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
