
"""
app/Repository s/image_Repository .py

This module contains image-methods.
"""

from app.models import DataFullPersonImageBD

class ImageRepository :
    """
    return algo
    """
    def get_image_by_code(self, id_pessoa: int):
        """
        return algo
        """
        return {"mensagem": f"id do usuario {id_pessoa}"}

    def post_image(self, data_image: DataFullPersonImageBD):
        """
        return algo
        """
        return {"mensagem": f"dados do usurio para inserção = {data_image}"}

    def update_image(self, data_image: DataFullPersonImageBD):
        """
        return algo
        """
        return {"mensagem": f"dados do usurio para atualização = {data_image}"}

image_repository  = ImageRepository ()
