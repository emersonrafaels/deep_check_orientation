"""

    FUNÇÕES PARA LEITURA DA IMAGEM.

    # Arguments
        object                  - Required : Imagem para leitura/visualização (String | Object)
    # Returns

"""

__version__ = "1.0"
__author__ = """Emerson V. Rafael (EMERVIN)"""
__data_atualizacao__ = "16/08/2021"


from inspect import stack

from iglovikov_helper_functions.utils.image_utils import load_rgb


def read_image_rgb(caminho_imagem):

    """

        FUNÇÃO PARA LEITURA DE UMA IMAGEM.

        # Arguments
            caminho_imagem       - Required : Caminho da imagem a ser lida (String)
        # Returns
            img                  - Required : Imagem após leitura (Array)

    """

    # INICIANDO O OBJETO DA IMAGEM
    img = None

    try:
        # A LEITURA É FEITA EM FORMATO RGB
        img = load_rgb(caminho_imagem)
    except Exception as ex:
        print(ex)

    return img