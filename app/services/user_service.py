
"""
app/services/user_service.py

This module contains user-methods.
"""

from app.models import User

class UserService:
    """
    return algo
    """
    def get_usuario_by_code(self, email_user: str):
        """
        return algo
        """
        return {"mensagem": f"email do usuario {email_user}"}

    def autenticate_user(self, data_user: User):
        """
        return algo
        """
        return {"mensagem": f"dados do usurio para autenticação = {data_user}"}

    def post_user(self, data_user: User):
        """
        return algo
        """
        return {"mensagem": f"dados do usurio para inserção = {data_user}"}

    def update_password_user(self, data_user: User):
        """
        return algo
        """
        return {"mensagem": f"dados do usurio para atualização = {data_user}"}

user_service = UserService()
