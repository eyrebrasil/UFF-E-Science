# UFF-E-Science

<h3> Descrição </h3>

Este repositório possui a implementação de uma função incremental, que reconhece que dado um conjunto de dados (A U B), o conjunto A foi previamente executado, e realiza o experimento somente sobre o conjunto B, unindo ao final, os resultados de B aos de A.

<h3> Utilização </h3>

Arquivos de dados a serem processados devem ser guardados na pasta "DataSets". O experimento gera arquivos processados de mesmo nome na pasta "Resultados".

Para execução do experimento por meio do terminal, deve ser informado como parâmetro para o programa, o nome do arquivo a ser processado:
```
$ python experimento.py nomeDoArquivo.csv
```

Para execução do experimento em conjunto com a função incremental, os scripts devem ser executados da seguinte forma abaixo:
```
$ python diff.py nomeDoArquivo.csv
$ python experimento.py nomeDoArquivo-para_proc.csv
$ python incrementa.py nomeDoArquivo.csv

```
