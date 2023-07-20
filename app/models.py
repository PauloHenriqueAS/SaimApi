"""
models.py

This module contains all models that are being used in api.
"""

from typing import Optional
from pydantic import BaseModel

class Person(BaseModel):
    """
    Model of Person
    """
    id_pessoa: int
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

class ImageBD(BaseModel):
    """
    Model of Image
    """
    id_image: Optional[int] = None
    image: str

class PersonImageBD(BaseModel):
    """
    Model of Relation Image and Person
    """
    id_img_pes: Optional[int] = None
    id_pessoa: int
    id_imagem: int

class DataFullPersonImageBD(BaseModel):
    """
    Model of full data from relation Image and Person
    """
    id_img_pes: Optional[int] = None
    id_pessoa: int
    id_imagem: int
    image: str
