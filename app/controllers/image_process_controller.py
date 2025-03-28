"""
image_process_controller.py

module with routes of image processing methods.
"""

from fastapi import APIRouter
from app.services import process_service
from app.models import ImageThreshold,ImageBlur, ImageDilate, ImageErosion, ImageSobelX, ImageSobelY, ImageSobelXY, ImageLaplacian, ImageThinning, ImageMeasurement

router = APIRouter()

@router.post("/Thresholding")
async def get_image_threshold(dataImageThreshold: ImageThreshold):
    """
    Return image from image by id_person
    """
    return await process_service.get_image_threshold(dataImageThreshold)

@router.post("/Blur")
async def get_image_blur(dataImageBlur: ImageBlur):
    """
    Return image from image by id_person
    """
    return await process_service.get_image_blur(dataImageBlur)

@router.post("/Dilate")
async def get_image_dilate(dataImageDilate: ImageDilate):
    """
    Return image from image by id_person
    """
    return await process_service.get_image_dilate(dataImageDilate)

@router.post("/Erosion")
async def get_image_erosion(dataImageErosion: ImageErosion):
    """
    Return image from image by id_person
    """
    return await process_service.get_image_erosion(dataImageErosion)

@router.post("/SobelX")
async def get_image_sobelX(dataImageSobelX: ImageSobelX):
    """
    Return image from image by id_person
    """
    return await process_service.get_image_sobelX(dataImageSobelX)

@router.post("/SobelY")
async def get_image_sobelY(dataImageSobelY: ImageSobelY):
    """
    Return image from image by id_person
    """
    return await process_service.get_image_sobelY(dataImageSobelY)

@router.post("/SobelXY")
async def get_image_sobelXY(dataImageSobelXY: ImageSobelXY):
    """
    Return image from image by id_person
    """
    return await process_service.get_image_sobelXY(dataImageSobelXY)

@router.post("/Laplacian")
async def get_image_laplacian(dataImageLaplacian: ImageLaplacian):
    """
    Return image from image by id_person
    """
    return await process_service.get_image_laplacian(dataImageLaplacian)

@router.post("/Thinning")
async def get_image_thinning(dataImageThinning: ImageThinning):
    """
    Return image from image by id_person
    """
    return await process_service.get_image_thinning(dataImageThinning)

# @router.post("/Measurement")
# async def get_image_measurement(dataImageMeasurement: ImageMeasurement):
#     """
#     Return image from image by id_person
#     """
#     return await process_service.get_image_measurement(dataImageMeasurement)
