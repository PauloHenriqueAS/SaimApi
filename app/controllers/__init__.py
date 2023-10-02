"""
app/controllers/__init__.py

Imports a module from the package so that it is available when importing the package
"""

#from .authentication_controller import router as authentication_router
from .user_controller import router as user_router
from .image_controller import router as image_router
from .health_controller import router as health_router
from .person_controller import router as person_router
from .dashboard_controller import router as dashboard_router
from .image_process_controller import router as process_router
