"""

    FUNÇÕES PARA LEITURA DA IMAGEM.

    # Arguments
        object                  - Required : Imagem para leitura/visualização (String | Object)
    # Returns

"""

__version__ = "1.0"
__author__ = """Emerson V. Rafael (EMERVIN)"""
__data_atualizacao__ = "16/08/2021"


import base64
from inspect import stack
import io

import cv2
from PIL import Image

from iglovikov_helper_functions.utils.image_utils import load_rgb


def read_image_rgb(input_image):

    """

        FUNÇÃO PARA LEITURA DE UMA IMAGEM.

        # Arguments
            input_image          - Required : Caminho da imagem a ser lida (String)
        # Returns
            img                  - Required : Imagem após leitura (Array)

    """

    # INICIANDO O OBJETO DA IMAGEM
    img = None

    try:
        # A LEITURA É FEITA EM FORMATO RGB
        img = load_rgb(input_image)
    except Exception as ex:
        print("ERRO NA FUNÇÃO: {} - {}".format(stack()[0][3], ex))

    return img


def read_image(input_image):

    """

        FUNÇÃO PARA LEITURA DE UMA IMAGEM.

        # Arguments
            input_image          - Required : Caminho da imagem a ser lida (String)
        # Returns
            img                  - Required : Imagem após leitura (Object)

    """

    # INICIANDO O OBJETO DA IMAGEM
    img = None

    try:
        # UTILIZANDO O OPENCV PARA LEITURA DA IMAGEM
        # A LEITURA É FEITA EM FORMATO BGR
        img = cv2.imread(input_image)
    except Exception as ex:
        print(ex)

    return img


def read_image_pillow(input_image):

    """

        FUNÇÃO PARA LEITURA DE UMA IMAGEM.
        UTILIZA PIL - IMAGE

        # Arguments
            input_image          - Required : Caminho da imagem a ser lida (String)
        # Returns
            img                  - Required : Imagem após leitura (Object)

    """

    # INICIANDO O OBJETO DA IMAGEM
    img = None

    try:
        # UTILIZANDO O PILLOW PARA LEITURA DA IMAGEM
        # A LEITURA É FEITA EM FORMATO RGB
        img = Image.open(input_image)
    except Exception as ex:
        print("ERRO NA FUNÇÃO: {} - {}".format(stack()[0][3], ex))

    return img


def open_image_pil(imagem):

    """

        ABRE E IDENTIFICA O ARQUIVO DE IMAGEM FORNECIDO.

        ESSA FUNÇÃO TEM COMO OBJETIVO CONVERTER STR -> FORMATO DE IMAGEM (PIL)

        # Arguments
            imagem                 - Required : Imagem atual antes da formatação.
                                                Imagem no formato string (String)

        # Returns
            img_pil                - Required : Imagem convertida para formato PIL (PIL)

    """

    # INICIANDO A VARIÁVEL QUE RECEBERÁ A IMAGEM EM FORMATO PIL
    img_pil = "null"

    try:
        img_pil = Image.open(imagem)
    except Exception as ex:
        print("ERRO NA FUNÇÃO: {} - {}".format(stack()[0][3], ex))

    return img_pil


def base64_to_pil(imagem):

    """

        FUNÇÕES PARA REALIZAR O DECODE DA IMAGEM DE BASE64

        ESSA FUNÇÃO TEM COMO OBJETIVO CONVERTER BASE64 -> FORMATO DE IMAGEM (PIL)

        # Arguments
            imagem                 - Required : Imagem atual antes da formatação.
                                                Imagem no formato Base64 (Base64)

        # Returns
            img_pil                - Required : Imagem convertida para formato PIL (PIL)

    """

    # INICIANDO A VARIÁVEL QUE RECEBERÁ A IMAGEM EM FORMATO PIL
    img_pil = "null"

    try:
        img_str = io.BytesIO(base64.b64encode(imagem))
        img_pil = Image.open(img_str, mode='r')

    except Exception as ex:
        print("ERRO NA FUNÇÃO: {} - {}".format(stack()[0][3], ex))

    return img_pil


def array_to_pil(imagem):

    """

        FUNÇÕES PARA REALIZAR O ENCODE DA IMAGEM DE BASE64

        ESSA FUNÇÃO TEM COMO OBJETIVO CONVERTER ARRAY -> FORMATO DE IMAGEM (PIL)

        # Arguments
            imagem                 - Required : Imagem atual antes da formatação.
                                                Imagem no formato Array (Array)

        # Returns
            img_pil                - Required : Imagem convertida para formato PIL (PIL)


    """

    # INICIANDO A VARIÁVEL QUE RECEBERÁ A IMAGEM EM FORMATO PIL
    img_pil = "null"

    try:
        img_pil = Image.fromarray(imagem)

    except Exception as ex:
        print("ERRO NA FUNÇÃO: {} - {}".format(stack()[0][3], ex))

    return img_pil


def array_to_base64(imagem):

    """

        FUNÇÕES PARA REALIZAR O ENCODE DA IMAGEM DE BASE64

        ESSA FUNÇÃO TEM COMO OBJETIVO CONVERTER ARRAY -> BASE64

        # Arguments
            imagem                 - Required : Imagem atual antes da formatação.
                                                Imagem no formato Array (Array)

        # Returns
            img_pil                - Required : Imagem convertida para formato Base64 (Base64)


    """

    # INICIANDO A VARIÁVEL QUE RECEBERÁ A IMAGEM EM FORMATO PIL
    img_pil = "null"

    try:
        img_pil = Image.fromarray(imagem)

    except Exception as ex:
        print("ERRO NA FUNÇÃO: {} - {}".format(stack()[0][3], ex))

    return img_pil


def str_to_base64(imagem):

    """

        FUNÇÕES PARA REALIZAR O ENCODE DA IMAGEM DE BASE64

        ESSA FUNÇÃO TEM COMO OBJETIVO CONVERTER STR -> BASE64

        # Arguments
            imagem                 - Required : Imagem atual antes da formatação.
                                                Imagem no formato Array (Array)

        # Returns
            img_pil                - Required : Imagem convertida para Base64 (Base64)


    """

    # INICIANDO A VARIÁVEL QUE RECEBERÁ A IMAGEM EM FORMATO BASE64
    img_base64 = "null"

    try:
        img_base64 = imagem.encode("utf-8")

    except Exception as ex:
        print("ERRO NA FUNÇÃO: {} - {}".format(stack()[0][3], ex))

    return img_base64


def convert_image(image):

    """

        ORQUESTRA AS CONVERSÕES DE IMAGEM ENTRE FORMATOS.

        A IMAGEM ORIGINAL PODE ESTAR EM FORMATOS: BASE64, STR, ARRAY, FORMATO DE IMAGEM (PIL)

        # Arguments
            image                  - Required : Imagem que será convertida.
                                                A imagem pode estar em formato PIL,
                                                array, base64 ou string (PIL | Array | Base64 | String)
            nome_imagem            - Required : Nome da imagem (String)
            identificador          - Required : Identificador para log (String)

        # Returns
            img_pil                - Required : Imagem em formato PIL (PIL)

    """

    try:
        # REALIZANDO A ABERTURA DA IMAGEM
        img_result = "null"

        if type(image) == bytes:

            # COMO A BASE ESTÁ EM BASE64, ELA SERÁ DECODIFICADA
            img_result = base64_to_pil(image)

        elif type(image) == str:

            # FOI ENVIADO O CAMINHO DA IMAGEM, ELA SERÁ ABERTA COM O OPENCV
            img_result = read_image_rgb(image)

            """ 
                NA CHAMADA DO SERVIÇO, A IMAGEM EM BASE64 É CONVERTIDA PARA
                STRING E CAI NESSA PARTE DO LOOP CONDICIONAL.
                ENCODAMOS DE STRING PARA BASE64 E ABRIMOS USANDO (PIL)
                USANDO A FUNÇÃO BASE64_TO_PIL
            """

        else:

            img_result = image

    except Exception as ex:
        print("ERRO NA FUNÇÃO: {} - {}".format(stack()[0][3], ex))

    return img_result