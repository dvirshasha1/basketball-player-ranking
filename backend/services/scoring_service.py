from typing import Dict

class ScoringService:
    @staticmethod
    def calculate_overall_score(offense: Dict[str, int], defense: Dict[str, int]) -> float:
        """
        Calculate the player's overall score based on offense and defense stats
        
        Args:
            offense: Dictionary containing offensive stats
            defense: Dictionary containing defensive stats
            
        Returns:
            Float representing the overall score (0-100)
        """
        if not offense or not defense:
            raise ValueError("Both offense and defense stats are required")

        # Calculate average offensive score
        offense_score = sum(offense.values()) / len(offense)
        
        # Calculate average defensive score
        defense_score = sum(defense.values()) / len(defense)
        
        # Overall score is the average of offense and defense
        overall_score = (offense_score + defense_score) / 2
        
        return round(overall_score, 2)

    @staticmethod
    def calculate_position_weighted_score(
        offense: Dict[str, int],
        defense: Dict[str, int],
        position: str
    ) -> float:
        """
        Calculate position-weighted overall score based on player's position
        
        Args:
            offense: Dictionary containing offensive stats
            defense: Dictionary containing defensive stats
            position: Player's position (PG, SG, SF, PF, C)
            
        Returns:
            Float representing the weighted overall score (0-100)
        """
        # Position-specific weights for offensive and defensive attributes
        POSITION_WEIGHTS = {
            'PG': {
                'offense': {
                    'ball_handling': 0.3,
                    'passing': 0.3,
                    'shooting': 0.2,
                    'speed': 0.1,
                    'finishing': 0.1
                },
                'defense': {
                    'perimeter_defense': 0.4,
                    'steal': 0.3,
                    'interior_defense': 0.1,
                    'block': 0.1,
                    'rebounding': 0.1
                }
            },
            'SG': {
                'offense': {
                    'shooting': 0.4,
                    'ball_handling': 0.2,
                    'speed': 0.2,
                    'passing': 0.1,
                    'finishing': 0.1
                },
                'defense': {
                    'perimeter_defense': 0.4,
                    'steal': 0.3,
                    'interior_defense': 0.1,
                    'block': 0.1,
                    'rebounding': 0.1
                }
            },
            'SF': {
                'offense': {
                    'shooting': 0.3,
                    'finishing': 0.2,
                    'ball_handling': 0.2,
                    'speed': 0.2,
                    'passing': 0.1
                },
                'defense': {
                    'perimeter_defense': 0.3,
                    'interior_defense': 0.2,
                    'steal': 0.2,
                    'rebounding': 0.2,
                    'block': 0.1
                }
            },
            'PF': {
                'offense': {
                    'finishing': 0.3,
                    'shooting': 0.2,
                    'speed': 0.2,
                    'ball_handling': 0.15,
                    'passing': 0.15
                },
                'defense': {
                    'interior_defense': 0.3,
                    'rebounding': 0.3,
                    'block': 0.2,
                    'perimeter_defense': 0.1,
                    'steal': 0.1
                }
            },
            'C': {
                'offense': {
                    'finishing': 0.4,
                    'shooting': 0.2,
                    'passing': 0.2,
                    'ball_handling': 0.1,
                    'speed': 0.1
                },
                'defense': {
                    'rebounding': 0.3,
                    'interior_defense': 0.3,
                    'block': 0.3,
                    'perimeter_defense': 0.05,
                    'steal': 0.05
                }
            }
        }
        
        weights = POSITION_WEIGHTS.get(position)
        if not weights:
            raise ValueError(f"Invalid position: {position}")

        # Calculate weighted offensive score
        offensive_score = sum(
            offense[stat] * weight
            for stat, weight in weights['offense'].items()
        )

        # Calculate weighted defensive score
        defensive_score = sum(
            defense[stat] * weight
            for stat, weight in weights['defense'].items()
        )

        # Overall score is the average of weighted offense and defense scores
        return round((offensive_score + defensive_score) / 2, 2)
