from mongoengine import connect, disconnect
from backend.models.player import Player
from backend.services.player_service import PlayerService

def init_db(db_url="mongodb://localhost:27017/basketball_rankings"):
    """Initialize the database with indexes and initial setup"""
    # Ensure we're disconnected first
    disconnect()
    
    # Connect to database
    connect(host=db_url)
    
    # Create text index on name and team fields for text search
    Player._get_collection().create_index([("name", "text"), ("team", "text")])
    
    # Create other necessary indexes
    Player._get_collection().create_index([("overall_score", -1)])  # For sorting
    Player._get_collection().create_index([("position", 1)])        # For filtering
    Player._get_collection().create_index([("team", 1)])           # For filtering
    
    print("Database initialization completed successfully.")

if __name__ == "__main__":
    init_db()
