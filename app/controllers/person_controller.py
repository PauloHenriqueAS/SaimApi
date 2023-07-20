"""
person_controller.py

This module contains person-related routes.
"""

from fastapi import APIRouter
from app.models import Person
from app.services import person_service

router = APIRouter()

@router.get("/GetPersonByCode/{id_pessoa}")
def get_person_by_code(id_pessoa: int):
    """
    Return data from person by id
    """
    return person_service.get_person_by_code(id_pessoa)

@router.post("/PostPerson")
def post_person(data_person: Person):
    """
    Post data from a new person
    """
    return person_service.post_person(data_person)

@router.patch("/UpdatePerson")
def update_person(data_person: Person):
    """
    Update data person
    """
    return person_service.update_person(data_person)
