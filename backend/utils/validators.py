from typing import Dict, Any, List
from marshmallow import Schema, fields, validate, ValidationError

class StatSchema(Schema):
    min_value = 0
    max_value = 100
    
    value = fields.Integer(
        required=True,
        validate=validate.Range(min=min_value, max=max_value)
    )

class OffenseSchema(Schema):
    shooting = fields.Integer(required=True, validate=validate.Range(min=0, max=100))
    ball_handling = fields.Integer(required=True, validate=validate.Range(min=0, max=100))
    passing = fields.Integer(required=True, validate=validate.Range(min=0, max=100))
    speed = fields.Integer(required=True, validate=validate.Range(min=0, max=100))
    finishing = fields.Integer(required=True, validate=validate.Range(min=0, max=100))

class DefenseSchema(Schema):
    perimeter_defense = fields.Integer(required=True, validate=validate.Range(min=0, max=100))
    interior_defense = fields.Integer(required=True, validate=validate.Range(min=0, max=100))
    steal = fields.Integer(required=True, validate=validate.Range(min=0, max=100))
    block = fields.Integer(required=True, validate=validate.Range(min=0, max=100))
    rebounding = fields.Integer(required=True, validate=validate.Range(min=0, max=100))

class PlayerSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=2, max=50))
    team = fields.String(required=True)
    position = fields.String(required=True, validate=validate.OneOf(['PG', 'SG', 'SF', 'PF', 'C']))
    offense = fields.Nested(OffenseSchema, required=True)
    defense = fields.Nested(DefenseSchema, required=True)

def validate_player_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate player data against the schema
    
    Args:
        data: Dictionary containing player data
        
    Returns:
        Validated and cleaned data
        
    Raises:
        ValidationError: If data fails validation
    """
    schema = PlayerSchema()
    return schema.load(data)

def format_validation_errors(errors: Dict[str, List[str]]) -> Dict[str, str]:
    """
    Format validation errors into a user-friendly format
    
    Args:
        errors: Dictionary of validation errors
        
    Returns:
        Formatted error messages
    """
    formatted_errors = {}
    for field, messages in errors.items():
        if isinstance(messages, dict):
            formatted_errors[field] = format_validation_errors(messages)
        else:
            formatted_errors[field] = messages[0] if messages else 'Invalid value'
    return formatted_errors
