"""

    UTILIZAÇÃO DE APRENDIZADO PROFUNDO (DEEP LEARNING) PARA VERIFICAÇÃO DA ORIENTAÇÃO DE UMA IMAGEM
    E ROTAÇÃO ADEQUADA DA MESMA. AO SER ENVIADA UMA IMAGEM (EM QUALQUER FORMATO),
    RETORNA-SE O NÚMERO DE ROTAÇÕES NECESÁRIAS E A IMAGEM ROTACIONADA CORRETAMENTE.

    OS PASSOS REALIZADOS SÃO:
    1) LEITURA DA IMAGEM EM RGB
    2) PIPELINE DE AUMENTO DE IMAGEM USANDO ALBUMENTATIONS (CLASSE: COMPOSE)
    3) REALIZAÇÃO DA PREDIÇÃO USANDO UMA REDE NEURAL DO TIPO RESNET
    4) OBTENÇÃO DAS PREDIÇÕES DE ORIENTAÇÃO DA IMAGEM
    5) CALCULO DO NÚMERO DE ROTAÇÕES NECESSÁRIAS PARA ORIENTAÇÃO CORRETA DA IMAGEM.

    # Arguments
        caminho_imagem          - Required : Imagem para verificação da orientação (String)
    # Returns
        predictions             - Required : Predições do modelo para 0º, 90º. 180º, 270º (List)
        number_rotate           - Required : Número de rotações necessárias (Integer)
        image_correct_rotate    - Required : Imagem após aplicação do número de rotações necessárias (PIL)

"""

__version__ = "1.0"
__author__ = """Emerson V. Rafael (EMERVIN)"""
__data_atualizacao__ = "16/08/2021"

from inspect import stack

import albumentations as albu
from check_orientation.pre_trained_models import create_model
from dynaconf import settings
from iglovikov_helper_functions.dl.pytorch.utils import tensor_from_rgb_image
import numpy as np
import torch

import utils.image_read as image_read_functions
import utils.image_view as image_view_functions


class check_orientation:

    """

        UTILIZAÇÃO DE APRENDIZADO PROFUNDO (DEEP LEARNING) PARA VERIFICAÇÃO DA ORIENTAÇÃO DE UMA IMAGEM
        E ROTAÇÃO ADEQUADA DA MESMA. AO SER ENVIADA UMA IMAGEM (EM QUALQUER FORMATO),
        RETORNA-SE O NÚMERO DE ROTAÇÕES NECESÁRIAS E A IMAGEM ROTACIONADA CORRETAMENTE.

        OS PASSOS REALIZADOS SÃO:
        1) LEITURA DA IMAGEM EM RGB
        2) PIPELINE DE AUMENTO DE IMAGEM USANDO ALBUMENTATIONS (CLASSE: COMPOSE)
        3) REALIZAÇÃO DA PREDIÇÃO USANDO UMA REDE NEURAL DO TIPO RESNET
        4) OBTENÇÃO DAS PREDIÇÕES DE ORIENTAÇÃO DA IMAGEM
        5) CALCULO DO NÚMERO DE ROTAÇÕES NECESSÁRIAS PARA ORIENTAÇÃO CORRETA DA IMAGEM.

        # Arguments
            caminho_imagem          - Required : Imagem para verificação da orientação (String)
        # Returns
            predictions             - Required : Predições do modelo para 0º, 90º. 180º, 270º (List)
            number_rotate           - Required : Número de rotações necessárias (Integer)
            image_correct_rotate    - Required : Imagem após aplicação do número de rotações necessárias (PIL)

    """


    def __init__(self):

        # INICIANDO O MODELO (RESNET)
        self.model = create_model(settings.MODEL_NAME)
        self.model.eval()

        # INICIANDO A INSTÂNCIA DE AUMENTO DE IMAGENS
        self.transform = albu.Compose([albu.Resize(height=settings.ALBUMENTATIONS_HEIGHT,
                                                   width=settings.ALBUMENTATIONS_WIDHT),
                                       albu.Normalize(p=settings.ALBUMENTATIONS_NORMALIZE)],
                                      p=settings.ALBUMENTATIONS_NORMALIZE)


    def pipeline_augmentation(self, image):

        """

            DEFININDO A PIPELINE DE AUMENTO, CRIANDO UMA INSTÂNCIA DA CLASSE COMPOSE.
            COMO ARGUMENTO PARA A COMPOSE, PASSAMOS UMA LISTA DE AUMENTOS QUE DESEJA APLICAR.
            UMA CHAMADA PARA COMPOSE, RETORNARÁ UMA FUNÇÃO DE TRANSFORMAÇÃO QUE EXECUTARÁ O AUMENTO DA IMAGEM.

            ESSA FUNÇÃO É USADA NESSA FUNÇÃO PARA APLICAÇÃO NA IMAGEM ATUAL.

            # Arguments
                image                - Required : Imagem para ser aumentada (Array)

            # Returns
                temp_albu            - Required : Imagens após a transformação (Array)

        """

        # INICIANDO A VARIÁVEL QUE ARMAZENARÁ OS RESULTADOS DA TRANSFORMAÇÃO DO ALBUMENTATIONS
        temp_albu = []

        try:
            # APLICANDO A TRANSFORMAÇÃO (COMPOSE) NA IMAGEM
            # A IMAGEM É ROTACIONADA EM 90º, 180º, 270º, 360º
            for k in [0, 1, 2, 3]:
                x = self.transform(image=np.rot90(image, k))["image"]
                temp_albu += [tensor_from_rgb_image(x)]
        except Exception as ex:
            print("ERRO NA FUNÇÃO: {} - {}".format(stack[0][3], ex))

        return temp_albu


    def get_predictions(self, images_albu):

        """

            FUNÇÃO RESPONSÁVEL POR UTILIZAR A REDE NEURAL PARA PREDIÇÃO DA ROTAÇÃO.

            A PREDIÇÃO É FEITA UTILIZANDO UMA SOFTMAX DE CLASSIFICAÇÃO (POSSUINDO 4 CLASSES)
            AS 4 CLASSES SÃO: 0º, 90º. 180º, 270º.

            A FUNÇÃO RETORNA QUATRO PREDIÇÕES, POIS:
            1) RECEBE A IMAGEM DA FORMA ORIGINAL - OBTÉM-SE A PREDIÇÃO NELA
            2) ROTACIONA A IMAGEM EM 90º - OBTÉM-SE A PREDIÇÃO NELA

            E O PROCESSO É REPETIDO POR 4 VEZES.

            # Arguments
                images_albu             - Required : Imagem após ser aumentada (Array)

            # Returns
                prediction_formated     - Required : Predições para a imagem rotacionada (List)

        """

        # INICIANDO A VARIÁVEL QUE ARMAZENARÁ AS PREDIÇÕES
        prediction = []

        # INICIANDO A VARIÁVEL QUE ARMAZENARÁ AS PREDIÇÕES FORMATADAS
        prediction_formated = []

        try:
            with torch.no_grad():
                prediction = self.model(torch.stack(images_albu)).numpy()

            # FORMATANDO AS PREDIÇÕES PARA FICAREM APENAS COM DUAS CASAS DECIMAIS
            # UTILIZANDO LIST COMPREHESION
            for tx in prediction:
                prediction_formated.append([round(value, 2) for value in tx])
        except Exception as ex:
            print("ERRO NA FUNÇÃO: {} - {}".format(stack[0][3], ex))

        return prediction_formated


    @staticmethod
    def get_number_rotations(predictions):

        """

            OBTÉM O NÚMERO DE ROTAÇÕES NECESSÁRIAS COM BASE NAS PREDIÇÕES.

            # Arguments
                predictions             - Required : Predições para a imagem rotacionada (List)

            # Returns
                rotations               - Required : Número de rotações necesssárias (Integer)

        """

        # INICIANDO A VARIÁVEL QUE ARMAZENARÁ O NÚMERO DE ROTAÇÕES NECESSÁRIAS
        rotations = 0

        try:
            rotations = [value[2] for idx, value in enumerate(predictions)].index(
                max([value[2] for idx, value in enumerate(predictions)])) + 2
        except Exception as ex:
            print("ERRO NA FUNÇÃO: {} - {}".format(stack[0][3], ex))

        return rotations


    @staticmethod
    def get_image_correct_orientation(image, rotations):

        """

            REALIZA A ROTAÇÃO DA IMAGEM, DE ACORDO COM O NÚMERO DE ROTAÇÕES NECESSÁRIAS.

            # Arguments
                image                  - Required : Imagem para verificação da orientação (Array)
                rotations              - Required : Número de rotações necesssárias (Integer)

            # Returns
                image                  - Required : Imagem orientada corretamente (Array)

        """

        try:
            return np.rot90(image, rotations)
        except Exception as ex:
            return image


    def orchestra_predictions(self, image):

        # REALIZANDO O AUMENTO DAS IMAGENS (AUGMENTATION)
        images_albu = check_orientation.pipeline_augmentation(self, image)

        # OBTENDO AS PREDICTIONS
        predictions = check_orientation.get_predictions(self, images_albu)

        # OBTENDO O NÚMERO DE ROTAÇÕES
        number_rotate = check_orientation.get_number_rotations(predictions)

        # ORIENTANDO A IMAGEM CORRETAMENTE
        image_correct_orientation = check_orientation.get_image_correct_orientation(image, number_rotate)

        # RETORNANDO AS PREDICTIONS, NÚMERO DE ROTAÇÕES NECESSÁRIAS
        # E IMAGEM ROTACIONADA CORRETAMENTE
        return predictions, number_rotate, image_correct_orientation


    def orchesta_model(self, imagem):

        # REALIZANDO A LEITURA DA IMAGEM
        image = image_read_functions.read_image_rgb(imagem)

        # VISUALIZANDO A IMAGEM
        image_view_functions.view_image(image, window_name="IMAGEM ORIGINAL")

        # VISUALIZANDO ROTAÇÕES DA IMAGEM
        #image_view_functions.view_rotations_image(image)

        # OBTENDO AS PREDIÇÕES DO MODELO
        predictions, number_rotate, image_correct_orientation = check_orientation.orchestra_predictions(self, image)

        return predictions, number_rotate, image_correct_orientation