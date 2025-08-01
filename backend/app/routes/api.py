from flask import Blueprint, jsonify

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "message": "Basketball Player Ranking API is running"
    })

# Import and register player routes
from backend.app.routes import players
bp.register_blueprint(players.bp)
