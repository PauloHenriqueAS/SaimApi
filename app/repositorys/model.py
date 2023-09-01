from sqlalchemy import Column, Integer, String, func
from datetime import datetime
from app.repositorys.configDb import Base

class UserDb(Base):
    __tablename__ = 'tb_usuario'
    __table_args__ = {"schema": "saim"}

    id_user = Column(Integer, primary_key=True, index=True)
    email_user = Column(String, index=True)
    password_user = Column(String, index=True)

#UserDb = UserDb()
