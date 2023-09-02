"""
health_controller.py

This module contains health check route.
"""

import datetime
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_health_check_api():
    """
    Return date time now
    """
    return { "code": 200, "mensagem": datetime.datetime.now()}
