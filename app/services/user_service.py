
"""
app/services/user_service.py

This module contains user-methods.
"""
import hashlib
import random
import string
from app.models import User, UserFull, UserAuth, UserActivate, UserReset
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
            user_data_db = await user_repository.get_user_by_code(data_user.email_user)

            if user_data_db is None:
                await saim_api_response.create_error_response(message=f"Usuário não cadastrado")

            # if user_data_db.flg_activated is None or user_data_db.flg_activated is False:
            #     await saim_api_response.create_error_response(message=f"Usuário não ativado verifique seu email para realizar a ativação.")

            is_valid = await validate_password_user(user_data_db.password_user, data_user.password_user)
            if is_valid:
                data_person_db = await person_repository.get_person_by_code(user_data_db.id_user)
                personId = next(iter(data_person_db)).id_pessoa

                if data_person_db is None or personId is None or personId <= 0:
                    await saim_api_response.create_error_response(message="Informaçoes da pessoa não encontrado!")

                user_auth = UserAuth(
                    id_user=user_data_db.id_user,
                    id_pessoa=personId,
                    email_user=user_data_db.email_user,
                    password_user=user_data_db.password_user,
                    user_activated=user_data_db.flg_activated
                )
                print('dataos ', user_auth)
                return await saim_api_response.create_response(True, user_auth, 'Usuário autenticado com sucesso')
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
            data_user.password_user = await encript_password_user(data_user.password_user)
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

            breakpoint()
            if is_valid:
                data_user_full.id_user = await user_repository.generate_id_user()
                data_user_full.id_pessoa = await person_repository.generate_id_person()
                data_user_full.password_user = await encript_password_user(data_user_full.password_user)
                # data_user_full.token_reset = await encript_password_user(await generate_token())

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

    async def activate_user_access(self, data_user: UserActivate):
        try:
            # pegar o token preestabelecido no banco de dados e comparar com o que o usuario enviou e atulizar ele para ativo
            print('4Email', data_user)
            user_data_db = await user_repository.get_user_by_code(data_user.email_user)
            # personId = next(iter(user_data_db)).token_reset
            # print('teste', personId)
            print(user_data_db)
            print(dir(user_data_db))
            if user_data_db is None:
                await saim_api_response.create_error_response(message=f"Usuário não cadastrado")

            is_valid = await validate_token_user(user_data_db.token_reset, data_user.token_activate)
            # Marcar user como ativo
            if is_valid:
                new_token_reset = await encript_password_user(await generate_token())
                return await saim_api_response.create_response(True, None, await user_repository.activate_user(data_user.email_user, new_token_reset))
            else:
                return await saim_api_response.create_error_response(message=f"Erro na ativação do usuário. Token Inválido")
        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro na ativação do usuário. Tente novamente. ERRO: {error}")

    async def reset_password(self, email_reset: str):
        try:
            # pegar o token preestabelecido no banco de dados e comparar com o que o usuario enviou e atulizar ele para ativo
            user_data_db = await user_repository.get_user_by_code(email_reset)
            if user_data_db is None:
                await saim_api_response.create_error_response(message=f"Usuário não cadastrado")

            password_sys = await encript_password_user(await generate_password_reset())
            data_user = User(
                email_user=email_reset,
                password_user=password_sys
            )
            # Reseta a senha o usuario e envia por email

            return await saim_api_response.create_response(True, None, await user_repository.update_password_user(data_user))
        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro na ativação do usuário. Tente novamente. ERRO: {error}")

    async def update_user_password_reseted(self, data_reset: UserReset):
        try:
            # pegar o token preestabelecido no banco de dados e comparar com o que o usuario enviou e atulizar ele para ativo
            user_data_db = await user_repository.get_user_by_code(data_reset.email_user)
            if user_data_db is None:
                await saim_api_response.create_error_response(message=f"Usuário não cadastrado")

            is_valid = await validate_token_user(user_data_db.password_user, data_reset.password_temp)
            if is_valid:
                new_psw_encript = await encript_password_user(data_reset.password_new)

                data_user = User(
                    email_user=data_reset.email_user,
                    password_user=new_psw_encript
                )

                return await saim_api_response.create_response(True, None, await user_repository.update_password_user(data_user))
            else:
                return await saim_api_response.create_error_response(message=f"Erro na atulaização de senha do usuário. Senha temporária inválida.")
        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro na atualização do usuário. Tente novamente. ERRO: {error}")


async def encript_password_user(password: str):
    '''
    Method to encript user password
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


async def validate_token_user(token_db: str, token_request: str):
    '''
    Method to verify user password in data base and in requestuser password
    '''
    print('tokenDB', token_db)
    print('tokenRequest', token_request)
    if token_db is None or token_db == "" or token_request is None or token_request == "":
        await saim_api_response.create_error_response(message=f"Token informado inválido!")

    token_hash = await encript_password_user(token_request)
    if token_db == token_hash:
        return True
    else:
        return False


async def generate_token():
    # Letras maiúsculas, minúsculas e números
    characters = string.ascii_letters + string.digits
    new_token = ''.join(random.choices(characters, k=6))
    print(new_token)
    return new_token
    # Enviar pelo email o token de ativação


async def generate_password_reset():
    characters = string.ascii_letters + string.digits + \
        string.punctuation  # Letras maiúsculas, minúsculas e números
    new_password = ''.join(random.choices(characters, k=10))
    print('NOva senha', new_password)
    return new_password

user_service = UserService()
