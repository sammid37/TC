# Projeto final, Teoria da Computação, tema 1
# Samantha Medeiros e Christopher Tavares
# 11 de julho de 2021

import re
import requests
from bs4 import BeautifulSoup
from exibir_topicos import exibir_topicos
from exibir_imagens import exibir_imagens
from exibir_links_externos import exibir_links_externos

# Validando se a URL informada pertence ao domínio da Wikipedia
while(True):
    # wikipediaURL = input("Informe a URL do artigo da Wikipedia: ")
    wikipediaURL = "https://pt.wikipedia.org/wiki/Adventure_Time"

    # Validando a URL com Regular Expressions
    formato_aceito = re.compile('(https)\:\/\/(..)\.(wikipedia)\.(org)\/(wiki)\/(\S*)')
    url_aceita = formato_aceito.match(wikipediaURL)

    if url_aceita:
        print("Você informou um endereço válido de artigo da Wikipedia.")
        break
    else:
        print("Esta URL não pertence ao domínio da Wikipedia. Tente novamente.")

response = requests.get(wikipediaURL) # realizando requisição para acessar a página

# Obtendo o HTTP Status Code
print("Status code:", response.status_code)

# fazendo a conversão do objeto para fazer uma busca dentro do conteúdo HTML
conteudoWiki = response.content
artigoWiki = BeautifulSoup(conteudoWiki, 'html.parser')
# Exibindo o tema do artigo
assunto = artigoWiki.find('h1', {"class": re.compile("^firstHeading")})
print(f"Estamos visitando uma página da Wikipedia sobre: {assunto.get_text()}")

op = True
while(op):
    print("BEM-VINDO!")
    print("1 - exibir tópicos")
    print("2 - exibir imagens")
    print("3 - exibir links externos")
    print("0 - sair")
    op = input("Por favor informe uma opção: ")

    if(op == "1"):
        exibir_topicos(artigoWiki)
    elif(op == "2"):
        exibir_imagens(conteudoWiki)
    elif(op == "3"):
        exibir_links_externos(conteudoWiki)
    elif(op == "0"):
        print("Obrigado por usar o nosso programa")
        op = False
        break
    else:
        print("Opção indisponivel ou inexistente, tente novamente.")

print("Fim do programa :D")
