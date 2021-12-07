import os

from dynaconf import settings

# OBTENDO O DIRETÓRIO CONTENDO O BANCO DE DADOS
DIR_MODEL_WORDS = os.path.join(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')), settings.DIR_MODEL_WORDS)