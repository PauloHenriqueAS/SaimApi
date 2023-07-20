"""
user_controller.py

This module contains user-related routes.
"""

from fastapi import APIRouter
from app.models import User
from app.services import user_service

router = APIRouter()

@router.get("/GetUsuarioByCode/{email_user}")
def get_usuario_by_code(email_user: str):
    """
    Return data from user by email
    """
    return user_service.get_usuario_by_code(email_user)

@router.post("/AutenticateUser")
def autenticate_user(data_user: User):
    """
    Return confirmation if user is authenticated
    """
    return user_service.autenticate_user(data_user)

@router.post("/PostUser")
def post_user(data_user: User):
    """
    Post data from a new user
    """
    return user_service.post_user(data_user)

@router.patch("/UpdatePasswordUser")
def update_password_user(data_user: User):
    """
    Update data user
    """
    return user_service.update_password_user(data_user)
