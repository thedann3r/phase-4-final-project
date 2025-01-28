from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy_serializer import SerializerMixin
from flask_cors import CORS
from flask_restful import Api, Resource

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airplanes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)
CORS(app, supports_credentials=True)
api = Api(app)

@app.route('/')
def home():
    return '<h1>Welcome to the airplane web page!</h1>'

class PlaneCompany(db.Model, SerializerMixin):
    __tablename__ = 'plane_company'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False, unique = True)
    founded = db.Column(db.String, nullable = False)

class Planes(db.Model, SerializerMixin):
    __tablename__ = 'planes'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False, unique = True)

class PlaneCompany(db.Model, SerializerMixin):
    __tablename__ = 'plane_company'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False, unique = True)
    founded = db.Column(db.String, nullable = False)

if __name__ == '__main__':
    app.run(debug=True)