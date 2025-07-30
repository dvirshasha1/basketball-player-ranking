from datetime import datetime
from pydantic import BaseModel, Field, validator
from typing import Dict, Optional
from enum import Enum

class Position(str, Enum):
    PG = "PG"  # Point Guard
    SG = "SG"  # Shooting Guard
    SF = "SF"  # Small Forward
    PF = "PF"  # Power Forward
    C = "C"    # Center

class Stats(BaseModel):
    shooting: int = Field(..., ge=0, le=100)
    ball_handling: int = Field(..., ge=0, le=100)
    passing: int = Field(..., ge=0, le=100)
    speed: int = Field(..., ge=0, le=100)
    finishing: int = Field(..., ge=0, le=100)

    @validator('*')
    def validate_stat_range(cls, v):
        if not 0 <= v <= 100:
            raise ValueError('Stat must be between 0 and 100')
        return v

class DefensiveStats(BaseModel):
    perimeter_defense: int = Field(..., ge=0, le=100)
    interior_defense: int = Field(..., ge=0, le=100)
    steal: int = Field(..., ge=0, le=100)
    block: int = Field(..., ge=0, le=100)
    rebounding: int = Field(..., ge=0, le=100)

    @validator('*')
    def validate_stat_range(cls, v):
        if not 0 <= v <= 100:
            raise ValueError('Stat must be between 0 and 100')
        return v

class Player(BaseModel):
    id: Optional[str] = None
    name: str = Field(..., min_length=2, max_length=50)
    team: str
    position: Position
    offense: Stats
    defense: DefensiveStats
    overall_score: float = 0.0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    def calculate_overall_score(self) -> float:
        """Calculate overall score based on offensive and defensive stats"""
        offense_stats = [
            self.offense.shooting,
            self.offense.ball_handling,
            self.offense.passing,
            self.offense.speed,
            self.offense.finishing
        ]
        
        defense_stats = [
            self.defense.perimeter_defense,
            self.defense.interior_defense,
            self.defense.steal,
            self.defense.block,
            self.defense.rebounding
        ]
        
        # Equal weight to offense and defense
        offense_score = sum(offense_stats) / len(offense_stats)
        defense_score = sum(defense_stats) / len(defense_stats)
        
        self.overall_score = round((offense_score + defense_score) / 2, 1)
        return self.overall_score

    def to_dict(self) -> Dict:
        """Convert model to dictionary for MongoDB storage"""
        return {
            "name": self.name,
            "team": self.team,
            "position": self.position,
            "offense": self.offense.dict(),
            "defense": self.defense.dict(),
            "overall_score": self.overall_score,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
