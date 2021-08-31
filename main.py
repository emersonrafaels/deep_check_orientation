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
import sys

from deep_check_orientation import check_orientation
from utils.image_view import view_image


if __name__ == '__main__':

    try:
        # OBTENDO O CAMINHO DA IMAGEM ENVIADA PELO USUÁRIO
        IMAGE_FILE_LOCATION = sys.argv[1]

        orquestrador = check_orientation()
        predictions_check_orientation, number_rotations, image_correct_orientation = orquestrador.orchesta_model(IMAGE_FILE_LOCATION)

        print("AS PREDIÇÕES DO MODELO SÃO: {}"
              "\nPARA 0º: {}"
              "\nPARA 90º: {}"
              "\nPARA 180º: {}"
              "\nPARA 270º: {}".format(predictions_check_orientation,
                                       predictions_check_orientation[0],
                                       predictions_check_orientation[1],
                                       predictions_check_orientation[2],
                                       predictions_check_orientation[3]))

        print("NÚMERO DE ROTAÇÕES NECESSÁRIAS: {} ROTAÇÕES".format(number_rotations))

        # VISUALIZANDO A IMAGEM ROTACIONADA CORRETAMENTE
        view_image(image_correct_orientation, window_name="IMAGEM ROTACIONADA")


    except Exception as ex:
        print("ERRO NA FUNÇÃO: {} - {}".format(stack()[0][3], ex))