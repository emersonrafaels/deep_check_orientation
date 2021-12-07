import os

from dynaconf import Dynaconf, settings

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['settings.yaml', '.secrets.yaml'],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load this files in the order.

# OBTENDO O DIRETÓRIO CONTENDO O BANCO DE DADOS
DIR_MODEL_WORDS = os.path.join(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')), settings.DIR_MODEL_WORDS)