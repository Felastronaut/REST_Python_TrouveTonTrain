from flask import Flask
from flask_restful import Api

from resources.devise import Devise

app = Flask(__name__)
api = Api(app)

api.add_resource(Devise, "/devise")

