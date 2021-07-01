# Projeto final, Teoria da Computação, tema 1
# Samantha Medeiros e Christopher Tavares
# 21 de junho de 2021
'''
Importar biblioteca do python Beautiful Soup
Requisitos do programa:
* Listar os tópicos do índice do artigo #* classes toctitle toclevel-1 tocsection-
* Listar todos os nomes de arquivos de imagens presentes no artigo #* classes thumbcaption
* Listar todas as referências bibliográficas disponíveis na página #* classes mw-references-wrap references 
* Listar todos os links para outros artigos da Wikipedia citados no conteúdo do artigo
'''
import re
import requests
from bs4 import BeautifulSoup

# Validando se a URL informada pertence ao domínio da Wikipedia
while(True):
    # wikipediaURL = input("Informe a URL do artigo da Wikipedia: ")
    wikipediaURL = "https://pt.wikipedia.org/wiki/%C3%81gata"

    # Validando a URL com Regular Expressions
    formato_aceito = re.compile('(https)\:\/\/(..)\.(wikipedia)\.(org)\/(wiki)\/(\S*)')
    url_aceita = formato_aceito.match(wikipediaURL)

    if url_aceita:
        print("Você informou um endereço válido de artigo da Wikipedia.")
        break
    else:
        print("Esta URL não pertence ao domínio da Wikipedia. Tente novamente.")

# Exibindo o assunto do artigo Wikipedia utilizando re
assunto = re.search(r'\/(wiki)\/\S*', wikipediaURL)
print(f"Estamos visitando o artigo: {assunto.group()}") 

response = requests.get(wikipediaURL)

# Obtendo o HTTP Status Code
print("Status code:", response.status_code)

# fazendo a conversão do objeto para fazer uma busca dentro do conteúdo HTML
content = response.content
artigoWiki = BeautifulSoup(content, 'html.parser')

#! Fazendo a busca dentro do HTML
#~ Fazendo a busca dos tópicos
# topicos = artigoWiki.find('div', attrs={'class':'toc'})
# print(topicos.text)

#~ Fazendo a busca dos arquivos de imagem
imagens = artigoWiki.find('div',attrs={'class':'floatnone'})
print(imagens.prettify())

#~ Fazendo a busca da referência bibliográfica
# referencias = artigoWiki.find('',attrs={'class'})

#~ Fazendo a busca dos links externos
# links_externos = artigoWiki.find('',attrs={'class'})
