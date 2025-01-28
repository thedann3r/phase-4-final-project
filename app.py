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

class PlaneCompany(db.Model, SerializerMixin):
    __tablename__ = 'plane_company'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False, unique = True)
    founded = db.Column(db.String, nullable = False)
    planes = db.relationship('Planes', back_populates = 'plane_company')

class Planes(db.Model, SerializerMixin):
    __tablename__ = 'planes'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False, unique = True)
    planeCompany_id = db.Column(db.Integer, db.ForeignKey('plane_company.id'), nullable = False)

    plane_company = db.relationship('PlaneCompany', back_populates = 'planes')
    owners = db.relationship('Owners', back_populates = 'planes')

class Owners(db.Model, SerializerMixin):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False, unique = True)

    planes = db.relationship('Planes', back_populates = 'owners')

class PlanesOwners(db.Model, SerializerMixin):
    __tablename__ = 'planesowners'
    id = db.Column(db.Integer, primary_key = True)
    
    planes_id = db.Column(db.Integer, db.ForeignKey('planes.id'), nullable = False)
    owners_id = db.Column(db.Integer, db.ForeignKey('owners.id'), nullable = False)
    
    planes = db.relationship('Planes', back_populates = 'owners')
    owners = db.relationship('Owners', back_populates = 'planes')

@app.route('/')
def home():
    return '<h1>Welcome to the airplane web page!</h1>'

class PlaneCompanyResource(Resource):
    def get(self):
        companies = PlaneCompany.query.all()
        return [company.to_dict() for company in companies]
    
    def post(self):
        data = request.get_json()
        if not data or not all(key in data for key in ('name', 'founded')):
            return {'error' : 'missing required fields!'}, 422
        new_company = PlaneCompany(**data)
        db.session.add(new_company)
        db.session.commit()
        return new_company.to_dict(), 201

if __name__ == '__main__':
    app.run(debug=True)