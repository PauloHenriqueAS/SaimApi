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
    id_pessoa: int
    image: Text
