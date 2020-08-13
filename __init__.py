from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('myBlog.config')

db = SQLAlchemy(app)

from myBlog.views import views,entries