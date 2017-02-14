from uuid import uuid4
import boto3
import os.path
from .app import app, db
from werkzeug.utils import secure_filename
from .models import RawFile


def s3_upload(source_file, req, upload_dir=None):
    """ Uploads WTForm File Object to Amazon S3

        Expects following app.config attributes to be set:
            S3_KEY              :   S3 API Key
            S3_SECRET           :   S3 Secret Key
            S3_BUCKET           :   What bucket to upload to
            S3_UPLOAD_DIRECTORY :   Which S3 Directory.

        The default sets the access rights on the uploaded file to
        public-read.  It also generates a unique filename via
        the uuid4 function combined with the file extension from
        the source file.
    """

    if upload_dir is None:
        upload_dir = app.config["S3_UPLOAD_DIRECTORY"]

    source_filename = secure_filename(source_file.data.filename)
    source_extension = os.path.splitext(source_filename)[1]

    destination_filename = uuid4().hex + source_extension

    # Connect to S3 and upload file.
    s3 = boto3.resource('s3', aws_access_key_id=app.config["S3_KEY"],
                        aws_secret_access_key=app.config["S3_SECRET"])
    s3.Object(app.config["S3_BUCKET"], "uploads/" +
              destination_filename).put(Body=source_file.data.read())
    print(req["email"])
    newfile = RawFile(file_name=destination_filename, email=req.get('email'),
                      text=req.get('text'), date=req.get('datetime'),
                      user_id=req.get('user'),)

    db.session.add(newfile)
    db.session.commit()

    return destination_filename
