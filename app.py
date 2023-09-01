import os
import cloudinary
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from models import db

from routes.auth import api as api_auth
from routes.portfolio import api as api_portfolio
from routes.photo import api as api_photos

load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

db.init_app(app)
Migrate(app, db)
jwt = JWTManager(app)
CORS(app)

cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
    secure=True
)

app.register_blueprint(api_auth, url_prefix='/api')
app.register_blueprint(api_portfolio, url_prefix='/api')
app.register_blueprint(api_photos, url_prefix='/api')

@app.route('/')
def main():
    return jsonify({ "msg": "API REST Flask with CLOUDINARY"})


if __name__ == '__main__':
    app.run()

