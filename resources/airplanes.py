from flask_restful import Resource
from flask import request
from models import PlaneCompany, Planes,PlanesOwners,Owners,db

class Company(Resource):
    def get(self):
        companies = PlaneCompany.query.all()
        return [company.to_dict() for company in companies]
    
    # def post(self):
    #     data = request.get_json()
    #     if not data or not all(key in data for key in ('name', 'founded')):
    #         return {'error' : 'You are missing required fields!'}, 422
    #     new_company = PlaneCompany(**data)
    #     db.session.add(new_company)
    #     db.session.commit()
    #     return new_company.to_dict(), 201
    
class CompanyList(Resource):
    def get(self, id):
        company = PlaneCompany.query.filter_by(id=id).first()

        if not company:
            return {'error' : 'The company could not be found!'}, 404
        return company.to_dict(), 200

class Airplane(Resource):
    def get(self):
        planes = Planes.query.all()
        return [plane.to_dict() for plane in planes]
    
    def post(self):
        data = request.get_json()
        if not data or not all(key in data for key in ('name', 'planeCompany_id')):
            return {'error' : 'You are missing required fields!'}, 422
        new_plane = Planes(
            name = data['name'],
            planeCompany_id = data['planeCompany_id']
        )
        db.session.add(new_plane)
        db.session.commit()
        return new_plane.to_dict(), 201
    
class AirplaneList(Resource):
    def get(self, id):
        plane = Planes.query.filter_by(id=id).first()

        if not plane:
            return {'error' : 'The airplane could not be found!'}, 404
        return plane.to_dict(), 200
    
    def patch(self, id):
        data = request.get_json()
        plane = Planes.query.filter_by(id=id).first()
        if not plane:
            return {'error' : 'The airplane could not be found!'}, 404
        if 'name' in data:
            plane.name = data['name']
        if 'planeCompany_id' in data:
            plane.planeCompany_id = data['planeCompany_id']
        db.session.commit()
        return plane.to_dict(), 200
    
    def delete(self, id):
        plane = Planes.query.get(id)
        if not plane:
            return {'error' : 'The airplane could not be found!'}, 404
        db.session.delete(plane)
        db.session.commit()
        return {'message' : 'Airplane deleted successfully!'}, 200
    
class TheOwner(Resource):
    def get(self):
        owners = Owners.query.all()
        return [owner.to_dict() for owner in owners]
    
    def post(self):
        data = request.get_json()
        if not data or 'name' not in data:
            return {'error': 'You are missing the required field: name!'}, 422
        new_owner = Owners(
            name = data['name']
        )
        db.session.add(new_owner)
        db.session.commit()
        return new_owner.to_dict(), 201
    
class TheOwnerList(Resource):
    def get(self, id):
        owner = Owners.query.filter_by(id=id).first()

        if not owner:
            return {'error' : 'The airplane could not be found!'}, 404
        return owner.to_dict(), 200
    
class PlaneOwner(Resource):
    def get(self):
        planeOwners = PlanesOwners.query.all()
        return [planeOwner.to_dict() for planeOwner in planeOwners]
    
    def post(self):
        data = request.get_json()
        if not data or not all(key in data for key in ('planes_id', 'owners_id')):
            return {'error' : 'You are missing required fields!'}, 422
        new_owner = PlanesOwners(
            planes_id = data['planes_id'],
            owners_id = data['owners_id']
        )
        db.session.add(new_owner)
        db.session.commit()
        return new_owner.to_dict(), 201
    
class PlaneOwnerList(Resource):
    def get(self,id):
        planeOwner = PlanesOwners.query.filter_by(id=id).first()

        if not planeOwner:
            return {'error' : 'The airplane and its owners could not be found!'}, 404
        return planeOwner.to_dict(), 200