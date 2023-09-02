
"""
app/services/person_service.py

This module contains person-methods.
"""

from app.models import Person
from app.repositorys.person_repository import person_repository
from sqlalchemy.exc import IntegrityError

class PersonService:
    """
    return algo
    """
    def get_person_by_code(self, id_user: int):
        """
        Get person data by code
        """
        return person_repository.get_person_by_code(id_user)

    def post_person(self, data_person: Person):
        """
        Insert new data person
        """
        try:
            data_person.id_pessoa = person_repository.generate_id_person()
            breakpoint()
            print(data_person.id_pessoa)
            return person_repository.post_person(data_person)
        except IntegrityError  as error:
            return {f"Erro na atualização de senha. tente novamente. ERRO: {error}"}
        
    def update_person(self, data_person: Person):
        """
        Update data person
        """
        return person_repository.update_person(data_person)

person_service = PersonService()
