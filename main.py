#Programa Desenvolvido pelo Estudante Ivson Soares
#Para oBtencao de nota na "Disciplia de Construcao de Interpretadores"
#PUCPR.

                 ######### IMPORTANTE #########
## Para que o programa funcione é preciso
## os arquivos os arquivos de texto 
## estejam dentro da pasta txt e respeitem o padrão
## strings_1, strings_2, strings_3, strings_4...
from share.functions import start
import os

n_arquivos = len(os.listdir(r"MaquinaDeEstados/txt"))
listas_de_strings = [ open(f"MaquinaDeEstados/txt/strings_{x}.txt",'r').read().splitlines() for x in range(1, n_arquivos + 1, 1)]
arquivo_count = 0

for lista in listas_de_strings:
  arquivo_count = arquivo_count + 1
  print(f"\n########### ARQUIVO: {arquivo_count} ############")
  n_str = int(lista[0])
  try:
    for i in range(n_str):
      start(lista[i + 1])
      print("----------------------------------------------")
  except IndexError as e:
    print(f"Erro: {e}")
    print(f"{n_str} é maior que {i} seu último elemento")
