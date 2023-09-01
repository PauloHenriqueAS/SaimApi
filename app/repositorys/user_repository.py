
"""
app/Repository s/user_Repository .py

This module contains user-methods.
"""

from app.repositorys.configDb import engine
from app.models import User
from app.repositorys.model import UserDb
from .configDb import SessionLocal
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
#from app.repositorys.schemas import UserSchema



class UserRepository :
    """
    return algo
    """
    def autenticate_user(self, data_user: User):
        """
        return algo
        """
        return {"mensagem": f"dados do usurio para autenticação = {data_user}"}

    def get_usuario_by_code(self, email_user: str):
        """
        return algo
        """
        try:
            db = SessionLocal()
            user  =  db.query(UserDb).filter(UserDb.email_user == email_user).first()
            db.close()

            if user is None:
                return {"mensagem": "Usuário não cadastrado"}
            else:
                return { user }
        except Exception as e:
            return {"mensagem": f"Erro ao obter usuário. ERRO: {str(e)}"}

    def post_user(self, data_user: User):
        """
        return algo
        """
        try: 
            db = SessionLocal()

            data_new_user_db = UserDb(
                id_user=data_user.id_user,
                email_user=data_user.email_user,
                password_user=data_user.password_user
            )
            breakpoint()
            print(str(data_new_user_db.password_user))
            print(str(data_user.id_user))

            db.add(data_new_user_db)
            db.commit()
            db.close()
        except IntegrityError as e:
            db.rollback()  # Desfaz a transação em caso de erro
            return {"mensagem": "Erro ao cadastrar usuário. O email já está em uso. ERRO: {e}"}
        except Exception as e:
            return {"mensagem": f"ERRO: {e}"}

    def update_password_user(self, data_user: User):
        """
        return algo
        """
        try: 
            db = SessionLocal()

            user_data_db = db.query(UserDb).filter(UserDb.email_user == data_user.email_user).first()
            if user_data_db:
                user_data_db.password_user = data_user.password_user
            db.commit()
            db.close()
        except IntegrityError as e:
            db.rollback()  # Desfaz a transação em caso de erro
            return {"mensagem": "Erro ao atualizar usuário. ERRO: {e}"}
        except Exception as e:
            return {"mensagem": f"ERRO: {e}"}

    def generate_id_user(self):
        """
        return algo
        """
        try: 
            db = SessionLocal()
            max_id_user = db.query(func.max(UserDb.id_user)).scalar()
            db.close()
            if max_id_user is not None:
                return max_id_user + 1
        except Exception as e:
            return {"mensagem": f"Erro ao consultar id máximo. ERRO: {e}"}
        
        
user_repository  = UserRepository ()
