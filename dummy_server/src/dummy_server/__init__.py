from flask import Flask
from flask_restful import Api

from . import api as api_src

def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(api_src.sample.Sample, '/sample')
    api.add_resource(api_src.query.Query, '/query')
    return app
