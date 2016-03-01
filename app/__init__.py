from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = "this is a super secure key"

# remember to change to heroku's databas
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://yzicurmnvkqqhp:Kpl-6hLvDaRcPCelsrxdmydSgi@ec2-23-21-219-209.compute-1.amazonaws.com:5432/de7vj5i2j9deb1"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/db"
db = SQLAlchemy(app)
db.create_all()
from app import views

