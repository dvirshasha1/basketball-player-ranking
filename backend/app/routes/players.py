from flask import Blueprint, jsonify, request
from http import HTTPStatus
from backend import db

bp = Blueprint('players', __name__)

@bp.route('/players', methods=['GET'])
def get_players():
    """Get all players"""
    database = db.get_db()
    players = list(database.players.find({}, {'_id': False}))
    return jsonify(players), HTTPStatus.OK

@bp.route('/players/<player_id>', methods=['GET'])
def get_player(player_id):
    """Get a specific player"""
    database = db.get_db()
    player = database.players.find_one({'id': player_id}, {'_id': False})
    if not player:
        return jsonify({'error': 'Player not found'}), HTTPStatus.NOT_FOUND
    return jsonify(player), HTTPStatus.OK

@bp.route('/players', methods=['POST'])
def create_player():
    """Create a new player"""
    player_data = request.get_json()
    if not player_data:
        return jsonify({'error': 'No data provided'}), HTTPStatus.BAD_REQUEST
    
    database = db.get_db()
    result = database.players.insert_one(player_data)
    if result.inserted_id:
        return jsonify({'message': 'Player created successfully'}), HTTPStatus.CREATED
    return jsonify({'error': 'Failed to create player'}), HTTPStatus.INTERNAL_SERVER_ERROR
