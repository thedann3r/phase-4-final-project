from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class PlaneCompany(db.Model, SerializerMixin):
    __tablename__ = 'plane_company'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    founded = db.Column(db.String, nullable=False)
    planes = db.relationship('Planes', back_populates='plane_company')

class Planes(db.Model, SerializerMixin):
    __tablename__ = 'planes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    planeCompany_id = db.Column(db.Integer, db.ForeignKey('plane_company.id'), nullable=False)

    plane_company = db.relationship('PlaneCompany', back_populates='planes')
    owners = db.relationship('Owners', secondary='planes_owners', back_populates='planes')

class Owners(db.Model, SerializerMixin):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    planes = db.relationship('Planes', secondary='planes_owners', back_populates='owners')

class PlanesOwners(db.Model, SerializerMixin):
    __tablename__ = 'planes_owners'
    id = db.Column(db.Integer, primary_key=True)
    
    planes_id = db.Column(db.Integer, db.ForeignKey('planes.id'), nullable=False)
    owners_id = db.Column(db.Integer, db.ForeignKey('owners.id'), nullable=False)
    
    plane = db.relationship('Planes')
    owner = db.relationship('Owners')
