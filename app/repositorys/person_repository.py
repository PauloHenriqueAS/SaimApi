
"""
app/Repository s/person_Repository .py

This module contains person-methods.
"""

from app.models import Person

class PersonRepository :
    """
    return algo
    """
    def get_person_by_code(self, id_pessoa: int):
        """
        return algo
        """
        return {"mensagem": f"id do usuario {id_pessoa}"}

    def post_user(self, data_person: Person):
        """
        return algo
        """
        return {"mensagem": f"dados do usurio para inserção = {data_person}"}

    def update_password_user(self, data_person: Person):
        """
        return algo
        """
        return {"mensagem": f"dados do usurio para atualização = {data_person}"}

person_repository  = PersonRepository ()
