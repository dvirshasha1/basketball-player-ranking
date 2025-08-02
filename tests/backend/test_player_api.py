import pytest
from flask import json
from http import HTTPStatus
from ..models.player import Player
from bson import ObjectId

@pytest.fixture
def sample_player_data():
    return {
        "name": "LeBron James",
        "team": "Lakers",
        "position": "SF",
        "offense": {
            "shooting": 85,
            "ball_handling": 90,
            "passing": 95,
            "speed": 85,
            "finishing": 90
        },
        "defense": {
            "perimeter_defense": 85,
            "interior_defense": 85,
            "steal": 80,
            "block": 85,
            "rebounding": 85
        }
    }

@pytest.fixture
def create_test_player(app, sample_player_data):
    """Create a test player in the database"""
    with app.app_context():
        player = Player(**sample_player_data)
        player.save()
        return player

def test_list_players_empty(client):
    """Test listing players when database is empty"""
    response = client.get('/api/players')
    assert response.status_code == HTTPStatus.OK
    data = json.loads(response.data)
    assert data['total'] == 0
    assert len(data['players']) == 0

def test_list_players_with_data(client, create_test_player):
    """Test listing players with data in database"""
    response = client.get('/api/players')
    assert response.status_code == HTTPStatus.OK
    data = json.loads(response.data)
    assert data['total'] == 1
    assert len(data['players']) == 1
    assert data['players'][0]['name'] == "LeBron James"

def test_list_players_pagination(client, sample_player_data):
    """Test player listing pagination"""
    # Create multiple players
    with client.application.app_context():
        for i in range(25):  # Create 25 players
            player_data = sample_player_data.copy()
            player_data['name'] = f"Player {i}"
            Player(**player_data).save()

    # Test first page
    response = client.get('/api/players?page=1&per_page=10')
    assert response.status_code == HTTPStatus.OK
    data = json.loads(response.data)
    assert len(data['players']) == 10
    assert data['total'] == 25
    assert data['page'] == 1
    assert data['pages'] == 3

def test_get_player(client, create_test_player):
    """Test getting a single player"""
    response = client.get(f'/api/players/{create_test_player.id}')
    assert response.status_code == HTTPStatus.OK
    data = json.loads(response.data)
    assert data['name'] == "LeBron James"
    assert data['team'] == "Lakers"

def test_get_player_not_found(client):
    """Test getting a non-existent player"""
    non_existent_id = str(ObjectId())
    response = client.get(f'/api/players/{non_existent_id}')
    assert response.status_code == HTTPStatus.NOT_FOUND

def test_create_player(client, sample_player_data):
    """Test creating a new player"""
    response = client.post('/api/players', 
                          data=json.dumps(sample_player_data),
                          content_type='application/json')
    assert response.status_code == HTTPStatus.CREATED
    data = json.loads(response.data)
    assert data['name'] == sample_player_data['name']
    assert 'overall_score' in data

def test_create_player_invalid_data(client):
    """Test creating a player with invalid data"""
    invalid_data = {
        "name": "",  # Invalid: empty name
        "team": "Lakers",
        "position": "INVALID"  # Invalid position
    }
    response = client.post('/api/players', 
                          data=json.dumps(invalid_data),
                          content_type='application/json')
    assert response.status_code == HTTPStatus.BAD_REQUEST
    data = json.loads(response.data)
    assert 'error' in data
    assert 'details' in data

def test_update_player(client, create_test_player):
    """Test updating an existing player"""
    update_data = {
        "name": "Updated Name",
        "team": "Warriors"
    }
    response = client.put(f'/api/players/{create_test_player.id}',
                         data=json.dumps(update_data),
                         content_type='application/json')
    assert response.status_code == HTTPStatus.OK
    data = json.loads(response.data)
    assert data['name'] == "Updated Name"
    assert data['team'] == "Warriors"

def test_update_player_not_found(client):
    """Test updating a non-existent player"""
    non_existent_id = str(ObjectId())
    update_data = {"name": "New Name"}
    response = client.put(f'/api/players/{non_existent_id}',
                         data=json.dumps(update_data),
                         content_type='application/json')
    assert response.status_code == HTTPStatus.NOT_FOUND

def test_delete_player(client, create_test_player):
    """Test deleting a player"""
    response = client.delete(f'/api/players/{create_test_player.id}')
    assert response.status_code == HTTPStatus.NO_CONTENT

    # Verify player is deleted
    get_response = client.get(f'/api/players/{create_test_player.id}')
    assert get_response.status_code == HTTPStatus.NOT_FOUND

def test_delete_player_not_found(client):
    """Test deleting a non-existent player"""
    non_existent_id = str(ObjectId())
    response = client.delete(f'/api/players/{non_existent_id}')
    assert response.status_code == HTTPStatus.NOT_FOUND
