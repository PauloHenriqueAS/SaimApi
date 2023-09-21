"""
app/Repositorys/model.py

This module contains database models.
"""

from sqlalchemy import Column, Integer, String, Text
from app.repositorys.configDb import Base

class UserDb(Base):
    '''
    Model User Database
    '''
    __tablename__ = 'tb_usuario'
    __table_args__ = {"schema": "saim"}

    id_user = Column(Integer, primary_key=True, index=True)
    email_user = Column(String, index=True)
    password_user = Column(String, index=True)

class PersonDb(Base):
    '''
    Model Person Database
    '''
    __tablename__ = 'tb_pessoa'
    __table_args__ = {"schema": "saim"}

    id_pessoa = Column(Integer, primary_key=True, index=True)
    instituicao_pessoa = Column(String, index=True)
    uf_pessoa = Column(String, index=True)
    nome_pessoa = Column(String, index=True)
    tipo_pessoa = Column(String, index=True)
    id_user = Column(Integer, index=True)

class DataImageDb(Base):
    '''
    Model Person Database
    '''
    __tablename__ = 'tb_imagens'
    __table_args__ = {"schema": "saim"}

    id_image = Column(Integer, primary_key=True, index=True)
    image = Column(Text, index=True)

class PersonImageBD(Base):
    '''
    Model Person Database
    '''
    __tablename__ = 'tb_rlc_img_pessoa'
    __table_args__ = {"schema": "saim"}

    id_img_pes = Column(Integer, primary_key=True, index=True)
    id_pessoa = Column(Integer, index=True)
    id_image = Column(Integer, index=True)