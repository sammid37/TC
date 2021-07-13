# Projeto final, Teoria da Computação, tema 1
# Samantha Medeiros e Christopher Tavares
# 12 de julho de 2021

import re
import requests
from bs4 import BeautifulSoup
from exibir_topicos import exibir_topicos
from exibir_imagens import exibir_imagens
from exibir_links_externos import exibir_links_externos
from exibir_referencias import exibir_referencias

# Validando se a URL informada pertence ao domínio da Wikipedia
while(True):
    wikipediaURL = input("Informe a URL do artigo da Wikipedia: ")
    # wikipediaURL = "https://pt.wikipedia.org/wiki/Adventure_Time"

    # Formato aceito: qualquer url do domínio da Wikipedia que esteja em português (pt)
    formato_aceito = re.compile('(https)\:\/\/(pt)\.(wikipedia)\.(org)\/(wiki)\/(\S*)')
    url_aceita = formato_aceito.match(wikipediaURL)

    if url_aceita:
        print("Você informou um endereço válido de um artigo em português da Wikipedia.")
        break
    else:
        print("Esta URL não pertence ao domínio da Wikipedia ou o artigo não está em português. Tente novamente.")

response = requests.get(wikipediaURL) # realizando requisição para acessar a página

# Obtendo o HTTP Status Code
print("Status code:", response.status_code)

# variáveis que serão utilizadas nas buscas
conteudoWiki = response.content # tipo bytes
artigoWiki = BeautifulSoup(conteudoWiki, 'html.parser') # conversão para um objeto beautiful soup

# Exibindo o tema do artigo
assunto = artigoWiki.find('h1', {"class": re.compile("^firstHeading")})
print(f"Bem-vindo! Estamos acessando um artigo da Wikipedia sobre: {assunto.get_text()}.")

# Menu de opções
op = True
while(op):
    print("MENU")
    print("1 - exibir tópicos")
    print("2 - exibir imagens")
    print("3 - exibir links externos")
    print("4 - exibir referências")
    print("0 - sair")

    op = input("Por favor informe uma opção: ")
    print()
    
    # Chamando as funções que se encontram em arquivos externos
    if(op == "1"):
        exibir_topicos(artigoWiki)
    elif(op == "2"):
        exibir_imagens(conteudoWiki)
    elif(op == "3"):
        exibir_links_externos(conteudoWiki) 
    elif(op == "4"):
        exibir_referencias(artigoWiki)

    elif(op == "0"):
        print("Obrigado por usar o nosso programa.")
        op = False
        break
    else:
        print("Opção indisponivel ou inexistente, tente novamente.")
        print()
# fim do programa
