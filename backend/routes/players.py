from flask import Blueprint, request, jsonify
from http import HTTPStatus
from ..services.player_service import PlayerService
from ..utils.validators import validate_player_data, format_validation_errors
from marshmallow import ValidationError
from bson.errors import InvalidId
from mongoengine.errors import DoesNotExist, ValidationError as MongoValidationError

# Create blueprint and service instance
players_bp = Blueprint('players', __name__, url_prefix='/api/players')
player_service = PlayerService()

@players_bp.route('', methods=['GET', 'POST'])
def list_or_create_players():
    """List all players or create a new one"""
    if request.method == 'POST':
        try:
            player_data = request.get_json()
            new_player = player_service.create_player(player_data)
            return jsonify(new_player.dict()), HTTPStatus.CREATED
        except ValidationError as e:
            return jsonify({'errors': format_validation_errors(e)}), HTTPStatus.BAD_REQUEST
        except Exception as e:
            import traceback
            print(f"Error creating player: {e}\n{traceback.format_exc()}")
            return jsonify({'error': str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    
    try:
        players = player_service.list_players()
        return jsonify([p.dict() for p in players]), HTTPStatus.OK
    except Exception as e:
        return jsonify({'error': str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR
    """List all players with pagination and filtering"""
    try:
        # Get query parameters
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 20))
        sort_by = request.args.get('sort_by', 'overall_score')
        order = request.args.get('order', 'desc')
        
        # Get filters from query parameters
        filters = {}
        if 'position' in request.args:
            filters['position'] = request.args['position']
        if 'team' in request.args:
            filters['team'] = request.args['team']
        if 'name' in request.args:
            filters['name'] = request.args['name']

        # Get players from service
        result = player_service.list_players(
            page=page,
            per_page=per_page,
            sort_by=sort_by,
            order=order,
            filters=filters
        )
        
        return jsonify(result), HTTPStatus.OK

    except ValueError as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), HTTPStatus.INTERNAL_SERVER_ERROR

@players_bp.route('/<player_id>', methods=['GET'])
def get_player(player_id):
    """Get a single player by ID"""
    try:
        player = player_service.get_player(player_id)
        return jsonify(player.to_dict()), HTTPStatus.OK
    
    except InvalidId:
        return jsonify({'error': 'Invalid player ID format'}), HTTPStatus.BAD_REQUEST
    except DoesNotExist:
        return jsonify({'error': 'Player not found'}), HTTPStatus.NOT_FOUND
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), HTTPStatus.INTERNAL_SERVER_ERROR

@players_bp.route('/api/players', methods=['POST'])
def create_player():
    """Create a new player"""
    try:
        # Validate request data
        player_data = request.get_json()
        if not player_data:
            return jsonify({'error': 'No data provided'}), HTTPStatus.BAD_REQUEST

        # Create player using service
        player = player_service.create_player(player_data)
        return jsonify(player.to_dict()), HTTPStatus.CREATED

    except ValidationError as e:
        return jsonify({'error': 'Validation error', 'details': format_validation_errors(e.messages)}), HTTPStatus.BAD_REQUEST
    except MongoValidationError as e:
        return jsonify({'error': 'Validation error', 'details': str(e)}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), HTTPStatus.INTERNAL_SERVER_ERROR

@players_bp.route('/api/players/<player_id>', methods=['PUT'])
def update_player(player_id):
    """Update an existing player"""
    try:
        # Validate request data
        player_data = request.get_json()
        if not player_data:
            return jsonify({'error': 'No data provided'}), HTTPStatus.BAD_REQUEST

        # Update player using service
        player = player_service.update_player(player_id, player_data)
        return jsonify(player.to_dict()), HTTPStatus.OK

    except InvalidId:
        return jsonify({'error': 'Invalid player ID format'}), HTTPStatus.BAD_REQUEST
    except DoesNotExist:
        return jsonify({'error': 'Player not found'}), HTTPStatus.NOT_FOUND
    except ValidationError as e:
        return jsonify({'error': 'Validation error', 'details': format_validation_errors(e.messages)}), HTTPStatus.BAD_REQUEST
    except MongoValidationError as e:
        return jsonify({'error': 'Validation error', 'details': str(e)}), HTTPStatus.BAD_REQUEST
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), HTTPStatus.INTERNAL_SERVER_ERROR

@players_bp.route('/api/players/<player_id>', methods=['DELETE'])
def delete_player(player_id):
    """Delete a player"""
    try:
        player_service.delete_player(player_id)
        return '', HTTPStatus.NO_CONTENT

    except InvalidId:
        return jsonify({'error': 'Invalid player ID format'}), HTTPStatus.BAD_REQUEST
    except DoesNotExist:
        return jsonify({'error': 'Player not found'}), HTTPStatus.NOT_FOUND
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), HTTPStatus.INTERNAL_SERVER_ERROR
