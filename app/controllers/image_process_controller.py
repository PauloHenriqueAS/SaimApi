"""
image_process_controller.py

module with routes of image processing methods.
"""

from fastapi import APIRouter
from app.services import process_service

router = APIRouter()

@router.get("/Thresholding")
def get_image_thresholded(image: str):
    """
    Return image from image by id_person
    """
    return process_service.get_image_thresholded(image)
