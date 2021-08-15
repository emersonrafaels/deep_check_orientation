"""

    FUNÇÕES PARA VISUALIZAÇÃO DA IMAGEM.

    # Arguments
        object                  - Required : Imagem para leitura/visualização (String | Object)
    # Returns


"""


from inspect import stack

import cv2
import matplotlib.pyplot as plt
import numpy as np
from pylab import imshow


def view_image(image):

    """

        FUNÇÃO PARA VISUALIZAÇÃO DE UMA IMAGEM.
        A VISUALIZAÇÃO UTILIZA O IMSHOW DO PYLAB.


        # Arguments
            image                - Required : Imagem a ser visualizada (Object)

        # Returns

    """

    try:
        # MOSTRANDO IMAGEM ATUAL
        imshow(image)
    except Exception as ex:
        print("ERRO NA FUNÇÃO: {} - {}".format(stack[0][3], ex))


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
        print("ERRO NA FUNÇÃO: {} - {}".format(stack[0][3], ex))


def view_rotations_image(image):

    """

        FUNÇÃO PARA VISUALIZAÇÃO DE UMA IMAGEM
        ROTACIONANDO EM 0º, 90º. 180º, 270º.
        A VISUALIZAÇÃO UTILIZA A FUNÇÃO - VIEW_IMAGE

        # Arguments
            image                - Required : Imagem a ser visualizada (Object)
            window_name          - Required : Nome que será usada como
                                              título da janela de exibição
                                              da imagem (String)
        # Returns

    """

    try:
        for k in [0, 1, 2, 3]:
            image_rotate = np.rot90(image, k)
            view_image(image_rotate)
    except Exception as ex:
        print("ERRO NA FUNÇÃO: {} - {}".format(stack[0][3], ex))