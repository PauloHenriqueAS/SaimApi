
"""
app/services/person_service.py

This module contains person-methods.
"""

from app.models import Person
from app.repositorys.person_repository import person_repository
from sqlalchemy.exc import IntegrityError

class PersonService:
    """
    return await algo
    """
    async def get_person_by_code(self, id_user: int):
        """
        Get person data by code
        """
        return await person_repository.get_person_by_code(id_user)

    async def post_person(self, data_person: Person):
        """
        Insert new data person
        """
        try:
            data_person.id_pessoa = await person_repository.generate_id_person()
            return await person_repository.post_person(data_person)
        except IntegrityError  as error:
            return await {f"Erro na atualização de senha. tente novamente. ERRO: {error}"}
                
    async def update_person(self, data_person: Person):
        """
        Update data person
        """
        return await person_repository.update_person(data_person)

person_service = PersonService()
