from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '82a2d875563fc963b1544e822312444d'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config["SQLALCHEMY_DATABASE_URI"] ='jdbc:postgresql://localhost:5432/ImageTest'
app.config["SQLALCHEMY_DATABASE_URI"] ='postgresql://postgres:admin@localhost/ImageTest'
db = SQLAlchemy(app)

