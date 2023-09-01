from sqlalchemy.orm import mapper
# from .model import UserDb
# from models import User
# ... (outras importações)

def map_user_to_userdb():
    """
    Mapeia a classe User para a classe UserDb.
    """
    mapper(
        UserDb,
        User,
        properties={
            "id_user": User.id_user,
            "email_user": User.email_user,
            "password_user": User.password_user
        }
    )

map_user_to_userdb  = map_user_to_userdb()