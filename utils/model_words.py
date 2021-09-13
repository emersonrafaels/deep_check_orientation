from os import path

from dynaconf import settings

ENTRADA = path.join(path.abspath(r".."), "model_words/por_words.txt")

# INICIANDO A LISTA QUE ARMAZENARÁ OS RESULTADOS
result_model_words = []

palavras = set()
with open(ENTRADA, encoding='latin-1') as entrada:
    for i, linha in enumerate(entrada):
        if i != 0 and linha != None:
            result_model_words.append(linha)

print(result_model_words)