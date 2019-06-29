import pandas  as pd
import sys
import os
import datetime

def atualiza_lista_processados(nome_arquivo):

    todos_dados_proc  = open("processados.csv", "a")
    dados_experimento = open("Resultados/" + nome_arquivo.split(".")[0] + "-para_proc.csv", "r")

    if not(os.stat("processados.csv").st_size == 0):
        dados_experimento.readline()
    
    texto = dados_experimento.read()
    todos_dados_proc.write(texto)

    todos_dados_proc.close()
    dados_experimento.close()


def ordena_dados_processados():
    dados = pd.read_csv("processados.csv")
    dados = dados.sort_values(by=["co_cnes"], kind='mergesort')
    dados.to_csv("processados.csv", index=False)


def uniao_resultados(nome_arquivo):

    dados_experimento = open("Resultados/" + nome_arquivo.split(".")[0] + "-para_proc.csv", "a")

    try:
        dados_pre_existen = open("Resultados/" + nome_arquivo.split(".")[0] + "-ja_proc.csv", "r")
        dados_pre_existen.readline()
        texto = dados_pre_existen.read()
        dados_experimento.write(texto)
        dados_pre_existen.close()
    except FileNotFoundError:
        pass

    dados_experimento.close()

inicio = datetime.datetime.now()


nome_arquivo = str(sys.argv[1])

atualiza_lista_processados(nome_arquivo)
ordena_dados_processados()
uniao_resultados(nome_arquivo)


fim = datetime.datetime.now()
tempo = fim - inicio
print("tempo de execução: " + str(tempo))