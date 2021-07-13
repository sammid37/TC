# Projeto final, Teoria da Computação, tema 1
# Samantha Medeiros e Christopher Tavares
# 13 de julho de 2021

import re
import requests
from bs4 import BeautifulSoup

def exibir_referencias(artigoWiki):
    print("Listando as referências do artigo.")

    # Buscando pela div de classe reflist cuja contém a lista de todas 
    # as referências utilizadas para construir o artigo
    referencias = artigoWiki.find('div',{'class':re.compile('^reflist')})
    # referencias = re.findall("\<(ol) (class)\=\"(references)\"\>(([^]*))\<\/(ol)\>",conteudoWiki.decode("utf-8"))
    # cont_referencias = 0

    # print(referencias)
    print(referencias.get_text(),end=" ")
    # print(type(referencias))

    # for i in range(len(referencias)):
    #     for j in range(len(referencias[i])):
    #         cont_referencias += 1
    #         print(f"{cont_referencias[i][j]}", end=" ")

    # print(f" {referencias.get_text()}",end=" ")
    print()
    # print(f"◉ {cont_referencias} referências encontradas.")
    print()
    print()

