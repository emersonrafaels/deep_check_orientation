from dynaconf import settings
import os

# OBTENDO O DIRETÓRIO CONTENDO O BANCO DE DADOS
DIR_MODEL_WORDS = os.path.join(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')), settings.DIR_MODEL_WORDS)