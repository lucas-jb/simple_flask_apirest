from flask import Flask
from app.routes import products#, users

app = Flask(__name__)
def create_app():
  app.register_blueprint(products.app)
  #app.register_bluleprint(users.app)
  return app