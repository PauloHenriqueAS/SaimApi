"""
health_controller.py

This module contains health check route.
"""

import datetime
from fastapi import APIRouter
from app.middleware import saim_api_response

router = APIRouter()

@router.get("/")
async def get_health_check_api():
    """
    Return date time now
    """
    return saim_api_response.create_response(True, datetime.datetime.now())
