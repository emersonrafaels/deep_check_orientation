"""

    FUNÇÕES PARA CONVERSÃO:
    CONVERTER IMAGEM PARA BASE64
    DECODE DA IMAGEM DE BASE64

    # Arguments

    # Returns

"""

__version__ = "2.0"
__author__ = """Patricia Catandi (CATANDI) & Oscar Bedoya (BEDOYAO) & Edson Mano (EDDANSA) &
                Lucas Menegheso (MENEFAR) & Fabio Andre Sonza (SONZAFA) & 
                Rafael Barbosa Ferreira (RBFRDTH) & Felipe Gomes Luttzolff (LUTTZOL) &
                Emerson V. Rafael (EMERVIN) & Henrique Fantinatti (HENRFAN)"""

import base64
from inspect import stack
import io

import numpy as np
from PIL import Image


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


def convert_image(imagem):

    """

        ORQUESTRA AS CONVERSÕES DE IMAGEM ENTRE FORMATOS.

        A IMAGEM ORIGINAL PODE ESTAR EM FORMATOS: BASE64, STR, ARRAY, FORMATO DE IMAGEM (PIL)

        # Arguments
            imagem                 - Required : Imagem que será convertida.
                                                A imagem pode estar em formato PIL,
                                                array, base64 ou string (PIL | Array | Base64 | String)
            nome_imagem            - Required : Nome da imagem (String)
            identificador          - Required : Identificador para log (String)

        # Returns
            img_pil                - Required : Imagem em formato PIL (PIL)

    """

    try:
        # REALIZANDO A ABERTURA DA IMAGEM
        img_pil = "null"

        if type(imagem) == bytes:

            # COMO A BASE ESTÁ EM BASE64, ELA SERÁ DECODIFICADA
            img_pil = base64_to_pil(imagem)

        elif type(imagem) == str:

            # FOI ENVIADO O CAMINHO DA IMAGEM, ELA SERÁ ABERTA COM O OPENCV

            """ 
                NA CHAMADA DO SERVIÇO, A IMAGEM EM BASE64 É CONVERTIDA PARA
                STRING E CAI NESSA PARTE DO LOOP CONDICIONAL.
                ENCODAMOS DE STRING PARA BASE64 E ABRIMOS USANDO (PIL)
                USANDO A FUNÇÃO BASE64_TO_PIL
            """

    except Exception as ex:
        print("ERRO NA FUNÇÃO: {} - {}".format(stack()[0][3], ex))









