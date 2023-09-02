"""
app/Repository/user_Repository .py

This module contains user-methods.
"""

from app.models import User
from app.repositorys.model import UserDb
from .configDb import SessionLocal
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError

class UserRepository :
    """
    Repository User
    """
    def autenticate_user(self, data_user: User):
        """
        Autheticate user data
        """
        return {"mensagem": f"dados do usurio para autenticação = {data_user}"}
        
    def get_user_by_code(self, email_user: str):
        """
        Get data user by email user
        """
        try:
            db = SessionLocal()
            user = db.query(UserDb).filter(UserDb.email_user == email_user).first()
            db.close()

            if user is None:
                return {"code": 302, "mensagem": "Usuário não cadastrado"}
            else:
                return { user }
        except IntegrityError as error:
            return {"code": 404, "mensagem": f"Erro ao obter usuário. ERRO: {error}"}
        
    def post_user(self, data_user: User):
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

            return { "code": 201, "mensagem": "Usuário cadastrado com sucesso."}
        except IntegrityError as error:
            db.rollback()
            return {"code": 400, "mensagem": "Erro ao cadastrar usuário. O email já está em uso. ERRO: {error}"}
        except Exception as error:
            return {"code": 400, "mensagem": f"ERRO: {error}"}
        
    def update_password_user(self, data_user: User):
        """
        Update user password
        """
        try:
            db = SessionLocal()
            
            user_data_db = db.query(UserDb).filter(UserDb.email_user == data_user.email_user).first()
            if user_data_db:
                user_data_db.password_user = data_user.password_user

            db.commit()
            db.close()

            return { "code": 200, "mensagem": "Senha atualizada com sucesso."}
        except IntegrityError as error:
            db.rollback() 
            return {"code": 400, "mensagem": f"Erro ao atualizar usuário. ERRO: {error}"}
        except Exception as error:
            return {"code": 400, "mensagem": f"ERRO: {error}"}
        
    def generate_id_user(self):
        """
        Generate new id user to insert method
        """
        try:
            db = SessionLocal()
            max_id_user = db.query(func.max(UserDb.id_user)).scalar()
            db.close()
            if max_id_user is not None:
                return max_id_user + 1
        except Exception as error:
            return {"code": 404, "mensagem": f"Erro ao consultar id máximo. ERRO: {error}"}
                    
user_repository  = UserRepository ()
