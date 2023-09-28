"""
user_controller.py

This module contains user-related routes.
"""

from fastapi import APIRouter
from app.models import User, UserFull
from app.services import user_service

router = APIRouter()

@router.get("/GetUsuarioByCode")
def get_user_by_code(email_user: str):
    """
    Return data from user by email
    """
    return user_service.get_user_by_code(email_user)

@router.post("/AutenticateUser")
def autenticate_user(data_user: User):
    """
    Verify if user have access to system
    """
    return user_service.autenticate_user(data_user)

@router.post("/PostUser")
def post_user(data_user: User):
    """
    Post data from a new user
    """
    return user_service.post_user(data_user)

@router.post("/PostFullUser")
def post_user_full(data_user_full: UserFull):
    """
    Post data from a new user
    """
    return user_service.post_user_full(data_user_full)


@router.patch("/UpdatePasswordUser")
def update_password_user(data_user: User):
    """
    Update data user
    """
    return user_service.update_password_user(data_user)
