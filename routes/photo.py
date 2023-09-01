import csv
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Photo, Portfolio
from cloudinary.uploader import upload 

api = Blueprint('api3', __name__)

@api.route('/portfolios/<int:portfolios_id>/photos', methods=['GET'])
@jwt_required()
def get_photos(portfolios_id):
    
    photos = Photo.query.filter_by(portfolios_id=portfolios_id).all()
    photos = list(map(lambda photo: photo.serialize(), photos))
    
    return jsonify(photos), 200
    
    
@api.route('/portfolios/<int:portfolios_id>/photos', methods=['POST'])
@jwt_required()
def create_photo(portfolios_id):
    
    portfolio = Portfolio.query.get(portfolios_id)
    
    if not portfolio:
        return jsonify({ "msg": "Portfolio doesn't exist, please try again!"}), 400
    
    # active = request.json.get('active')
    active = request.form['active']
    if not active:
        return jsonify({ "msg": "Active field is required!"}), 400
    
    if not 'imagen' in request.files:
        return jsonify({ "msg": "Image file is required!"}), 400
    
    imagen = request.files['imagen']

    response = upload(imagen, folder="photos_portfolios")

    photo = Photo()
    photo.filename = response['secure_url']
    photo.active = bool(active)
    photo.portfolios_id = portfolios_id
    photo.save()
    
    return jsonify({ "msg": "Images uploaded!", "photo": photo.serialize()}), 200


@api.route('/portfolios/<int:portfolios_id>/photos/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_photo(id):
    pass


@api.route('/file-upload', methods=['POST'])
def upload_file():
    
    if 'listado' in request.files:
        csv_file = request.files['listado']
        
    return jsonify({ "msg": "File uploaded!"}), 200