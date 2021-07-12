# Projeto final, Teoria da Computação, tema 1
# Samantha Medeiros e Christopher Tavares
# 12 de julho de 2021

import re
import requests
from bs4 import BeautifulSoup

def exibir_topicos(artigoWiki):
    print("Listando tópicos do artigo:")

    # Realizando a busca dos textos dos tópicos 
    # e sua respectiva numeração(seguindo o seguinte formato x, x.y, x.y.z)
    topicos = re.findall("\<(span) (class)\=\"(toctext)\"\>(.*)\<\/(span)\>",str(artigoWiki))
    numeracao = re.findall("\<(span) (class)\=\"(tocnumber)\"\>(\d|\d\.\d|\d\.\d\.\d)\<\/(span)\>", str(artigoWiki))
    cont_topicos = 0

    # Imprimindo todas ocorrências de tópicos e numeração,
    # ambos quando j == 3
    for i in range(len(topicos)):
        for j in range(len(topicos[i])):
            if (j == 3):
                cont_topicos += 1
                print(f"{numeracao[i][j]} {topicos[i][j]}", end=" ")
        print()
    print(f"◉ {cont_topicos} tópicos encontrados.")
    print()
    print()
