from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Database
from database.db import db
# Routes
from routes import Client

# Configuraciones
from config import DATABASE_CONNECTION_URI, secret_key

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)

db.init_app(app)
with app.app_context():
  db.create_all()

if __name__ == '__main__':

  # Blueprints
  app.register_blueprint(Client.client, url_prefix='/client')

  app.run(debug=True, port=3000)