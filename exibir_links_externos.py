# Projeto final, Teoria da Computação, tema 1
# Samantha Medeiros e Christopher Tavares
# 12 de julho de 2021

import re
import requests
from bs4 import BeautifulSoup

def exibir_links_externos(conteudoWiki):
    print("Listando links do artigo:")

    # Existem diversos padrões de links no corpo do artigo da wikipedia
    # Alguns possuem classes, outros não, aluns redirecionam para artigos existentes(links azuis) e outros não(links vermelhos)
    links1 = re.findall("\<(a) (href)\=\"(\/wiki\/\S*)\" (class)\=\"(mw-redirect)\" (title)\=\"([^\"\>\<]*)\"\>([^\"\>\<]*)\<\/(a)\>", conteudoWiki.decode("utf-8")) # class mw-redirect, href = /wiki/, title="algumacoisa"
    links2 = re.findall("\<(a) (href)\=\"(\/wiki\/\S*)\" (title)\=\"([^\"\>\<]*)\"\>([^\"\>\<]*)\<\/(a)\>", conteudoWiki.decode("utf-8")) # # sem classe, href = /wiki/, title="alguma coisa"
    links3 = re.findall("\<(a) (href)\=\"(\/w\/\S*)\" (class)\=\"(new)\" (title)\=\"([^\"\<\>]*)\"\>([^\"\<\>]*)\<\/(a)\>", conteudoWiki.decode("utf-8")) # class new, href = /w/
   
    # criando listas vazias para armazenar os títulos e links de artigos externos e artigos inexistentes
    a_externos = []
    l_externos = []
    a_inexistentes = []
    l_inexistentes = []

    # artigos_externos = []
    # artigos_inexistentes = []

    cont1 = 0
    cont2 = 0
    cont3 = 0

    # Na primeira categoria o título do link é localizado na posição j == 8
    # e o seu link está localizado na posição j == 2
    for i in range(len(links1)):
        for j in range(len(links1[i])):
            # Para imprimir o título e seu respectivo link
            # print(f"{links1[i][8]}: {links1[i][2]}")
            if j == 2:
                l_externos.append(links1[i][j])
            if j == 8:
                # cont1 += 1
                a_externos.append(links1[i][j])

    # Na segunda categoria o título do link é localizado na posição j == 5
    # e o seu link está localizado na posição j == 2
    for i in range (len(links2)):
        for j in range (len(links2[i])):
            # Para imprimir o título e seu respectivo link
            # print(f"{links2[i][5]}: {links2[i][2]}")
            if j == 2:
                l_externos.append(links2[i][j])
            if j == 5:
                # cont2 += 1
                a_externos.append(links2[i][j])

    # Na terceira categoria o título do link é localizado na posição j == 6
    # e o seu link está localizado na posição j == 2
    for i in range (len(links3)):
        for j in range (len(links3[i])):
            # Para imprimir o título e seu respectivo link
            # print(f"{links3[i][6]}: {links3[i][2]}") 
            if j == 2:
                l_inexistentes.append(links3[i][j])
            if j == 6:
                # cont3 += 1
                a_inexistentes.append(links3[i][j])

    # Transformando as listas em conjuntos que permitem a impressão de valores únicos
    ae = set(a_externos)
    le = set(l_externos) 
    ai = set(a_inexistentes)
    li = set(l_inexistentes)

    # organizando em ordem alfabética :)
    sorted_ae = sorted(ae)
    sorted_le = sorted(le)
    sorted_ai = sorted(ai)
    sorted_li = sorted(li)

    # Exibindo apenas os títulos
    # print(f"Exibindo {len(ae)} títulos de artigos externos:")
    # for externo in sorted_ae:
    #     print(f"✦ {externo}")
    # print()
    # print(f"Exibindo {len(ai)} títulos de artigos inexistentes:")
    # for inexistente in sorted_ai:
    #     print(f"✧ {inexistente}")
    # print()
    # print()

    # Exibindo apenas os links
    for externo in sorted_le:
        print(f"✦ {externo}")
    print(f"◉ {len(le)} links de artigos externos encontrados.")
    print()
    for inexistente in sorted_li:
        print(f"✧ {inexistente}")
    print(f"◉ {len(li)} links de artigos inexistentes encontrados.")
    print()
    print()
