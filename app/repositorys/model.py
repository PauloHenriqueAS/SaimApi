from sqlalchemy import Column, Integer, String, func
from datetime import datetime
from app.repositorys.configDb import Base

class UserDb(Base):
    __tablename__ = 'tb_usuario'
    __table_args__ = {"schema": "saim"}

    id_user = Column(Integer, primary_key=True, index=True)
    email_user = Column(String, index=True)
    password_user = Column(String, index=True)

class PersonDb(Base):
    __tablename__ = 'tb_pessoa'
    __table_args__ = {"schema": "saim"}

    id_pessoa = Column(Integer, primary_key=True, index=True)
    instituicao_pessoa = Column(String, index=True)
    uf_pessoa = Column(String, index=True)
    nome_pessoa = Column(String, index=True)
    tipo_pessoa = Column(String, index=True)
    id_user = Column(Integer, index=True)

#UserDb = UserDb()
