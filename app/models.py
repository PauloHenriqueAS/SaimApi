"""
models.py

This module contains all models that are being used in api.
"""

from datetime import date
from typing import Optional, Text
from pydantic import BaseModel

class Person(BaseModel):
    """
    Model of Person
    """
    id_pessoa: Optional[int] = None
    instituicao_pessoa: str
    uf_pessoa: str
    nome_pessoa: str
    tipo_pessoa: str
    id_user: str

class User(BaseModel):
    """
    Model of User
    """
    id_user: Optional[int] = None
    email_user: str
    password_user: str
    flg_activated: Optional[bool] =  None
    token_reset: Optional[str] =  None

class UserAuth(BaseModel):
    """
    Model of User
    """
    id_user: Optional[int] = None
    id_pessoa: int
    email_user: str
    password_user: str

class UserFull(BaseModel):
    """
    Model of Full data User 
    """
    id_user: Optional[int] = None
    id_pessoa: Optional[int] = None
    email_user: str
    password_user: str
    nome_pessoa: str
    uf_pessoa: str
    instituicao_pessoa: str
    password_confirmation: str
    tipo_pessoa: str
    token_reset: Optional[str] = None

class Image(BaseModel):
    """
    Model of Image
    """
    id_image: Optional[int] = None
    date_image: Optional[date] = None
    name_image: Optional[str] = None
    image: str

class PersonImage(BaseModel):
    """
    Model of Relation Image and Person
    """
    id_img_pes: Optional[int] = None
    id_pessoa: int
    id_imagem: int

class DataFullPersonImage(BaseModel):
    """
    Model of full data from relation Image and Person
    """
    id_img_pes: Optional[int] = None
    id_imagem: Optional[int] = None
    date_image: Optional[date] = None
    name_image: Optional[str] = None
    extension_image: Optional[str] = None
    id_pessoa: int
    image: Text

class ImageThreshold(BaseModel):
    """
    Model of Image Threshold
    """
    id_image: int
    val_min: int
    val_max: int

class ImageBlur(BaseModel):
    """
    Model of Image Blur
    """
    id_image: int
    kernel_size: int

class ImageDilate(BaseModel):
    """
    Model of Image Dilate
    """
    id_image: int
    kernel_size: int
    num_iterations : int

class ImageErosion(BaseModel):
    """
    Model of Image Dilate
    """
    id_image: int
    kernel_size: int
    num_iterations : int
    
class ImageSobelX(BaseModel):
    """
    Model of Image Dilate
    """
    id_image: int
    kernel_size: int

class ImageSobelY(BaseModel):
    """
    Model of Image Dilate
    """
    id_image: int
    kernel_size: int

class ImageSobelXY(BaseModel):
    """
    Model of Image Dilate
    """
    id_image: int
    kernel_size_X: int 
    kernel_size_Y: int

class ImageLaplacian(BaseModel):
    """
    Model of Image Dilate
    """
    id_image: int
    kernel_size: int

class ImageThinning(BaseModel):
    """
    Model of Image Dilate
    """
    id_image: int
class ImageMeasurement(BaseModel):
    """
    Model of Image Dilate
    """
    id_image: int
    min_size: int
    format_filter: str
    unit_measurement: str

class UserReset(BaseModel):
    """
    Model of User
    """
    email_user: str
    password_temp: str
    password_new: str

class UserActivate(BaseModel):
    """
    Model of User
    """
    email_user: str
    token_activate: str
