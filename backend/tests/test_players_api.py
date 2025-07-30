import pytest
from http import HTTPStatus

def test_create_player(client):
    player_data = {
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
    
    response = client.post('/api/players', json=player_data)
    assert response.status_code == HTTPStatus.CREATED
    
    data = response.get_json()
    assert data['name'] == player_data['name']
    assert data['team'] == player_data['team']
    assert 'overall_score' in data
    assert isinstance(data['overall_score'], float)

def test_get_players(client, db):
    # First create a player
    player_data = {
        "name": "Stephen Curry",
        "team": "Warriors",
        "position": "PG",
        "offense": {
            "shooting": 95,
            "ball_handling": 90,
            "passing": 90,
            "speed": 85,
            "finishing": 85
        },
        "defense": {
            "perimeter_defense": 80,
            "interior_defense": 70,
            "steal": 85,
            "block": 70,
            "rebounding": 75
        }
    }
    
    client.post('/api/players', json=player_data)
    
    # Test GET players endpoint
    response = client.get('/api/players')
    assert response.status_code == HTTPStatus.OK
    
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]['name'] == player_data['name']
