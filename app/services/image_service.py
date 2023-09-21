
"""
app/services/image_service.py

This module contains image-methods.
"""

from app.models import DataFullPersonImage
from app.repositorys.image_repository import image_repository
from sqlalchemy.exc import IntegrityError

class ImageService:
    """
    return algo
    """
    def get_image_by_code(self, id_image: int):
        """
        Get image by id image
        """
        return image_repository.get_image_by_code(id_image)
    
    def get_image_by_person(self, id_pessoa: int):
        """
        Get image by id person
        """
        try:
            list_images_person = []
            list_id_images_person = []
            list_id_images_person = image_repository.get_all_images_by_person(id_pessoa)
            breakpoint()
            print(list_id_images_person)

            for item in list_id_images_person:
                data_image = image_repository.get_image_by_code(item['id_image'])
                list_images_person.append(data_image)
            
            return list_images_person
        except Exception as error:
            raise error
        
    def post_image(self, data_image: DataFullPersonImage):
        """
        Insert new data image
        """
        try:
            new_id_image = image_repository.generate_id_image()
            new_id_relation = image_repository.generate_id_relation()
            data_image.id_imagem = new_id_image
            data_image.id_img_pes = new_id_relation

            insert_image = image_repository.post_image(data_image)
            insert_relation = image_repository.post_relation_image(data_image)
            print(insert_image, insert_relation)
            if (insert_image == True) and (insert_relation == True):
                return {"code": 201, "mensagem": "Cadastro de imagem realizado com sucesso."}
        except Exception as error:
            raise error

    def update_image(self, data_image: DataFullPersonImage):
        """
        Update data image
        """
        return image_repository.update_image(data_image)

image_service = ImageService()
