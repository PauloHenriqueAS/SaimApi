"""
user_controller.py

This module contains user-related routes.
"""

from fastapi import APIRouter
from app.models import User, UserFull
from app.services import user_service

router = APIRouter()

@router.get("/GetUsuarioByCode")
async def get_user_by_code(email_user: str):
    """
    return await data from user by email
    """
    return await user_service.get_user_by_code(email_user)

@router.post("/AutenticateUser")
async def autenticate_user(data_user: User):
    """
    Verify if user have access to system
    """
    #return await saim_api_response.create_response(True, 'riofjore', 'dofdjmfo')
    print(data_user)

    return await user_service.autenticate_user(data_user)

@router.post("/PostUser")
async def post_user(data_user: User):
    """
    Post data from a new user
    """

    return await user_service.post_user(data_user)

@router.post("/PostFullUser")
async def post_user_full(data_user_full: UserFull):
    """
    Post data from a new user
    """
    return await user_service.post_user_full(data_user_full)


@router.patch("/UpdatePasswordUser")
async def update_password_user(data_user: User):
    """
    Update data user
    """
    return await user_service.update_password_user(data_user)
