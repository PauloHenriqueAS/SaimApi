"""
person_controller.py

This module contains person-related routes.
"""

from fastapi import APIRouter
from app.models import Person
from app.services import person_service

router = APIRouter()

@router.get("/GetPersonByCode")
async def get_person_by_code(id_user: int):
    """
    return await data from person by id
    """
    return await person_service.get_person_by_code(id_user)

@router.post("/PostPerson")
async def post_person(data_person: Person):
    """
    Post data from a new person
    """
    return await person_service.post_person(data_person)

@router.patch("/UpdatePerson")
async def update_person(data_person: Person):
    """
    Update data person
    """
    return await person_service.update_person(data_person)
