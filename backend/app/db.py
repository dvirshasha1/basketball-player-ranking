from pymongo import MongoClient
from flask import current_app, g
import os

def get_db():
    """Return database connection"""
    if 'db' not in g:
        client = MongoClient(
            host=os.getenv('DB_HOST', 'localhost'),
            port=int(os.getenv('DB_PORT', 27017)),
            username=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        g.db = client[os.getenv('DB_NAME', 'basketball_rankings')]
    return g.db

def close_db(e=None):
    """Close database connection"""
    db = g.pop('db', None)
    if db is not None:
        db.client.close()
