"""
image_controller.py

This module contains image-related routes.
"""

from fastapi import APIRouter
from app.models import DataFullPersonImage
from app.services import image_service

router = APIRouter()

@router.get("/GetImageByCode")
def get_image_by_code(id_image: int):
    """
    Return data from image by id image
    """
    return image_service.get_image_by_code(id_image)

@router.get("/GetImageByPerson")
def get_image_by_person(id_pessoa: int):
    """
    Return data from image by id_person
    """
    return image_service.get_image_by_person(id_pessoa)


@router.post("/PostImage")
def post_image(data_image: DataFullPersonImage):
    """
    Post data from a new image to save
    """
    return image_service.post_image(data_image)

@router.patch("/UpdateImage")
def update_image(data_image: DataFullPersonImage):
    """
    Update data image
    """
    return image_service.update_image(data_image)
