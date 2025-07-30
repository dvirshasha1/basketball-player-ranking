from typing import List, Optional
from bson import ObjectId
from ..models.player import Player
from ..db import get_db

class PlayerService:
    @staticmethod
    def create_player(player: Player) -> Player:
        """Create a new player"""
        player.calculate_overall_score()
        db = get_db()
        result = db.players.insert_one(player.to_dict())
        player.id = str(result.inserted_id)
        return player

    @staticmethod
    def get_player(player_id: str) -> Optional[Player]:
        """Get a player by ID"""
        db = get_db()
        player_data = db.players.find_one({"_id": ObjectId(player_id)})
        if player_data:
            player_data['id'] = str(player_data.pop('_id'))
            return Player(**player_data)
        return None

    @staticmethod
    def get_players(skip: int = 0, limit: int = 100) -> List[Player]:
        """Get all players with pagination"""
        db = get_db()
        players = []
        cursor = db.players.find().skip(skip).limit(limit)
        
        for player_data in cursor:
            player_data['id'] = str(player_data.pop('_id'))
            players.append(Player(**player_data))
        
        return players

    @staticmethod
    def update_player(player_id: str, player_update: Player) -> Optional[Player]:
        """Update a player"""
        db = get_db()
        player_update.calculate_overall_score()
        result = db.players.update_one(
            {"_id": ObjectId(player_id)},
            {"$set": player_update.to_dict()}
        )
        
        if result.modified_count:
            return PlayerService.get_player(player_id)
        return None

    @staticmethod
    def delete_player(player_id: str) -> bool:
        """Delete a player"""
        db = get_db()
        result = db.players.delete_one({"_id": ObjectId(player_id)})
        return result.deleted_count > 0
