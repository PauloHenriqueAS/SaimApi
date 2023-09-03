"""
app/Repositorys/configDb.py

This module contains database configurations.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

with open('../config.json', 'r') as config_file:
    config_data = json.load(config_file)

DATABASE_URL = config_data["database_url"]

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 
