from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models import db
from flask_cors import CORS
from resources.airplanes import CompanyList,Company,Airplanes,AirplaneList

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airplanes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
CORS(app, supports_credentials=True)
api = Api(app)

@app.route('/')
def home():
    return '<h1>Welcome to the airplane web page!</h1>'
    
api.add_resource(CompanyList, '/companies')
api.add_resource(Company, '/company/<int:id>')

api.add_resource(Airplanes, '/planes')
api.add_resource(AirplaneList, '/planes/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)