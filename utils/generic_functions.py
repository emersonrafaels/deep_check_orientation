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

        try:
            if isinstance(valor_para_converter, int):
                return valor_para_converter
            else:
                return int(valor_para_converter)
        except Exception as ex:
            print(ex)
            return None