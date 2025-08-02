import pytest
from flask import Flask
from mongoengine import connect, disconnect
from backend.models.player import Player

@pytest.fixture(scope='session')
def app():
    """Create a Flask application for testing"""
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config['MONGODB_DB'] = 'test_basketball_rankings'
    return app

@pytest.fixture(scope='function')
def client(app):
    """Create a test client"""
    return app.test_client()

@pytest.fixture(autouse=True)
def setup_db():
    """Set up test database before each test and clean up after"""
    # Set up test database connection
    disconnect()  # Disconnect from any existing connection
    connect('test_basketball_rankings', host='mongodb://localhost:27017/test_basketball_rankings')
    
    yield  # Run the test
    
    # Clean up after test
    Player.objects.delete()
