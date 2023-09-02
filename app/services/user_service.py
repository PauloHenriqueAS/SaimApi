
"""
app/services/user_service.py

This module contains user-methods.
"""
import hashlib
from app.models import User
from app.repositorys.user_repository import user_repository
from sqlalchemy.exc import IntegrityError

class UserService:
    """
    User Service with logic
    """
    def get_user_by_code(self, email_user: str):
        """
        Get data user by email user
        """
        return user_repository.get_user_by_code( email_user)

    def autenticate_user(self, data_user: User):
        """
        Autenticate user system
        """
        return {"mensagem": f"dados do usurio para autenticação = {data_user}"}

    def post_user(self, data_user: User):
        """
        Insert new user data
        """
        try:
            data_user.id_user = user_repository.generate_id_user()
            data_user.password_user = encript_password_user(data_user.password_user)
            return user_repository.post_user(data_user)
        except IntegrityError as error:
            return {f"Erro na encriptação da senha. tente novamente. ERRO: {error}"}

    def update_password_user(self, data_user: User):
        '''
        Update user password
        '''
        try:
            data_user.password_user = encript_password_user(data_user.password_user)
            return user_repository.update_password_user(data_user)
        except IntegrityError  as error:
            return {f"Erro na atualização de senha. tente novamente. ERRO: {error}"}
        
def encript_password_user(password: str):
    '''
    Method to encrip user password
    '''
    hash_object = hashlib.sha256()
    password_bytes = password.encode('utf-8')
    hash_object.update(password_bytes)
    hash_hex = hash_object.hexdigest()
    return hash_hex

user_service = UserService()
