"""
dashboard_controller.py

This module contains dashboard-related routes.
"""

from fastapi import APIRouter
from app.services import dashboard_service

router = APIRouter()

@router.get("/GetDataDashImages")
def get_dash_images():
    """
    Return statistics from images
    """
    return dashboard_service.get_dash_images()

@router.get("/GetDataDashUsers")
def get_dash_users():
    """
    Return statistics from users
    """
    return dashboard_service.get_dash_users()

@router.get("/GetDataDashProcessingMethods")
def get_dash_precessing_methods():
    """
    Return statistics from processing images
    """
    return dashboard_service.get_dash_precessing_methods()
