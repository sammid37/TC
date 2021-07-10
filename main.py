# Projeto final, Teoria da Computação, tema 1
# Samantha Medeiros e Christopher Tavares
# 10 de julho de 2021

import re
import requests
from bs4 import BeautifulSoup

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

# Exibindo o assunto do artigo Wikipedia utilizando re
assunto = re.search(r'\/(wiki)\/\S*', wikipediaURL)
print(f"Estamos visitando o artigo: {assunto.group()}") 

response = requests.get(wikipediaURL)

# Obtendo o HTTP Status Code
print("Status code:", response.status_code)

# fazendo a conversão do objeto para fazer uma busca dentro do conteúdo HTML
# ! renomear content e artigoWiki(fazer relacionado ao bs4)
content = response.content
artigoWiki = BeautifulSoup(content, 'html.parser')


#~ Fazendo a busca dos tópicos
topicos = re.findall("\<(span) (class)\=\"(toctext)\"\>(\S*)\<\/(span)\>",content.decode("utf-8"))

print("Os tópicos da wikipedia foram encontrados!")
for i in range(len(topicos)):
    for j in range(len(topicos[i])):
        if (j == 3):
            print(topicos[i][j], end=' ')
    print()


# print("Listando os tópicos do artigo: ")
# div_topicos = artigoWiki.find('div', attrs={'class':'toc'})
# topicos = div_topicos.find_all('span', {'class':re.compile(r'(class)\=\"(toctext")\>(\w*)')})
# print(topicos)

# #~ Fazendo a busca dos arquivos de imagem
# print("Listando os imagens do artigo: ")

# imagens_info_box = artigoWiki.find('div',attrs={'class':'floatnone'})
# print(imagens_info_box.prettify())

# # Será necessário utilizar um for para encontrar todas as imagens
# imagens_content = artigoWiki.find('div', class_='thumbinner')
# print(imagens_content.prettify())


#~ Fazendo a busca dos links externos
# \<(a) (href)\=\"\/(wiki)\/\S*\" (class)\=\"(mw-redirect)\" (title)\=\"\S*\"\>(\S*)\<\/(a)\>
# soup.find_all('a', {'href': re.compile(r'crummy\.com/')})
links_externos = artigoWiki.find_all('a',{'href':re.compile(r'\/(wiki)\/\w*')})
print(links_externos)


#  Validando a URL com Regular Expressions
#     formato_aceito = re.compile('(https)\:\/\/(..)\.(wikipedia)\.(org)\/(wiki)\/(\S*)')
#     url_aceita = formato_aceito.match(wikipediaURL)
