"""
app/Repository/user_Repository .py

This module contains user-methods.
"""
from app.middleware import saim_api_response
from app.models import User, UserFull
from app.repositorys.model import PersonDb, UserDb
from .configDb import SessionLocal
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError


class UserRepository:
    """
    Repository User
    """

    async def autenticate_user(self, data_user: User):
        """
        Autheticate user data
        """
        return f"dados do usurio para autenticação = {data_user}"

    async def get_user_by_code(self, email_user: str):
        """
        Get data user by email user
        """
        try:
            db = SessionLocal()
            user = db.query(UserDb).filter(
                UserDb.email_user == email_user).first()
            db.close()

            if user is None:
                return None
            else:
                return user
        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro ao obter usuário. ERRO: {error}")

    async def post_user(self, data_user: User):
        """
        Insert new data user
        """
        try:
            db = SessionLocal()

            data_new_user_db = UserDb(
                id_user=data_user.id_user,
                email_user=data_user.email_user,
                password_user=data_user.password_user
            )

            db.add(data_new_user_db)
            db.commit()
            db.close()

            return "Usuário cadastrado com sucesso."
        except IntegrityError as error:
            db.rollback()
            await saim_api_response.create_error_response(message=f"Erro ao cadastrar usuário. O email já está em uso. ERRO: {error}")
        except Exception as error:
            await saim_api_response.create_error_response(message=f"ERRO: {error}")

    async def post_user_full(self, data_user_full: UserFull):
        """
        Insert new user data
        """
        try:
            breakpoint()
            db = SessionLocal()
            transaction = db.begin()

            print(data_user_full.id_user)
            try:
                data_user = UserDb(
                    id_user=data_user_full.id_user if data_user_full.id_user is not None else 1,
                    email_user=data_user_full.email_user,
                    password_user=data_user_full.password_user
                )
                db.add(data_user)
                db.flush()

                data_person = PersonDb(
                    id_pessoa=data_user_full.id_pessoa if data_user_full.id_pessoa is not None else 1,
                    instituicao_pessoa=data_user_full.instituicao_pessoa,
                    uf_pessoa=data_user_full.uf_pessoa,
                    nome_pessoa=data_user_full.nome_pessoa,
                    tipo_pessoa=data_user_full.tipo_pessoa,
                    id_user=data_user_full.id_user if data_user_full.id_user is not None else 1
                )
                db.add(data_person)
                db.flush()

                transaction.commit()

                return 'Cadastro realizado sucesso.'
            except Exception as error:
                transaction.rollback()
                print(f"ERRO: {error}")
                await saim_api_response.create_error_response(message=f"{error}")
            finally:
                db.close()
        except Exception as error:
            await saim_api_response.create_error_response(message=f"ERRO: {error}")

    async def update_password_user(self, data_user: User):
        """
        Update user password
        """
        try:
            db = SessionLocal()

            user_data_db = db.query(UserDb).filter(
                UserDb.email_user == data_user.email_user).first()
            if user_data_db:
                user_data_db.password_user = data_user.password_user

            db.commit()
            db.close()

            return "Senha atualizada com sucesso."
        except IntegrityError as error:
            db.rollback()
            await saim_api_response.create_error_response(message=f"Erro ao atualizar usuário. ERRO: {error}")
        except Exception as error:
            await saim_api_response.create_error_response(message=f"ERRO: {error}")

    async def generate_id_user(self):
        """
        Generate new id user to insert method
        """
        try:
            db = SessionLocal()
            max_id_user = db.query(func.max(UserDb.id_user)).scalar()
            db.close()
            
            return (max_id_user or 0) + 1
        except Exception as error:
            await saim_api_response.create_error_response(message=f"Erro ao consultar id máximo. ERRO: {error}")

user_repository = UserRepository()
