
"""
app/services/user_service.py

This module contains user-methods.
"""
import hashlib
from app.models import User
from app.repositorys.configDb import SessionLocal
from sqlalchemy.orm import Session
#from schemas import UserSchema, RequestUser
from fastapi import Depends

from app.repositorys.user_repository import user_repository

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

class UserService:
    """
    return algo,  db:Session=Depends(get_db)
    """
    def get_usuario_by_code(self, email_user: str):
        """
        return algo
        """
        #breakpoint()
        return user_repository.get_usuario_by_code( email_user)

    def autenticate_user(self, data_user: User):
        """
        return algo
        """
        return {"mensagem": f"dados do usurio para autenticação = {data_user}"}

    def post_user(self, data_user: User):
        """
        return algo
        """
        try:
            data_user.id_user = user_repository.generate_id_user()
            data_user.password_user = encript_password_user(data_user.password_user)
            return user_repository.post_user(data_user)
        except Exception as e:
            return {"Erro na encriptação da senha. tente novamente"}

    def update_password_user(self, data_user: User):
        try:
            #data_user.id_user = user_repository.generate_id_user()
            data_user.password_user = encript_password_user(data_user.password_user)
            return user_repository.update_password_user(data_user)
        except Exception as e:
            return {"Erro na atualização d senha. tente novamente"}
    
    

def encript_password_user(password: str):
    hash_object = hashlib.sha256()
    password_bytes = password.encode('utf-8')
    hash_object.update(password_bytes)
    hash_hex = hash_object.hexdigest()
    return hash_hex;

user_service = UserService()
