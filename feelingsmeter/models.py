from .app import db


class RawFile(db.Model):

    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    date = db.Column(db.String)
    user_id = db.Column(db.String)

    def __init__(self, file_name=None, email=None, text=None,
                 date=None, user_id=None):
        self.file_name = file_name
        self.email = email
        self.text = text
        self.date = date
        self.user_id = user_id
        # self.boh = boh

    def __repr__(self):
        return '<File "{file_name}">'.format(file_name=self.file_name)
