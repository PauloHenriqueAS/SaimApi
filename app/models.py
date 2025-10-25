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
    user_activated: Optional[bool] = None

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
    id_image: Optional[int] = None
    val_min: int
    val_max: int
    image: Optional[Text] = None

class ImageBlur(BaseModel):
    """
    Model of Image Blur
    """
    id_image: Optional[int] = None
    kernel_size: int
    image: Optional[Text] = None

class ImageDilate(BaseModel):
    """
    Model of Image Dilate
    """
    id_image: Optional[int] = None
    kernel_size: int
    num_iterations : int
    image: Optional[Text] = None

class ImageErosion(BaseModel):
    """
    Model of Image Dilate
    """
    id_image: Optional[int] = None
    kernel_size: int
    num_iterations : int
    image: Optional[Text] = None
    
class ImageSobelX(BaseModel):
    """
    Model of Image Dilate
    """
    id_image: Optional[int] = None
    kernel_size: int
    image: Optional[Text] = None

class ImageSobelY(BaseModel):
    """
    Model of Image Dilate
    """
    id_image: Optional[int] = None
    kernel_size: int
    image: Optional[Text] = None

class ImageSobelXY(BaseModel):
    """
    Model of Image Dilate
    """
    id_image: Optional[int] = None
    kernel_size_X: int 
    kernel_size_Y: int
    image: Optional[Text] = None

class ImageLaplacian(BaseModel):
    """
    Model of Image Dilate
    """
    id_image: Optional[int] = None
    kernel_size: int
    image: Optional[Text] = None

class ImageThinning(BaseModel):
    """
    Model of Image Dilate
    """
    id_image: Optional[int] = None
    image: Optional[Text] = None

class ImageMensureAuto(BaseModel):
    """
    Model of Image Dilate
    """
    id_image: Optional[int] = None
    image: Optional[Text] = None

class ImageMeasurement(BaseModel):
    """
    Model of Image Dilate
    """
    id_image: Optional[int] = None
    min_size: int
    format_filter: str
    unit_measurement: str
    image: Optional[Text] = None

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
