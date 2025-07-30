import pytest
from backend.app import create_app
from backend.app.db import get_db

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'DB_NAME': 'basketball_rankings_test'
    })
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def db(app):
    with app.app_context():
        db = get_db()
        # Clear database before each test
        db.players.delete_many({})
        yield db
        # Clean up after tests
        db.players.delete_many({})
