from flask import Blueprint, jsonify, request
from ..models.player import Player
from ..services.player_service import PlayerService
from http import HTTPStatus

bp = Blueprint('players', __name__, url_prefix='/api/players')

@bp.route('', methods=['POST'])
def create_player():
    try:
        player = Player(**request.json)
        created_player = PlayerService.create_player(player)
        return jsonify(created_player.dict()), HTTPStatus.CREATED
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST

@bp.route('', methods=['GET'])
def get_players():
    try:
        skip = int(request.args.get('skip', 0))
        limit = int(request.args.get('limit', 100))
        players = PlayerService.get_players(skip, limit)
        return jsonify([player.dict() for player in players])
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@bp.route('/<player_id>', methods=['GET'])
def get_player(player_id):
    try:
        player = PlayerService.get_player(player_id)
        if player:
            return jsonify(player.dict())
        return jsonify({"error": "Player not found"}), HTTPStatus.NOT_FOUND
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@bp.route('/<player_id>', methods=['PUT'])
def update_player(player_id):
    try:
        player = Player(**request.json)
        updated_player = PlayerService.update_player(player_id, player)
        if updated_player:
            return jsonify(updated_player.dict())
        return jsonify({"error": "Player not found"}), HTTPStatus.NOT_FOUND
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.BAD_REQUEST

@bp.route('/<player_id>', methods=['DELETE'])
def delete_player(player_id):
    try:
        if PlayerService.delete_player(player_id):
            return '', HTTPStatus.NO_CONTENT
        return jsonify({"error": "Player not found"}), HTTPStatus.NOT_FOUND
    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
