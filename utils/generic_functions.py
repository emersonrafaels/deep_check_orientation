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
    def convert_list_lower_case(lista_atual):

        """

            CONVERTE TODOS OS ELEMENTOS DE UMA LISTA EM LOWER CASE

            # Arguments
                lista_atual                - Required : Lista que terão os elementos convertidos (List)

            # Returns
                lista_lower                - Required : Lista após conversão (List)

        """

        try:
            # CONVERTENDO TODOS OS ELEMENTOS DA LISTA PARA LOWER CASE
            lista_lower = [x.lower() for x in lista_atual]

            return lista_lower

        except Exception as ex:
            print(ex)

            return lista_atual



    @staticmethod
    def remove_list_value_none(list_remove_none):

        """

            RETIRA TODOS OS ELEMENTOS QUE SÃO NONE OU "" DE UMA LISTA.

            # Arguments
                list_remove_none               - Required : Lista que será analisada (List)

            # Returns
                result_list_remove_none        - Required : Resultado da análise da função(List)

        """

        # INICIANDO A LISTA DE RESULTADO DA INTERSECÇÃO
        result_list_remove_none = []

        try:
            result_list_remove_none = [value for value in list_remove_none.split(" ") if value is not "" and  value is not None]
        except Exception as ex:
            print(ex)

        return result_list_remove_none


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