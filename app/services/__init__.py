"""
app/services/__init__.py

Imports a module from the package so that it is available when importing the package
"""
from .user_service import user_service
from .person_service import person_service
from .image_service import image_service
from .image_process_service import process_service
from .dashboard_service import dashboard_service

__all__ = [
    "user_service",
    "person_service",
    "image_service",
    "process_service",
    "dashboard_service",
]
