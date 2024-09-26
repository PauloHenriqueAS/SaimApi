
"""
app/services/user_service.py

This module contains user-methods.
"""
import hashlib
from app.models import User, UserFull
from sqlalchemy.exc import IntegrityError
from app.repositorys.user_repository import user_repository
from app.repositorys.person_repository import person_repository
from app.middleware import saim_api_response
from app.middleware import helper

class UserService:
    """
    User Service with logic
    """

    async def get_user_by_code(self, email_user: str):
        """
        Get data user by email user
        """
        return await saim_api_response.create_response(True, await user_repository.get_user_by_code(email_user))

    async def autenticate_user(self, data_user: User):
        """
        Autenticate user system
        """
        try:
            user_data_db = await user_repository.get_user_by_code(
                data_user.email_user)
            
            if user_data_db is None:
                await saim_api_response.create_error_response(message=f"Usuário não cadastrado")

            is_valid = await validate_password_user(
                user_data_db.password_user, data_user.password_user)
            if is_valid:
                return await saim_api_response.create_response(True, None, 'Usuário autenticado com sucesso')
            else:
                await saim_api_response.create_error_response(message="Usuário sem acesso ao sistema")
        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro na autenticação do usuário. tente novamente. ERRO: {error}")

    async def post_user(self, data_user: User):
        """
        Insert new user data
        """
        try:
            data_user.id_user = await user_repository.generate_id_user()
            data_user.password_user = await encript_password_user(
                data_user.password_user)
            return await user_repository.post_user(data_user)
        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro na encriptação da senha. tente novamente. ERRO: {error}")

    async def post_user_with_return(self, data_user: User):
        """
        Insert new user data
        """
        try:
            data_user.id_user = await user_repository.generate_id_user()
            data_user.password_user = await encript_password_user(
                data_user.password_user)
            return await saim_api_response.create_response(True, None, await user_repository.post_user_with_return(data_user))
        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro na encriptação da senha. tente novamente. ERRO: {error}")

    async def post_user_full(self, data_user_full: UserFull):
        """
        Insert new user data
        """
        try:
            is_valid = await validate_password_request(
                data_user_full.password_user, data_user_full.password_confirmation)

            if is_valid:
                data_user_full.id_user = await user_repository.generate_id_user()
                data_user_full.id_pessoa = await person_repository.generate_id_person()
                data_user_full.password_user = await encript_password_user(
                    data_user_full.password_user)

                return await saim_api_response.create_response(True, None, await user_repository.post_user_full(data_user_full))
            else:
                await saim_api_response.create_error_response(message="Senhas inválidas")
        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro na encriptação da senha. tente novamente. ERRO: {error}")

    async def update_password_user(self, data_user: User):
        '''
        Update user password
        '''
        try:
            data_user.password_user = await encript_password_user(
                data_user.password_user)
            return await saim_api_response.create_response(True, None, await user_repository.update_password_user(data_user))
        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro na atualização de senha. tente novamente. ERRO: {error}")

async def encript_password_user(password: str):
    '''
    Method to encrip user password
    '''
    salt = helper.get_salt_data()
    hash_object = hashlib.sha256()
    password_bytes = password.encode('utf-8')
    salt_bytes = salt.encode('utf-8')
    hash_object.update(salt_bytes+password_bytes)
    hash_hex = hash_object.hexdigest()
    return hash_hex


async def validate_password_user(password_db: str, password_request: str):
    '''
    Method to verify user password in data base and in requestuser password
    '''
    if password_db is None or password_db == "" or password_request is None or password_request == "":
        await saim_api_response.create_error_response(message=f"Senha inválida")
    
    password_hash_request = await encript_password_user(password_request)
    if password_db == password_hash_request:
        return True
    else:
        return False


async def validate_password_request(password_request: str, password_confirm: str):
    '''
    Method to verify user password front request to insert
    '''
    password_hash_request = await encript_password_user(password_request)
    password_hash_confirm = await encript_password_user(password_confirm)
    if password_hash_request == password_hash_confirm:
        return True
    else:
        return False


user_service = UserService()
