# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, static_url_path='/static')

app.config.from_object('feelingsmeter.config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
