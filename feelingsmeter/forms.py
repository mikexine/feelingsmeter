from flask_wtf import FlaskForm
from wtforms import FileField, StringField
from wtforms.validators import DataRequired, Email, Length


class UploadForm(FlaskForm):
    email = StringField('Email', [DataRequired(), Email(),
                                  Length(min=6, max=40)])
    text = StringField('Text Column', [DataRequired()])
    datetime = StringField('Datetime Column', [DataRequired()])
    user = StringField('User Column', [DataRequired()])
    file = FileField('Example File', [DataRequired()])
