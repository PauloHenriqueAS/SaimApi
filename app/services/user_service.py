
"""
app/services/user_service.py

This module contains user-methods.
"""
import hashlib
from app.models import User, UserFull
from sqlalchemy.exc import IntegrityError
from app.repositorys.user_repository import user_repository
from app.repositorys.person_repository import person_repository


class UserService:
    """
    User Service with logic
    """

    def get_user_by_code(self, email_user: str):
        """
        Get data user by email user
        """
        return user_repository.get_user_by_code(email_user)

    def autenticate_user(self, data_user: User):
        """
        Autenticate user system
        """
        try:
            user_data_db = user_repository.get_user_by_code(
                data_user.email_user)
            is_valid = validate_password_user(
                user_data_db.password_user, data_user.password_user)
            if is_valid:
                return {'mensagem': 'Usuário autenticado com sucesso', 'data': True}
            else:
                return {'mensagem': 'Usuário sem acesso ao sistema', 'data': False}
        except IntegrityError as error:
            return {f"Erro na autenticação do usuário. tente novamente. ERRO: {error}"}

    def post_user(self, data_user: User):
        """
        Insert new user data
        """
        try:
            data_user.id_user = user_repository.generate_id_user()
            data_user.password_user = encript_password_user(
                data_user.password_user)
            return user_repository.post_user(data_user)
        except IntegrityError as error:
            return {f"Erro na encriptação da senha. tente novamente. ERRO: {error}"}

    def post_user_with_return(self, data_user: User):
        """
        Insert new user data
        """
        try:
            data_user.id_user = user_repository.generate_id_user()
            data_user.password_user = encript_password_user(
                data_user.password_user)
            return user_repository.post_user_with_return(data_user)
        except IntegrityError as error:
            return {f"Erro na encriptação da senha. tente novamente. ERRO: {error}"}

    def post_user_full(self, data_user_full: UserFull):
        """
        Insert new user data
        """
        try:
            is_valid = validate_password_request(
                data_user_full.password_user, data_user_full.password_confirmation)

            if is_valid:
                data_user_full.id_user = user_repository.generate_id_user()
                data_user_full.id_pessoa = person_repository.generate_id_person()
                data_user_full.password_user = encript_password_user(
                    data_user_full.password_user)

                return user_repository.post_user_full(data_user_full)
            else:
                return {'mensagem': 'Senhas inválidas', 'data': False}
        except IntegrityError as error:
            return {'mensagem': f"Erro na encriptação da senha. tente novamente. ERRO: {error}", 'data': False}

    def update_password_user(self, data_user: User):
        '''
        Update user password
        '''
        try:
            data_user.password_user = encript_password_user(
                data_user.password_user)
            return user_repository.update_password_user(data_user)
        except IntegrityError as error:
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


def validate_password_user(password_db: str, password_request: str):
    '''
    Method to verify user password in data base and in requestuser password
    '''
    password_hash_request = encript_password_user(password_request)
    if password_db == password_hash_request:
        return True
    else:
        return False


def validate_password_request(password_request: str, password_confirm: str):
    '''
    Method to verify user password front request to insert
    '''
    password_hash_request = encript_password_user(password_request)
    password_hash_confirm = encript_password_user(password_confirm)
    if password_hash_request == password_hash_confirm:
        return True
    else:
        return False


user_service = UserService()
