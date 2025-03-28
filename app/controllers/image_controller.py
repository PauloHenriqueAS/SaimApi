"""
image_controller.py

This module contains image-related routes.
"""

from fastapi import APIRouter
from app.models import DataFullPersonImage
from app.services import image_service

router = APIRouter()

@router.get("/GetImageByCode")
async def get_image_by_code(id_image: int):
    """
    return await data from image by id image
    """
    return await image_service.get_image_by_code(id_image)

@router.get("/GetImageByPerson")
async def get_image_by_person(id_pessoa: int):
    """
    return await data from image by id_person
    """
    return await image_service.get_image_by_person(id_pessoa)


@router.post("/PostImage")
async def post_image(data_image: DataFullPersonImage):
    """
    Post data from a new image to save
    """
    return await image_service.post_image(data_image)

@router.patch("/UpdateImage")
async def update_image(data_image: DataFullPersonImage):
    """
    Update data image
    """
    return await image_service.update_image(data_image)

@router.delete("/DeleteImage")
async def delete_image(id_image: int, id_person: int):
    """
    Delete data image
    """
    return await image_service.delete_image(id_image, id_person)