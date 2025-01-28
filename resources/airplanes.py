from flask_restful import Resource
from flask import request
from models import PlaneCompany, Planes,PlanesOwners,Owners,db

class Company(Resource):
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
    
class CompanyList(Resource):
    def get(self, id):
        company = PlaneCompany.filter_by(id=id).first()

        if not company:
            return {'error' : 'Company was not found!'}, 404
        return company.to_dict(), 200
    
    # def patch(self, id):
    #     data = request.get_json()
    #     company = PlaneCompany.filter_by(id=id).first()
    #     if not company:
    #         return {'error' : 'Company not found!'}, 404
    #     if 'name' in data:
    #         company.name = data['name']
    #     if 'founded' in data:
    #         company.founded = data['founded']
    #     db.session.commt()
    #     return company.to_dict(), 200
    # def delete(self, id):
    #     company = PlaneCompany.query.get(id)
    #     if not company:
    #         return {'error' : 'Company not found!'}, 404
    #     db.session.delete(company)
    #     db.session.commit()
    #     return {'message' : 'company deleted successfully!'}, 200

class Airplanes(Resource):
    def get(self):
        planes = Planes.query.all()
        return [plane.to_dict() for plane in planes]