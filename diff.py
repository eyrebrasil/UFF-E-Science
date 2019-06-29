import pandas  as pd
import sys
import datetime

inicio = datetime.datetime.now()


nome_arquivo = str(sys.argv[1])

dataset = pd.read_csv("DataSets/" + nome_arquivo) 
dataset = dataset.sort_values(by=["co_cnes"], kind='mergesort')

arq_proc = open("processados.csv") # arquivo base com todos os processamentos
row_proc = arq_proc.readline()

if row_proc:

  para_processar = open("DataSets/" + nome_arquivo.split(".")[0] + "-para_proc.csv", "w")
  para_processar.write("co_cnes,co_ibge,origem_dado,data_atualizacao,lat,long\n") # cria cabeçalho de arquivo com dados à processar

  ja_processado = open("Resultados/" + nome_arquivo.split(".")[0] + "-ja_proc.csv", "w")
  ja_processado.write(row_proc) # inclui cabeçalho no arquivo de dados que já foram processados

  row_proc = arq_proc.readline()

  for indice, linha in dataset.iterrows():  

    cod = linha["co_cnes"]

    if row_proc:
      cod_proc = int(row_proc.split(",")[0])

    while row_proc and (cod > cod_proc):

      row_proc = arq_proc.readline()
      if row_proc:
        cod_proc = int(row_proc.split(",")[0])

    else:
      if row_proc: 
        if cod == cod_proc:     

          ja_processado.write(row_proc)
          row_proc = arq_proc.readline()

        else: # cod < cod_proc
          para_processar.write(str(linha["co_cnes"]) +",\""+ str(linha["co_ibge"]) +"\",\""+ linha["origem_dado"] +"\",\""+ linha["data_atualizacao"] +"\",\""+ str(linha["lat"]) +"\",\""+ str(linha["long"]) +"\"\n")

      else:
        para_processar.write(str(linha["co_cnes"]) +",\""+ str(linha["co_ibge"]) +"\",\""+ linha["origem_dado"] +"\",\""+ linha["data_atualizacao"] +"\",\""+ str(linha["lat"]) +"\",\""+ str(linha["long"]) +"\"\n")


  ja_processado.close()
  para_processar.close()
  arq_proc.close()
  
else: # nada foi processado ainda

  dataset.to_csv("DataSets/" + nome_arquivo.split(".")[0] + "-para_proc.csv", index=False)
  arq_proc.close()


fim = datetime.datetime.now()
tempo = fim - inicio
print("tempo de execução: " + str(tempo))