# Projeto final, Teoria da Computação, tema 1
# Samantha Medeiros e Christopher Tavares
# 11 de julho de 2021
#* arquivo que contém a função para exibir links externos

import re
import requests
from bs4 import BeautifulSoup

def exibir_links_externos(conteudoWiki):
    print("Vou imprimir todos os links externos")
    print("Inclusive os que não existem(vermelho)")
   
    # Existem diversos padrões de links no corpo do artigo da wikipedia
    # Alguns possuem classes, outros não, aluns redirecionam para artigos existentes(links azuis) e outros não(links vermelhos)
    # ! Se for pegar os links/urls, lembre de tirar os parênteses de wiki e w e coloque a partir da barra e após o * de S*
    # ! posição 2 para ambos tipos de links
    links1 = re.findall("\<(a) (href)\=\"(\/wiki\/\S*)\" (class)\=\"(mw-redirect)\" (title)\=\"([^\"\>\<]*)\"\>([^\"\>\<]*)\<\/(a)\>", conteudoWiki.decode("utf-8")) # class mw-redirect, href = /wiki/, title="algumacoisa"
    links2 = re.findall("\<(a) (href)\=\"(\/wiki\/\S*)\" (title)\=\"([^\"\>\<]*)\"\>([^\"\>\<]*)\<\/(a)\>", conteudoWiki.decode("utf-8")) # # sem classe, href = /wiki/, title="alguma coisa"
    links3 = re.findall("\<(a) (href)\=\"(\/w\/\S*)\" (class)\=\"(new)\" (title)\=\"([^\"\<\>]*)\"\>([^\"\<\>]*)\<\/(a)\>", conteudoWiki.decode("utf-8")) # class new, href = /w/
   
    # criando listas vazias para armazenar títulos de artigos externos e artigos inexistentes
    artigos_externos = []
    l_externos = []
    artigos_inexistentes = []
    l_inexistentes = []

    cont1 = 0
    cont2 = 0
    cont3 = 0

    print("Exibindo os títulos dos links encontrados no artigo: ")
    print("LINKS 1")
    # 0 - 8
    for i in range(len(links1)):
        for j in range(len(links1[i])):
            if j == 2:
                l_externos.append(links1[i][j])
            if j == 8:
                cont1 += 1
                artigos_externos.append(links1[i][j])
               
    if cont1 == 0:
        print("Não foi possível encontrar links que se encaixem na categoria 1.")
    else:
        print(f"Foram encontrados {cont1} links da categoria 1")
    print(cont1)

    print("LINKS 2")
    # 0 - 6
    for i in range (len(links2)):
        for j in range (len(links2[i])):
            if j == 2:
                l_externos.append(links2[i][j])
            if j == 5:
                cont2 += 1
                artigos_externos.append(links2[i][j])
    if cont2 == 0:
        print("Não foi possível encontrar links que se encaixem na categoria 2.")
    else:
        print(f"Foram encontrados {cont2} links da categoria 2")
    print(cont2)

    print("LINKS 3")
    # 0 - 8
    for i in range (len(links3)):
        for j in range (len(links3[i])):
            if j == 2:
                l_inexistentes.append(links3[i][j])
            if j == 6:
                cont3 += 1
                artigos_inexistentes.append(links3[i][j])
    if cont3 == 0:
        print("Não foi possível encontrar links que se encaixem na categoria 3.")
    else:
        print(f"Foram encontrados {cont3} links da categoria 3")
    print()
    print()

    # transformando as listas em conjuntos que permitem a impressão de valores únicos
    ae = set(artigos_externos)
    le = set(l_externos)
    ai = set(artigos_inexistentes)
    li = set(l_inexistentes)

    # organizando em ordem alfabética :)
    sorted_ae = sorted(ae)
    sorted_ai = sorted(ai)

    # Exibindo títulos, mas sem links
    print(f"Exibindo {len(ae)} títulos de artigos externos:")
    for externo in sorted_ae:
        print(f"✦ {externo}")
    print()
    print(f"Exibindo {len(ai)} títulos de artigos inexistentes:")
    for inexistente in sorted_ai:
        print(f"✧ {inexistente}")
    print()
    print()