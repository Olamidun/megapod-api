import os
from flask import Flask
from flask_restful import Api
from .endpoints import HelloWorld
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
    """Creates a Flask App"""
    app = Flask(__name__)
    # Get the corresponding database uri from docker-compose
    app_settings = os.environ.get('APP_SETTINGS')
    app.config.from_object(app_settings)
    # set up extensions
    db.init_app(app)
    
    api = Api(app)

    api.add_resource(HelloWorld, '/hello_world')
    return app