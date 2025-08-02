from datetime import datetime

class Player:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs['name']
        self.team = kwargs['team']
        self.position = kwargs['position']
        self.offense = kwargs['offense']
        self.defense = kwargs['defense']
        self.overall_score = kwargs.get('overall_score', 0.0)
        self.created_at = kwargs.get('created_at', datetime.utcnow())
        self.updated_at = kwargs.get('updated_at', datetime.utcnow())
        
        # Validate stats
        self._validate_stats()
        # Calculate initial overall score if not provided
        if not self.overall_score:
            self.calculate_overall_score()

    def _validate_stats(self):
        """Validate offense and defense stats"""
        offense_fields = ['shooting', 'ball_handling', 'passing', 'speed', 'finishing']
        defense_fields = ['perimeter_defense', 'interior_defense', 'steal', 'block', 'rebounding']
        
        # Check offense stats
        if not all(field in self.offense for field in offense_fields):
            raise ValueError(f"Missing required offense fields. Required: {offense_fields}")
        if not all(0 <= self.offense[field] <= 100 for field in offense_fields):
            raise ValueError("All offense stats must be between 0 and 100")

        # Check defense stats
        if not all(field in self.defense for field in defense_fields):
            raise ValueError(f"Missing required defense fields. Required: {defense_fields}")
        if not all(0 <= self.defense[field] <= 100 for field in defense_fields):
            raise ValueError("All defense stats must be between 0 and 100")

    def calculate_overall_score(self):
        """Calculate the overall score based on offense and defense stats"""
        offense_stats = sum(self.offense.values()) / len(self.offense)
        defense_stats = sum(self.defense.values()) / len(self.defense)
        self.overall_score = round((offense_stats + defense_stats) / 2, 2)

    def dict(self):
        """Convert the player model to a dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'team': self.team,
            'position': self.position,
            'offense': self.offense,
            'defense': self.defense,
            'overall_score': self.overall_score,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }