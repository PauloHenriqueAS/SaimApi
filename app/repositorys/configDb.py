"""
app/Repositorys/configDb.py

This module contains database configurations.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:iP0vskRkccKZc2TUgb8C@database-weatherwise.cdi5ncgph4r1.sa-east-1.rds.amazonaws.com:5432/db_WeatherWise"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 
