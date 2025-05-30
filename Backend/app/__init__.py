from flask import flask
from app.routes import auth

def create_app():
  app - Flask(__name__, instance_relative_config=True)

  app.config.from_pyfile('config.py')
  app.secret_key = app.config['SECRET_KEY']

  app.register_blueprint(auth)

  return app