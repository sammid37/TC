# Projeto final, Teoria da Computação, tema 1
# Samantha Medeiros e Christopher Tavares
# 12 de julho de 2021

import re
import requests
from bs4 import BeautifulSoup

def exibir_imagens(conteudoWiki):
    print("Listando os arquivos de imagem do artigo: ")

    # Realizando a busca dos arquivos de imagem
    # Buscando imagens nos formatos: png, jpg, jpeg e webp
    imagens1 = re.findall("\<(a) (href)\=\"\/wiki\/Ficheiro\:(\S*)\" (class)\=\"(image)\" (title)\=\"([^\"\<\>]*)\"\>\<(img) (alt)\=\"([^\"\<\>]*)\" (src)\=\"([^\"\<\>]*\.(png|jpg|jpeg|webp))\" (.*)\<\/(a)\>", conteudoWiki.decode("utf-8")) # class mw-redirect, href = /wiki/, title="algumacoisa"
    imagens2 = re.findall("\<(a) (href)\=\"\/wiki\/Ficheiro\:(\S*)\" (class)\=\"(image)\"\>\<(img) (alt)\=\"([^\"\<\>]*)\" (src)\=\"([^\"\<\>]*\.(png|jpg|jpeg|webp))\" (.*)\<\/(a)\>", conteudoWiki.decode("utf-8")) # class mw-redirect, href = /wiki/, title="algumacoisa"

    album = [] # lista vazia que vai armazenar todas as ocorrências de imagens

    # Armazenando na lista album o nome do arquivo de imagem, encontrado quando j == 2
    for i in range(len(imagens1)):
        for j in range(len(imagens1[i])):
            if j == 2:
                # print(f"O nome do arquivo de imagem é: {imagens[i][j]}")
                album.append(imagens1[i][j])

    # Armazenando na lista album o nome do arquivo de imagem, encontrado quando j == 2
    for i in range(len(imagens2)):
        for j in range(len(imagens2[i])):
            if j == 2:
                # print(f"O nome do arquivo de imagem é: {imagens2[i][j]}")
                album.append(imagens2[i][j])
    
    # Transformando a lista em um conjunto
    album = set(album)

    # Imprimindo o conjunto album que contém todas as imagens encontradas
    for i in album:
        print(f"• {i}")
    print(f"◉ {len(album)} arquivos de imagem encontrados.")
    print()
    print()
