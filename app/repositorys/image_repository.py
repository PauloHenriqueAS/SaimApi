
"""
app/Repository s/image_Repository .py

This module contains image-methods.
"""
from app.middleware import saim_api_response
import datetime
from app.models import DataFullPersonImage
from app.repositorys.model import PersonImageBD, DataImageDb
from .configDb import SessionLocal
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError

class ImageRepository :
    """
    return  algo
    """
    async def get_image_by_code(self, id_image: int):
        """
        Get Image by code
        """
        try:
            db = SessionLocal()
            image = db.query(DataImageDb).filter(DataImageDb.id_image == id_image).first()
            db.close()

            if image is None:
                await saim_api_response.create_error_response(message="Imagem não encontrada")
            else:
                return  image 
        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro ao obter imagem. ERRO: {error}")

    async def get_all_images_by_person(self, id_person: int):
        """
        Get Image by code
        """
        try:
            db = SessionLocal()
            lst_img_person = db.query(PersonImageBD).filter(PersonImageBD.id_pessoa == id_person).all()
            db.close()

            if not lst_img_person:
                return  []
            else:
                return  [{'id_image': img_pes.id_image} for img_pes in lst_img_person]
        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro ao obter imagem. ERRO: {error}")
       
    async def post_image(self, data_image: DataFullPersonImage):
        """
        Insert new data image
        """
        try:
            db = SessionLocal()

            data_new_image_db = DataImageDb(
                id_image=data_image.id_imagem,
                image=data_image.image,
                name_image=data_image.name_image,
                date_image=datetime.datetime.now()
            )

            db.add(data_new_image_db)
            db.commit()
            db.close()

            return  True 
        except IntegrityError as error:
            db.rollback()
            await saim_api_response.create_error_response(message=f"Erro ao cadastrar imagem. ERRO: {error}")
        except Exception as error:
            await saim_api_response.create_error_response(message=f"ERRO: {error}")
        
    async def post_relation_image(self, data_image: DataFullPersonImage):
        """
        Insert new relation data image-person
        """
        try:
            db = SessionLocal()

            data_new_relation_image_db = PersonImageBD(
                id_img_pes=data_image.id_img_pes,
                id_pessoa=data_image.id_pessoa,
                id_image=data_image.id_imagem
            )

            db.add(data_new_relation_image_db)
            db.commit()
            db.close()

            return  True 
        except IntegrityError as error:
            db.rollback()
            await saim_api_response.create_error_response(message=f"Erro ao cadastrar relação de imagem e pessoa. ERRO: {error}")
        except Exception as error:
            await saim_api_response.create_error_response(message=f"ERRO: {error}")
        
    async def update_image(self, data_image: DataFullPersonImage):
        """
        Update data image
        """
        try:
            db = SessionLocal()
            
            image_data_db = db.query(DataImageDb).filter(DataImageDb.id_image == data_image.id_imagem).first()
            if image_data_db:
                image_data_db.image = data_image.image

            db.commit()
            db.close()

            return  { "code": 200, "mensagem": "Imagem atualizada com sucesso."}
        except IntegrityError as error:
            db.rollback() 
            await saim_api_response.create_error_response(message=f"Erro ao atualizar imagem. ERRO: {error}")
        except Exception as error:
            await saim_api_response.create_error_response(message=f"ERRO: {error}")
        
    async def generate_id_image(self):
        """
        Generate new id image to insert method
        """
        try:
            db = SessionLocal()
            max_id_image = db.query(func.max(DataImageDb.id_image)).scalar()
            db.close()
            
            return (max_id_image or 0) + 1
        except Exception as error:
            await saim_api_response.create_error_response(message=f"Erro ao consultar id máximo. ERRO: {error}")
               
    async def generate_id_relation(self):
        """
        Generate new id user to insert method
        """
        try:
            db = SessionLocal()
            max_id_img_pes = db.query(func.max(PersonImageBD.id_img_pes)).scalar()
            db.close()
           
            return (max_id_img_pes or 0) + 1
        except Exception as error:
            await saim_api_response.create_error_response(message=f"Erro ao consultar id máximo. ERRO: {error}")
    
image_repository  = ImageRepository ()
