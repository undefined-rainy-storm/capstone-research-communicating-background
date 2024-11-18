from flask import Flask
from flask_restful import Api, Resource
from datetime import datetime

class Sample(Resource):
    def get(self):
        return { 'status': 'ok', 'timestamp': datetime.now().isoformat() }
    
    def post(self):
        return { 'status': 'ok', 'timestamp': datetime.now().isoformat() }
