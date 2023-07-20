"""
health_controller.py

This module contains health check route.
"""

import datetime
from fastapi import APIRouter

router = APIRouter()

@router.get("/HealthCheck")
def get_health_check_api():
    """
    Return date time now
    """
    return datetime.datetime.now()
