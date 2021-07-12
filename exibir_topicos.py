# Projeto final, Teoria da Computação, tema 1
# Samantha Medeiros e Christopher Tavares
# 11 de julho de 2021
#* arquivo que contém a função para exibir tópicos

import re
import requests
from bs4 import BeautifulSoup

def exibir_topicos(artigoWiki):
    print("Irei exibir os tópicos, obrigado por me escolher")
    # a busca irá retornar um vetor no qual cada posição armazena uma tupla
    topicos = re.findall("\<(span) (class)\=\"(toctext)\"\>(.*)\<\/(span)\>",str(artigoWiki))
    numeracao = re.findall("\<(span) (class)\=\"(tocnumber)\"\>(\d|\d\.\d|\d\.\d\.\d)\<\/(span)\>", str(artigoWiki))
    cont_topicos = 0

    print("Os tópicos da wikipedia foram encontrados!")
    # Imprimindo todas as posições do vetor onde a posição da tupla contém seu respectivo tópico e numeração escrito
    for i in range(len(topicos)):
        for j in range(len(topicos[i])):
            if (j == 3):
                cont_topicos += 1
                print(f"◉ {numeracao[i][j]} {topicos[i][j]}", end=' ')
        print()
    print(f"Foram encontrados {cont_topicos} itens no índice do artigo.")
    print()