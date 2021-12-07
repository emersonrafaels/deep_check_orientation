"""

    FUNÇÕES PARA OBTER AS STOP WORDS.

    AS STOP WORDS SÃO USADAS PARA VERIFICAR AS PALAVRAS OBTIDAS NO OCR

    # Arguments
        dir_path_words                    - Required : Diretório contendo o
                                                       banco de dados das
                                                       stop words (String)

    # Returns
        list_words                        - Required : Lista das Stop Words (List)

"""

__version__ = "1.0"
__author__ = """Emerson V. Rafael (EMERVIN)"""
__data_atualizacao__ = "03/07/2021"

from inspect import stack
from os import getcwd, path

from dynaconf import settings

from CONFIG import config


class Model_Words():

    def __init__(self):

        """

            FUNÇÕES PARA OBTER AS STOP WORDS.

            AS STOP WORDS SÃO USADAS PARA VERIFICAR AS PALAVRAS OBTIDAS NO OCR

            # Arguments
                dir_path_words                    - Required : Diretório contendo o
                                                               banco de dados das
                                                               stop words (String)

            # Returns
                list_words                        - Required : Lista das Stop Words (List)

        """

        # 1 - DEFININDO O LOCAL CONTENDO O ARQUIVO DE STOP WORDS
        self.dir_path_words = path.join(getcwd(), settings.DIR_MODEL_WORDS)


    @staticmethod
    def close_db_words(db_words):

        """

            REALIZA O FECHAMENTO DO BANCO DE DADOS QUE CONTÉM AS STOP WORDS.


            # Arguments
                list_words                        - Required : Lista das Stop Words (List)

            # Returns
                result_format_list_words          - Required : Lista das Stop Words
                                                               após formatação(List)

        """

        try:
            db_words.close()
        except Exception as ex:
            print("ERRO NA FUNÇÃO: {} - {}".format(stack()[0][3], ex))


    @staticmethod
    def format_list_words(list_words):

        """

            REALIZA A FORMATAÇÃO DA LISTA CONTENDO AS STOP WORDS.

            É RESPONSÁVEL POR RETIRAR OS '\n'

            # Arguments
                list_words                       - Required : Lista das Stop Words (List)

            # Returns
                result_format_list_words          - Required : Lista das Stop Words
                                                               após formatação(List)

        """

        # INICIANDO A VARIÁVEL QUE RECEBERÁ O RESULTADO FORMATADO
        result_format_list_words = []

        try:
            result_format_list_words = [word.replace("\n", "") for word in list_words]
        except Exception as ex:
            print("ERRO NA FUNÇÃO: {} - {}".format(stack()[0][3], ex))

        return result_format_list_words


    def get_model_words(self):

        """

            REALIZA A ABERTURA DO BANCO DE DADOS CONTENDO AS STOP WORDS.

            AS ETAPAS SÃO:
            1) REALIZAR A ABERTURA DO BANCO DE DADOS
            2) OBTER AS STOP WORDS
            3) REALIZAR O FECHAMENTO DO BANCO DE DADOS

            # Arguments

            # Returns
                result_model_words          - Required : Lista das Stop Words (List)

        """

        # INICIANDO A LISTA QUE ARMAZENARÁ OS RESULTADOS
        result_model_words = []

        palavras = set()
        with open(config.DIR_MODEL_WORDS, encoding='utf-8') as db_words:
            for i, linha in enumerate(db_words):
                if i != 0 and linha != None:
                    result_model_words.append(linha)

        # REALIZANDO O FECHAMENTO DO DOCUMENTO
        Model_Words.close_db_words(db_words)

        # RETORNANDO O RESULTADO CONTENDO AS STOP WORDS
        return result_model_words


    def orchestra_model_words(self):

        # INICIANDO A VARIÁVEL QUE RECEBERÁ OS RESULTADOS
        list_stop_words = result_list_stop_words = []

        # OBTENDO A LISTA DE STOP WORDS
        list_stop_words = Model_Words.get_model_words(self)

        # FORMATANDO A LISTA DE STOP WORDS
        result_list_stop_words = Model_Words.format_list_words(list_stop_words)

        return result_list_stop_words