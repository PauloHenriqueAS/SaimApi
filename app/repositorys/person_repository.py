
"""
app/Repository s/person_Repository .py

This module contains person-methods.
"""

from app.models import Person
from app.repositorys.model import PersonDb
from .configDb import SessionLocal
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError


class PersonRepository:
    """
    Person Repository
    """

    def get_person_by_code(self, id_user: int):
        """
        Get data person by id user
        """
        try:
            db = SessionLocal()
            person = db.query(PersonDb).filter(
                PersonDb.id_user == id_user).first()
            db.close()

            if person is None:
                return {"code": 404, "mensagem": "Nehuma pessoa encontrada."}
            else:
                return {person}
        except IntegrityError as error:
            return {"code": 400, "mensagem": f"Erro ao obter dados pessoa. ERRO: {error}"}

    def post_person(self, data_person: Person):
        """
        Insert new data person
        """
        try:
            db = SessionLocal()

            data_new_person_db = PersonDb(
                id_pessoa=data_person.id_pessoa,
                instituicao_pessoa=data_person.instituicao_pessoa,
                uf_pessoa=data_person.uf_pessoa,
                nome_pessoa=data_person.nome_pessoa,
                tipo_pessoa=data_person.tipo_pessoa,
                id_user=data_person.id_user
            )

            db.add(data_new_person_db)
            db.commit()
            db.close()

            return {"code": 201, "mensagem": "Pessoa cadastrado com sucesso.", 'data': True}
        except IntegrityError as error:
            db.rollback()
            return {"code": 400, "mensagem": "Erro ao cadastrar pessoa. ERRO: {error}", 'data': False}
        except Exception as error:
            return {"code": 400, "mensagem": f"ERRO: {error}", 'data': False}

    def update_person(self, data_person: Person):
        """
        Update user password
        """
        try:
            db = SessionLocal()

            person_data_db = db.query(PersonDb).filter(
                PersonDb.id_user == data_person.id_user).first()
            if person_data_db:
                person_data_db.instituicao_pessoa = data_person.instituicao_pessoa
                person_data_db.uf_pessoa = data_person.uf_pessoa
                person_data_db.nome_pessoa = data_person.nome_pessoa
                person_data_db.tipo_pessoa = data_person.tipo_pessoa

            db.commit()
            db.close()

            return {"code": 200, "mensagem": "Pessoa atualizada com sucesso."}
        except IntegrityError as error:
            db.rollback()
            return {"code": 400, "mensagem": f"Erro ao atualizar dados da pessoa. ERRO: {error}"}
        except Exception as error:
            return {"code": 400, "mensagem": f"ERRO: {error}"}

    def generate_id_person(self):
        """
        Generate new id user to insert method
        """
        try:
            db = SessionLocal()
            max_id_pessoa = db.query(func.max(PersonDb.id_pessoa)).scalar()
            db.close()
            if max_id_pessoa is not None:
                return max_id_pessoa + 1
        except Exception as error:
            return {"code": 404, "mensagem": f"Erro ao consultar id máximo. ERRO: {error}"}


person_repository = PersonRepository()
