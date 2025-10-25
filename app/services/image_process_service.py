"""
app/services/image_service.py

This module contains image-methods.
"""
import cv2
import numpy as np
import base64
from PIL import Image
from io import BytesIO
from sqlalchemy.exc import IntegrityError
from app.middleware import saim_api_response
from app.repositorys.image_repository import image_repository
from app.models import ImageThreshold, ImageBlur, ImageDilate, ImageErosion, ImageSobelX, ImageSobelY, ImageSobelXY, ImageLaplacian, ImageThinning

class ImageProcessingService:
    """
    return algo
    """

    async def get_image_threshold(self, dataImageThreshold: ImageThreshold):
        """
        Aplica limiarização em uma imagem Base64 com valores mínimo e máximo.
        """
        try:
            image_bytes = ''
            if dataImageThreshold.image is not None and dataImageThreshold.image != '':
                print('base64')
                image_bytes = base64.b64decode(dataImageThreshold.image)
            else:
            # Consultar o base 64 id_image
                print('whbfnio9udhbn')
                image_data = await image_repository.get_image_by_code(dataImageThreshold.id_image)
                if image_data is None:
                    return await saim_api_response.create_error_response(message="Imagem não encontrada")
                image_bytes = base64.b64decode(image_data.image)

            # Decodifica a imagem Base64 para bytes
            # image_bytes = base64.b64decode(image_data.image)
            image = Image.open(BytesIO(image_bytes)).convert("L")  # Converte para escala de cinza
            img_array = np.array(image)

            # Aplica a limiarização (Thresholding)
            _, thresh_img = cv2.threshold( img_array, dataImageThreshold.val_min, dataImageThreshold.val_max, cv2.THRESH_BINARY)
            # upper()
            # Converte a imagem processada de volta para Base64
            pil_img = Image.fromarray(thresh_img)
            buffered = BytesIO()
            # trocar para o que vier da tabela
            pil_img.save(buffered, format="PNG")
            # pil_img.save(buffered, format=image_data.extension_image.upper())

            processed_base64 = base64.b64encode( buffered.getvalue()).decode("utf-8")

            return await saim_api_response.create_response(True, processed_base64, None)
        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro na limiarização da imagem. tente novamente. ERRO: {error}")

    async def get_image_blur(self, dataImageBlur: ImageBlur):
        """
        Aplica o filtro de Média (Blur) em uma imagem Base64 com um kernel definido.
        """
        try:
            image_bytes = ''
            if dataImageBlur.image is not None and dataImageBlur.image != '':
                print('base64')
                image_bytes = base64.b64decode(dataImageBlur.image)
            else:
            # Consultar o base 64 id_image
                print('whbfnio9udhbn')
                image_data = await image_repository.get_image_by_code(dataImageBlur.id_image)
                if image_data is None:
                    return await saim_api_response.create_error_response(message="Imagem não encontrada")
                image_bytes = base64.b64decode(image_data.image)
            
            image = Image.open(BytesIO(image_bytes)).convert("RGB")  # Garante que a imagem está no formato RGB
            img_array = np.array(image)

            # Aplica o filtro de média (Blur)
            blurred_img = cv2.blur(img_array, (dataImageBlur.kernel_size, dataImageBlur.kernel_size))

            # Converte a imagem processada de volta para Base64
            pil_img = Image.fromarray(blurred_img)
            buffered = BytesIO()
            pil_img.save(buffered, format="PNG")
            processed_base64 = base64.b64encode(
            buffered.getvalue()).decode("utf-8")
            
            return await saim_api_response.create_response(True, processed_base64, None)

        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro na média da imagem. tente novamente. ERRO: {error}")

    async def get_image_dilate(self, dataImageDilate: ImageDilate):
        """
        Aplica o filtro de Média (Blur) em uma imagem Base64 com um kernel definido.
        """
        try:
            image_bytes = ''
            if dataImageDilate.image is not None and dataImageDilate.image != '':
                print('base64')
                image_bytes = base64.b64decode(dataImageDilate.image)
            else:
            # Consultar o base 64 id_image
                print('whbfnio9udhbn')
                image_data = await image_repository.get_image_by_code(dataImageDilate.id_image)
                if image_data is None:
                    return await saim_api_response.create_error_response(message="Imagem não encontrada")
                image_bytes = base64.b64decode(image_data.image)
            
            image = Image.open(BytesIO(image_bytes)).convert("RGB")  # Garante que a imagem está no formato RGB
            img_array = np.array(image)

            # Converte para escala de cinza (necessário para operações morfológicas)
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

            # Cria o kernel para dilatação
            kernel = np.ones((dataImageDilate.kernel_size, dataImageDilate.kernel_size), np.uint8)

            # Aplica a dilatação
            dilated_img = cv2.dilate(gray, kernel, iterations=dataImageDilate.num_iterations)

            # Converte a imagem processada de volta para Base64
            pil_img = Image.fromarray(dilated_img)
            buffered = BytesIO()
            pil_img.save(buffered, format="PNG")
            processed_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
            
            return await saim_api_response.create_response(True, processed_base64, None)

        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro na média da imagem. tente novamente. ERRO: {error}")

    async def get_image_erosion(self, dataImageErosion: ImageErosion):
        """
        Aplica o filtro de Média (Blur) em uma imagem Base64 com um kernel definido.
        """
        try:
            image_bytes = ''
            if dataImageErosion.image is not None and dataImageErosion.image != '':
                print('base64')
                image_bytes = base64.b64decode(dataImageErosion.image)
            else:
            # Consultar o base 64 id_image
                print('whbfnio9udhbn')
                image_data = await image_repository.get_image_by_code(dataImageErosion.id_image)
                if image_data is None:
                    return await saim_api_response.create_error_response(message="Imagem não encontrada")
                image_bytes = base64.b64decode(image_data.image)
            
            image = Image.open(BytesIO(image_bytes)).convert("RGB")  # Garante que a imagem está no formato RGB
            img_array = np.array(image)

            # Converte para escala de cinza (necessário para operações morfológicas)
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

            # Cria o kernel para erosão
            kernel = np.ones((dataImageErosion.kernel_size, dataImageErosion.kernel_size), np.uint8)

            # Aplica a erosão
            eroded_img = cv2.erode(gray, kernel, iterations=dataImageErosion.num_iterations)

            # Converte a imagem processada de volta para Base64
            pil_img = Image.fromarray(eroded_img)
            buffered = BytesIO()
            pil_img.save(buffered, format="PNG")
            processed_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
            
            return await saim_api_response.create_response(True, processed_base64, None)

        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro na média da imagem. tente novamente. ERRO: {error}")

    async def get_image_sobelX(self, dataImageSobelX: ImageSobelX):
        """
        Aplica o filtro de Média (Blur) em uma imagem Base64 com um kernel definido.
        """
        try:
            image_bytes = ''
            if dataImageSobelX.image is not None and dataImageSobelX.image != '':
                print('base64')
                image_bytes = base64.b64decode(dataImageSobelX.image)
            else:
            # Consultar o base 64 id_image
                print('whbfnio9udhbn')
                image_data = await image_repository.get_image_by_code(dataImageSobelX.id_image)
                if image_data is None:
                    return await saim_api_response.create_error_response(message="Imagem não encontrada")
                image_bytes = base64.b64decode(image_data.image)

            image = Image.open(BytesIO(image_bytes)).convert("RGB")  # Garante que a imagem está no formato RGB
            img_array = np.array(image)

            # Converte para escala de cinza (necessário para operações de borda)
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

            # Aplica o filtro Sobel X para detectar bordas verticais
            sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=dataImageSobelX.kernel_size)

            # Normaliza a imagem para converter os valores para 0-255
            sobel_x = cv2.convertScaleAbs(sobel_x)

            # Converte a imagem processada de volta para Base64
            pil_img = Image.fromarray(sobel_x)
            buffered = BytesIO()
            pil_img.save(buffered, format="PNG")
            processed_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
            
            return await saim_api_response.create_response(True, processed_base64, None)

        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro na média da imagem. tente novamente. ERRO: {error}")

    async def get_image_sobelY(self, dataImageSobelY: ImageSobelY):
        """
        Aplica o filtro de Média (Blur) em uma imagem Base64 com um kernel definido.
        """
        try:
            print('wbuoiesfrv')
            image_bytes = ''
            if dataImageSobelY.image is not None and dataImageSobelY.image != '':
                print('base64')
                image_bytes = base64.b64decode(dataImageSobelY.image)
            else:
            # Consultar o base 64 id_image
                print('whbfnio9udhbn')
                image_data = await image_repository.get_image_by_code(dataImageSobelY.id_image)
                if image_data is None:
                    return await saim_api_response.create_error_response(message="Imagem não encontrada")
                image_bytes = base64.b64decode(image_data.image)

            image = Image.open(BytesIO(image_bytes)).convert("RGB")  # Garante que a imagem está no formato RGB
            img_array = np.array(image)

            # Converte para escala de cinza (necessário para operações de borda)
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

            # Aplica o filtro Sobel Y para detectar bordas horizontais
            sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=dataImageSobelY.kernel_size)

            # Normaliza a imagem para converter os valores para 0-255
            sobel_y = cv2.convertScaleAbs(sobel_y)

            # Converte a imagem processada de volta para Base64
            pil_img = Image.fromarray(sobel_y)
            buffered = BytesIO()
            pil_img.save(buffered, format="PNG")
            processed_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
            
            return await saim_api_response.create_response(True, processed_base64, None)
        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro na média da imagem. tente novamente. ERRO: {error}")

    async def get_image_sobelXY(self, dataImageSobelXY: ImageSobelXY):
        """
        Aplica o filtro de Média (Blur) em uma imagem Base64 com um kernel definido.
        """
        try:
            image_bytes = ''
            if dataImageSobelXY.image is not None and dataImageSobelXY.image != '':
                print('base64')
                image_bytes = base64.b64decode(dataImageSobelXY.image)
            else:
            # Consultar o base 64 id_image
                print('whbfnio9udhbn')
                image_data = await image_repository.get_image_by_code(dataImageSobelXY.id_image)
                if image_data is None:
                    return await saim_api_response.create_error_response(message="Imagem não encontrada")
                image_bytes = base64.b64decode(image_data.image)

            image = Image.open(BytesIO(image_bytes)).convert("RGB")  # Garante que a imagem está no formato RGB
            img_array = np.array(image)

            # Converte para escala de cinza (necessário para operações de borda)
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

            # Aplica o filtro Sobel X (bordas verticais)
            sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=dataImageSobelXY.kernel_size_X)

            # Aplica o filtro Sobel Y (bordas horizontais)
            sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=dataImageSobelXY.kernel_size_Y)

            # Combina os gradientes de Sobel X e Y
            sobel_xy = cv2.magnitude(sobel_x, sobel_y)

            # Normaliza a imagem para converter os valores para 0-255
            sobel_xy = cv2.convertScaleAbs(sobel_xy)

            # Converte a imagem processada de volta para Base64
            pil_img = Image.fromarray(sobel_xy)
            buffered = BytesIO()
            pil_img.save(buffered, format="PNG")
            processed_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
            
            return await saim_api_response.create_response(True, processed_base64, None)
        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro na média da imagem. tente novamente. ERRO: {error}")    

    async def get_image_laplacian(self, dataImageLaplacian: ImageLaplacian):
        """
        Aplica o filtro de Média (Blur) em uma imagem Base64 com um kernel definido.
        """
        try:
            image_bytes = ''
            if dataImageLaplacian.image is not None and dataImageLaplacian.image != '':
                print('base64')
                image_bytes = base64.b64decode(dataImageLaplacian.image)
            else:
            # Consultar o base 64 id_image
                print('whbfnio9udhbn')
                image_data = await image_repository.get_image_by_code(dataImageLaplacian.id_image)
                if image_data is None:
                    return await saim_api_response.create_error_response(message="Imagem não encontrada")
                image_bytes = base64.b64decode(image_data.image)

            image = Image.open(BytesIO(image_bytes)).convert("RGB")  # Garante que a imagem está no formato RGB
            img_array = np.array(image)

            # Converte para escala de cinza (necessário para operações de borda)
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

            # Aplica o filtro Laplaciano para detecção de bordas
            laplacian = cv2.Laplacian(gray, cv2.CV_64F, ksize=dataImageLaplacian.kernel_size)

            # Normaliza a imagem para converter os valores para 0-255
            laplacian = cv2.convertScaleAbs(laplacian)

            # Converte a imagem processada de volta para Base64
            pil_img = Image.fromarray(laplacian)
            buffered = BytesIO()
            pil_img.save(buffered, format="PNG")
            processed_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
            
            return await saim_api_response.create_response(True, processed_base64, None)
        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro na média da imagem. tente novamente. ERRO: {error}") 
    
    async def get_image_thinning(self, dataImageThinning: ImageThinning):
        """
        Aplica o filtro de Média (Blur) em uma imagem Base64 com um kernel definido.
        """
        try:
            image_bytes = ''
            if dataImageThinning.image is not None and dataImageThinning.image != '':
                print('base64')
                image_bytes = base64.b64decode(dataImageThinning.image)
            else:
            # Consultar o base 64 id_image
                print('whbfnio9udhbn')
                image_data = await image_repository.get_image_by_code(dataImageThinning.id_image)
                if image_data is None:
                    return await saim_api_response.create_error_response(message="Imagem não encontrada")
                image_bytes = base64.b64decode(image_data.image)

            image_data = await image_repository.get_image_by_code(dataImageThinning.id_image)
            if image_data is None:
                return await saim_api_response.create_error_response(message="Imagem não encontrada")
            
            image = Image.open(BytesIO(image_bytes)).convert("RGB")  # Converte para RGB
            img_array = np.array(image)

            """
            Aplica afinamento (thinning) sem usar ximgproc.
            Baseado no algoritmo iterativo de Zhang-Suen.
            """
            # Converte para escala de cinza
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

            # Binariza a imagem
            _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

            # Cria um esqueleto vazio
            skeleton = np.zeros(binary.shape, np.uint8)

            # Elemento estruturante
            kernel = np.ones((3, 3), np.uint8)

            # Enquanto houver pixels a serem removidos, continua iterando
            while True:
                eroded = cv2.erode(binary, kernel)
                temp = cv2.dilate(eroded, kernel)
                temp = cv2.subtract(binary, temp)
                skeleton = cv2.bitwise_or(skeleton, temp)
                binary[:] = eroded[:]

                # Se não houver mais alterações, interrompe o loop
                if cv2.countNonZero(binary) == 0:
                    break

            # Converte a imagem processada de volta para Base64
            pil_img = Image.fromarray(skeleton)
            buffered = BytesIO()
            pil_img.save(buffered, format="PNG")
            processed_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
                
            return await saim_api_response.create_response(True, processed_base64, None)
        except IntegrityError as error:
            await saim_api_response.create_error_response(message=f"Erro na média da imagem. tente novamente. ERRO: {error}") 

    # # async def get_image_thinning(self, dataImageThinning: ImageThinning):
    #     """
    #     Aplica o filtro de Média (Blur) em uma imagem Base64 com um kernel definido.
    #     """
    #     try:

            
    #         image_data = await image_repository.get_image_by_code(dataImageThinning.id_image)
    #         if image_data is None:
    #             return await saim_api_response.create_error_response(message="Imagem não encontrada")
            
    #         image_bytes = base64.b64decode(image_data.image)
    #         image = Image.open(BytesIO(image_bytes)).convert("RGB")
    #         img_array = np.array(image)

    #         # Aplica a mensuração dos objetos
    #         measured_img, measurements = measure_object(img_array, pixel_per_unit, threshold, min_size, aspect_ratio_filter)

    #         # Converte a imagem processada de volta para Base64
    #         pil_img = Image.fromarray(measured_img)
    #         buffered = BytesIO()
    #         pil_img.save(buffered, format="PNG")
    #         processed_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
                
    #         return await saim_api_response.create_response(True, processed_base64, None)
    #     except IntegrityError as error:
    #         await saim_api_response.create_error_response(message=f"Erro na média da imagem. tente novamente. ERRO: {error}") 

    async def measure_automatic_regions(self, dataImageThreshold):
        try:
            # Obtenção da imagem
            if dataImageThreshold.image and dataImageThreshold.image != "":
                image_bytes = base64.b64decode(dataImageThreshold.image)
            else:
                image_data = await image_repository.get_image_by_code(dataImageThreshold.id_image)
                if image_data is None:
                    return await saim_api_response.create_error_response(message="Imagem não encontrada")
                image_bytes = base64.b64decode(image_data.image)

            image = Image.open(BytesIO(image_bytes)).convert("L")
            img_gray = np.array(image)

            # Limiarização automática com Otsu
            _, binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

            # Remoção de ruído
            binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))

            # Segmentação por componentes conectados
            num_labels, labels = cv2.connectedComponents(binary)

            # Inicializações
            output_img = np.zeros((labels.shape[0], labels.shape[1], 3), dtype=np.uint8)
            colors = np.random.randint(0, 255, size=(num_labels, 3), dtype=np.uint8)

            region_areas = []
            color_summary = {}

            for label in range(1, num_labels):
                mask = (labels == label)
                coords = np.argwhere(mask)
                area = coords.shape[0]

                # Coordenada central da região
                y_mean, x_mean = np.mean(coords, axis=0).astype(int)

                color_bgr = colors[label].tolist()
                hex_color = await bgr_to_hex(color_bgr)

                # Aplica cor na imagem de saída
                output_img[mask] = color_bgr

                # Atualiza regiões
                region_areas.append({
                    "label": int(label),
                    "area_pixels": int(area),
                    "center": {"x": int(x_mean), "y": int(y_mean)},
                    "color_hex": hex_color
                })

                # Agrupa estatísticas por cor
                if hex_color not in color_summary:
                    color_summary[hex_color] = {"area_total": 0, "count": 0}
                color_summary[hex_color]["area_total"] += area
                color_summary[hex_color]["count"] += 1

            # Converte imagem final para Base64
            pil_img = Image.fromarray(output_img)
            buffered = BytesIO()
            pil_img.save(buffered, format="PNG")
            img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

            dasta={
                    "image_segmented_base64": img_base64,
                    "regions": region_areas,
                    "color_stats": color_summary
                }
            print(dasta)
            return await saim_api_response.create_response(
                True,
                data={
                    "image_segmented_base64": img_base64,
                    "regions": region_areas,
                    "color_stats": color_summary
                },
                message=None
            )

        except IntegrityError as error:
            return await saim_api_response.create_error_response(
                message=f"Erro na mensuração automática. Tente novamente. ERRO: {error}"
            )
        
async def bgr_to_hex(bgr):
        return '#{:02x}{:02x}{:02x}'.format(bgr[2], bgr[1], bgr[0])

process_service = ImageProcessingService()
