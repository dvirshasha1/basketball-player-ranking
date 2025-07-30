from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from http import HTTPStatus
from . import db

def create_app(config=None):
    load_dotenv()
    
    app = Flask(__name__)
    
    # Enable CORS for development
    CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000"]}})
    
    # Configure app
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", "dev"),
        DB_HOST=os.getenv("DB_HOST", "localhost"),
        DB_PORT=int(os.getenv("DB_PORT", "27017")),
        DB_NAME=os.getenv("DB_NAME", "basketball_rankings")
    )
    
    if config:
        app.config.update(config)
    
    # Register database handlers
    app.teardown_appcontext(db.close_db)
    
    # Register error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"error": "Resource not found"}), HTTPStatus.NOT_FOUND
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal server error"}), HTTPStatus.INTERNAL_SERVER_ERROR
    
    # Register blueprints
    from .routes import api
    app.register_blueprint(api.bp)
    
    return app
