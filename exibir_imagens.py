# Projeto final, Teoria da Computação, tema 1
# Samantha Medeiros e Christopher Tavares
# 11 de julho de 2021
#* arquivo que contém a função para exibir imagens

import re
import requests
from bs4 import BeautifulSoup

def exibir_imagens(conteudoWiki):
    print("Irei exibir os nomes das imagens :D") 
    # #~ Fazendo a busca dos arquivos de imagem
    print("Listando os imagens do artigo: ")

    # irá imprimir o atributo title presente no link da tag a que contem uma tag img
    # O tipo de imagem pode ser: (png|jpg|jpeg|jfif|gif|bmp|tiff|exif|raw|webp|svg)
    imagens = re.findall("\<(a) (href)\=\"\/wiki\/Ficheiro\:(\S*)\" (class)\=\"(image)\" (title)\=\"([^\"\<\>]*)\"\>\<(img) (alt)\=\"\" (src)\=\"([^\"\<\>]*\.(png|jpg|jpeg|jfif|gif|bmp|tiff|exif|raw|webp|svg))\" (.*)\<\/(a)\>", conteudoWiki.decode("utf-8")) # class mw-redirect, href = /wiki/, title="algumacoisa"
    album = []

    for i in range(len(imagens)):
        for j in range(len(imagens[i])):
            if j == 2:
                print(f"O nome do arquivo de imagem é: {imagens[i][j]}")
                album.append(imagens[i][j])