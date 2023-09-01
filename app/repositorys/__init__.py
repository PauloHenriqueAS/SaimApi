"""
app/repository s/__init__.py

Imports a module from the package so that it is available when importing the package
"""
from .user_repository import user_repository 
from .person_repository  import person_repository 
from .image_repository  import image_repository 
from .image_process_repository  import process_repository 
from .dashboard_repository  import dashboard_repository 

__all__ = [
    "user_repository ",
    "person_repository ",
    "image_repository ",
    "process_repository ",
    "dashboard_repository ",
]
