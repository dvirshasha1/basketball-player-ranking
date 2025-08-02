from typing import List, Dict, Optional
from ..models.player import Player
from ..services.scoring_service import ScoringService
from ..utils.validators import validate_player_data
from mongoengine.errors import ValidationError, DoesNotExist
from bson import ObjectId

class PlayerService:
    def __init__(self):
        self.scoring_service = ScoringService()

    def create_player(self, player_data: Dict) -> Player:
        """
        Create a new player
        
        Args:
            player_data: Dictionary containing player information
            
        Returns:
            Created Player instance
            
        Raises:
            ValidationError: If player data is invalid
        """
        from ..db import get_db
        
        # Validate input data
        validated_data = validate_player_data(player_data)
        
        # Calculate overall score
        validated_data['overall_score'] = self.scoring_service.calculate_overall_score(
            validated_data['offense'],
            validated_data['defense']
        )
        
        # Create player
        db = get_db()
        result = db.players.insert_one(validated_data)
        
        # Get the created player
        player_doc = db.players.find_one({'_id': result.inserted_id})
        player_doc['id'] = str(player_doc.pop('_id'))
        
        return Player(**player_doc)

    def get_player(self, player_id: str) -> Player:
        """
        Get a player by ID
        
        Args:
            player_id: Player's ID
            
        Returns:
            Player instance
            
        Raises:
            DoesNotExist: If player not found
        """
        return Player.objects.get(id=ObjectId(player_id))

    def list_players(self) -> List[Player]:
        """
        List all players
        
        Returns:
            List of Player instances
        """
        from ..db import get_db
        
        db = get_db()
        players = []
        
        for doc in db.players.find():
            doc['id'] = str(doc.pop('_id'))
            players.append(Player(**doc))
        
        return players

    def update_player(self, player_id: str, player_data: Dict) -> Player:
        """
        Update a player
        
        Args:
            player_id: Player's ID
            player_data: Updated player data
            
        Returns:
            Updated Player instance
            
        Raises:
            DoesNotExist: If player not found
            ValidationError: If update data is invalid
        """
        player = self.get_player(player_id)
        
        # Validate update data
        validated_data = validate_player_data(player_data)
        
        # Update fields
        for key, value in validated_data.items():
            setattr(player, key, value)
        
        # Recalculate overall score
        player.calculate_overall_score()
        
        # Save changes
        player.save()
        
        return player

    def delete_player(self, player_id: str) -> bool:
        """
        Delete a player
        
        Args:
            player_id: Player's ID
            
        Returns:
            True if player was deleted
            
        Raises:
            DoesNotExist: If player not found
        """
        player = self.get_player(player_id)
        player.delete()
        return True
