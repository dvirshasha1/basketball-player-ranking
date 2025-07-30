from flask import Blueprint, jsonify
from . import players

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "message": "Basketball Player Ranking API is running"
    })

# Register player routes
bp.register_blueprint(players.bp)
