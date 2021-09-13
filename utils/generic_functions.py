"""

    FUNÇÕES GENÉRICAS UTILIZANDO PYTHON.

    # Arguments

    # Returns


"""

__version__ = "1.0"
__author__ = """Emerson V. Rafael (EMERVIN)"""
__data_atualizacao__ = "04/07/2021"


class generic_functions():

    @staticmethod
    def converte_int(valor_para_converter):

        """

            FUNÇÃO GENÉRICA PARA CONVERTER UM VALOR PARA FORMATO INTEIRO.


            # Arguments
                valor_para_converter              - Required : Valor para converter (Object)

            # Returns
                valor_para_converter              - Required : Valor após conversão (Integer)

        """

        try:
            if isinstance(valor_para_converter, int):
                return valor_para_converter
            else:
                return int(valor_para_converter)
        except Exception as ex:
            print(ex)
            return None


    @staticmethod
    def get_list_intersecction(list1, list2):

        """

            OBTÉM A INTERCÇÃO ENTRE DUAS LISTAS

            # Arguments
                list1                       - Required : Lista de dados 1 (List)
                list2                       - Required : Lista de dados 2 (List)

            # Returns
                result_intersecction        - Required : Lista com os dados interseccionados (List)

        """

        # INICIANDO A LISTA DE RESULTADO DA INTERSECÇÃO
        result_intersecction = []

        try:
            result_intersecction = list(set(list1).intersection(set(list2)))
        except Exception as ex:
            print(ex)

        return result_intersecction