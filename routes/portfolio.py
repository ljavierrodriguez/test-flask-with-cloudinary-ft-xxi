from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Portfolio

api = Blueprint('api2', __name__)

@api.route('/portfolios', methods=['GET'])
@jwt_required()
def get_portfolios():
    users_id = get_jwt_identity()
    
    portfolios = Portfolio.query.filter_by(users_id=users_id).all()
    portfolios = [portfolio.serialize_with_photos() for portfolio in portfolios]
    
    return jsonify(portfolios), 200

@api.route('/portfolios', methods=['POST'])
@jwt_required()
def create_portfolio():
    
    users_id = get_jwt_identity()
    title = request.json.get('title')
    active = request.json.get('active')
    
    portfolio = Portfolio()
    portfolio.title = title
    portfolio.active = active
    portfolio.users_id = users_id
    
    portfolio.save()
    
    return jsonify(portfolio.serialize()), 201
    


@api.route('/portfolios/<int:id>', methods=['GET'])
@jwt_required()
def get_portfolio_by_id(id):
    pass

@api.route('/portfolios/<int:id>', methods=['PUT'])
@jwt_required()
def update_portfolio(id):
    pass

@api.route('/portfolios/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_portfolio(id):
    pass