
"""
app/services/image_service.py

This module contains image-methods.
"""

from app.models import DataFullPersonImage
from app.repositorys.image_repository import image_repository
from sqlalchemy.exc import IntegrityError
from app.middleware import saim_api_response


class ImageService:
    """
    return await algo
    """

    async def get_image_by_code(self, id_image: int):
        """
        Get image by id image
        """
        return await saim_api_response.create_response(True, await image_repository.get_image_by_code(id_image))

    async def get_image_by_person(self, id_pessoa: int):
        """
        Get image by id person
        """
        try:
            list_images_person = []
            list_id_images_person = []
            list_id_images_person = await image_repository.get_all_images_by_person(id_pessoa)

            for item in list_id_images_person:
                data_image = await image_repository.get_image_by_code(item['id_image'])
                list_images_person.append(data_image)

            return await saim_api_response.create_response(True, list_images_person)
        except Exception as error:
            await saim_api_response.create_error_response(message=f"Erro ao obter a imagem. tente novamente. ERRO: {error}")

    async def post_image(self, data_image: DataFullPersonImage):
        """
        Insert new data image
        """
        try:
            new_id_image = await image_repository.generate_id_image()
            new_id_relation = await image_repository.generate_id_relation()
            data_image.id_imagem = new_id_image
            data_image.id_img_pes = new_id_relation

            insert_image = await image_repository.post_image(data_image)
            insert_relation = await image_repository.post_relation_image(data_image)

            if (insert_image == True) and (insert_relation == True):
                return await saim_api_response.create_response(True, True, 'Cadastro de imagem realizado com sucesso.')
        except Exception as error:
            await saim_api_response.create_error_response(message=f"Erro no cadastro da imagem. tente novamente. ERRO: {error}")

    async def update_image(self, data_image: DataFullPersonImage):
        """
        Update data image
        """
        return await saim_api_response.create_response(True, await image_repository.update_image(data_image))

    async def delete_image(self, id_image: int, id_person: int):
        """
        Delete data image
        """
        print('dados recebidos', id_image, id_person)
        wasOperationSuccessful = True
        wasOperationSuccessful &= await image_repository. delete_relation_image_person(id_image, id_person)
        wasOperationSuccessful &= await image_repository.delete_image(id_image)

        return await saim_api_response.create_response(wasOperationSuccessful, None, None)

image_service = ImageService()
