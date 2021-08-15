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
        numero_rotacoes         - Required : Número de rotações necessárias (Integer)
        imagem_rotacionada      - Required : Imagem após aplicação do número de rotações necessárias (PIL)

"""


from inspect import stack
import sys

from deep_check_orientation import check_orientation


if __name__ == '__main__':

    try:
        # OBTENDO O CAMINHO DA IMAGEM ENVIADA PELO USUÁRIO
        IMAGE_FILE_LOCATION = sys.argv[1]

        orquestrador = check_orientation()
        image, predictions_check_orientation = orquestrador.orchesta_model(IMAGE_FILE_LOCATION)

        print("AS PREDIÇÕES DO MODELO SÃO: {}"
              "\nPARA 0º: {}"
              "\nPARA 90º: {}"
              "\nPARA 180º: {}"
              "\nPARA 270º: {}".format(predictions_check_orientation,
                                       predictions_check_orientation[0],
                                       predictions_check_orientation[1],
                                       predictions_check_orientation[2],
                                       predictions_check_orientation[3]))


    except Exception as ex:
        print("ERRO NA FUNÇÃO: {} - {}".format(stack[0][3], ex))