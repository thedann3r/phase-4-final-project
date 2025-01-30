from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models import db
from flask_cors import CORS
import os
from resources.airplanes import CompanyList,Company,Airplane,AirplaneList,TheOwner,TheOwnerList,PlaneOwner,PlaneOwnerList
from dotenv import load_dotenv
load_dotenv()

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
CORS(app, supports_credentials=True)
api = Api(app)

@app.route('/')
def home():
    return '<h1>Welcome to the airplane web page!</h1>'
    
api.add_resource(Company, '/company')
api.add_resource(CompanyList, '/company/<int:id>')

api.add_resource(Airplane, '/planes')
api.add_resource(AirplaneList, '/planes/<int:id>')

api.add_resource(TheOwner, '/owners')
api.add_resource(TheOwnerList, '/owners/<int:id>')

api.add_resource(PlaneOwner, '/ownership')
api.add_resource(PlaneOwnerList, '/ownership/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)