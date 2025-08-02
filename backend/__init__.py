from flask import Flask
from flask_cors import CORS
from backend.routes.players import players_bp

def create_app(config=None):
    app = Flask(__name__)
    
    # Configure CORS
    CORS(app)
    
    # Register blueprints
    app.register_blueprint(players_bp)
    
    # Apply configuration if provided
    if config:
        app.config.update(config)
    
    return app
