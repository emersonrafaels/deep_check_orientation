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
        numero_rotacoes         - Required : Número de rotações necessárias (Integer)
        imagem_rotacionada      - Required : Imagem após aplicação do número de rotações necessárias (PIL)

"""


from inspect import stack

import albumentations as albu
from check_orientation.pre_trained_models import create_model
import cv2
from iglovikov_helper_functions.dl.pytorch.utils import tensor_from_rgb_image
from iglovikov_helper_functions.utils.image_utils import load_rgb
import matplotlib.pyplot as plt
import numpy as np
from pylab import imshow
import torch


class check_orientation:

    def __init__(self):

        # INICIANDO O MODELO (RESNET)
        self.model = create_model("swsl_resnext50_32x4d")
        self.model.eval()

        # INICIANDO A INSTÂNCIA DE AUMENTO DE IMAGENS
        self.transform = albu.Compose([albu.Resize(height=224, width=224), albu.Normalize(p=1)], p=1)


    @staticmethod
    def realiza_leitura_imagem(caminho_imagem):

        """

            FUNÇÃO PARA LEITURA DE UMA IMAGEM.

            # Arguments
                caminho_imagem       - Required : Caminho da imagem a ser lida (String)
            # Returns
                img                  - Required : Imagem após leitura (Object)

        """

        # INICIANDO O OBJETO DA IMAGEM
        img = None

        try:
            # A LEITURA É FEITA EM FORMATO RGB
            img = load_rgb(caminho_imagem)
        except Exception as ex:
            print(ex)

        return img


    @staticmethod
    def view_image(image):

        """

            FUNÇÃO PARA VISUALIZAÇÃO DE UMA IMAGEM.
            A VISUALIZAÇÃO UTILIZA O WINDOWFRAME DO OPENCV - FUNÇÃO IMSHOW.


            # Arguments
                image                - Required : Imagem a ser visualizada (Object)
                window_name          - Required : Nome que será usada como
                                                  título da janela de exibição
                                                  da imagem (String)
            # Returns

        """

        try:
            # MOSTRANDO IMAGEM ATUAL
            imshow(image)
        except Exception as ex:
            print(ex)


    @staticmethod
    def view_image_cv2(image, window_name="IMAGEM ATUAL"):

        """

            FUNÇÃO PARA VISUALIZAÇÃO DE UMA IMAGEM.
            A VISUALIZAÇÃO UTILIZA O WINDOWFRAME DO OPENCV - FUNÇÃO IMSHOW.

            # Arguments
                image                - Required : Imagem a ser visualizada (Object)
                window_name          - Required : Nome que será usada como
                                                  título da janela de exibição
                                                  da imagem (String)
            # Returns

        """

        try:
            # MOSTRANDO IMAGEM ATUAL
            cv2.imshow(window_name, image)

            # AGUARDA A AÇÃO DO USUÁRIO DE FECHAR A JANELA DE IMAGEM
            cv2.waitKey(0)

            # DESTRUINDO A JANELA DE IMAGEM
            cv2.destroyAllWindows()
        except Exception as ex:
            print(ex)


    @staticmethod
    def view_rotations_image(image):

        try:
            for k in [0, 1, 2, 3]:
                image_rotate = np.rot90(image, k)
                check_orientation.view_image(image_rotate)
        except Exception as ex:
            print("ERRO NA FUNÇÃO: {} - {}".format(stack[0][3], ex))


    def pipeline_augmentation(self, image):

        """

            DEFININDO A PIPELINE DE AUMENTO, CRIANDO UMA INSTÂNCIA DA CLASSE COMPOSE.
            COMO ARGUMENTO PARA A COMPOSE, PASSAMOS UMA LISTA DE AUMENTOS QUE DESEJA APLICAR.
            UMA CHAMADA PARA COMPOSE, RETORNARÁ UMA FUNÇÃO DE TRANSFORMAÇÃO QUE EXECUTARÁ O AUMENTO DA IMAGEM.

            ESSA FUNÇÃO É USADA NESSA FUNÇÃO PARA APLICAÇÃO NA IMAGEM ATUAL.

            # Arguments
                image                - Required : Imagem a ser aumentada (Object)

            # Returns
                temp_albu            - Required :

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

        # INICIANDO A VARIÁVEL QUE ARMAZENARÁ AS PREDIÇÕES
        prediction = []

        # INICIANDO A VARIÁVEL QUE ARMAZENARÁ AS PREDIÇÕES FORMATADAS
        prediction_formated = []

        try:
            with torch.no_grad():
                prediction = self.model(torch.stack(images_albu)).numpy()

            for tx in prediction:
                prediction_formated.append([round(value, 2) for value in tx])
        except Exception as ex:
            print("ERRO NA FUNÇÃO: {} - {}".format(stack[0][3], ex))

        return prediction_formated


    def orchestra_predictions(self, image):

        # REALIZANDO O AUMENTO DAS IMAGENS (AUGMENTATION)
        images_albu = check_orientation.pipeline_augmentation(self, image)

        # OBTENDO AS PREDICTIONS
        predictions = check_orientation.get_predictions(self, images_albu)

        # RETORNANDO AS PREDICTIONS
        return predictions


    def orchesta_model(self, imagem):

        # REALIZANDO A LEITURA DA IMAGEM
        image = check_orientation.realiza_leitura_imagem(imagem)

        # VISUALIZANDO A IMAGEM
        # check_orientation.view_image(image)

        # VISUALIZANDO ROTAÇÕES DA IMAGEM
        # check_orientation.view_rotations_image(image)

        # OBTENDO AS PREDIÇÕES DO MODELO
        predictions = check_orientation.orchestra_predictions(self, image)

        return image, predictions


IMAGE_FILE_LOCATION = r'C:\Users\Emerson\Desktop\UFABC\Cursos\Python\OPENCV\RG\DanielCoelho.jpg'

orquestrador = check_orientation()
image, predictions_check_orientation = orquestrador.orchesta_model(IMAGE_FILE_LOCATION)

print(predictions_check_orientation)
