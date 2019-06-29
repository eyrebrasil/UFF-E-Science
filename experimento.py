import pandas  as pd
import sys
import datetime
import time

def trata_dados (num1, num2):
    soma = int(num1) + int(num2)
    if soma < 0:
        soma = soma*(-1)
    return int(soma)

def fatorial (n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat   


inicio = datetime.datetime.now()


nome_arquivo = str(sys.argv[1])
dataset = pd.read_csv("DataSets/" + nome_arquivo, usecols=["co_cnes", "lat", "long"]) 

for indice, linha in dataset.iterrows():
    dataset.at[indice, "resultado"] = str(fatorial(trata_dados(linha["lat"], linha["long"])))

dataset = dataset.drop(["lat", "long"], axis=1)
dataset.to_csv("Resultados/" + nome_arquivo, index=False)


fim = datetime.datetime.now()
tempo = fim - inicio
tempo = tempo + (datetime.timedelta(microseconds=200000)*len(dataset.index))
print("tempo de execução: " + str(tempo))