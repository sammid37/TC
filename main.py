# Projeto final, Teoria da Computação, tema 1
# Samantha Medeiros e Christopher Tavares
# 11 de julho de 2021

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

response = requests.get(wikipediaURL) # realizando requisição para acessar a página

# Obtendo o HTTP Status Code
print("Status code:", response.status_code)

# fazendo a conversão do objeto para fazer uma busca dentro do conteúdo HTML
conteudoWiki = response.content
artigoWiki = BeautifulSoup(conteudoWiki, 'html.parser')

# Exibindo o tema do artigo
assunto = artigoWiki.find('h1', {"class": re.compile("^firstHeading")})
print(type(assunto))
print(f"Estamos visitando uma página da Wikipedia sobre: {assunto.get_text()}")

#~ Fazendo a busca dos tópicos
# a busca irá retornar um vetor no qual cada posição armazena uma tupla
# A busca é realizada com o padrão e uma string (conteudoWiki.decode("utf-8"))
topicos = re.findall("\<(span) (class)\=\"(toctext)\"\>(.*)\<\/(span)\>",str(artigoWiki))
cont_topicos = 0

print("Os tópicos da wikipedia foram encontrados!")
# Imprimindo todas as posições do vetor onde a posição da tupla contém o tópico escrito
for i in range(len(topicos)):
    for j in range(len(topicos[i])):
        if (j == 3):
            cont_topicos += 1
            print(topicos[i][j], end=' ')
    print()
print(f"Foram encontrados {cont_topicos} itens no índice do artigo.")
print()
# #~ Fazendo a busca dos arquivos de imagem
# print("Listando os imagens do artigo: ")

# imagens_info_box = artigoWiki.find('div',attrs={'class':'floatnone'})
# print(imagens_info_box.prettify())

# # Será necessário utilizar um for para encontrar todas as imagens
# imagens_content = artigoWiki.find('div', class_='thumbinner')
# print(imagens_content.prettify())


#~ Fazendo a busca dos links externos
# Existem diversos padrões de links no corpo do artigo da wikipedia
# Alguns possuem classes, outros não, aluns redirecionam para artigos existentes(links azuis) e outros não(links vermelhos)
links1 = re.findall("\<(a) (href)\=\"\/(wiki)\/\S*\" (class)\=\"(mw-redirect)\" (title)\=\"([^\"\>\<]*)\"\>([^\"\>\<]*)\<\/(a)\>", conteudoWiki.decode("utf-8")) # class mw-redirect, href = /wiki/, title="algumacoisa"
links2 = re.findall("\<(a) (href)\=\"\/(wiki)\/\S*\" (title)\=\"\"\>([^\"\<\>]*)\<\/(a)>", conteudoWiki.decode("utf-8")) # sem classe, href=/wiki/, title=""
links3 = re.findall("\<(a) (href)\=\"\/(wiki)\/\S*\" (title)\=\"([^\"\>\<]*)\"\>([^\"\>\<]*)\<\/(a)\>", conteudoWiki.decode("utf-8")) # # sem classe, href = /wiki/, title="alguma coisa"
links4 = re.findall("\<(a) (href)\=\"\/(w)\/\S*\" (class)\=\"(new)\" (title)\=\"([^\"\>\<]*)\"\>([^\"\>\<]*)\<\/(a)\>", conteudoWiki.decode("utf-8")) # class new, href = /w/
links5 = re.findall("\<(a) (href)\=\"\/(w)\/\S*\" (class)\=\"(new)\" (title)\=\"\"\>([^\"\>\<]*)\<\/(a)\>", conteudoWiki.decode("utf-8"))

cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0

print("Exibindo os links do artigo: ")
print("LINKS 1")
for i in links1:
    cont1 += 1
    print(i)
print(f"Encontrei {cont1} links na categoria 1")
print()

print("LINKS 2")
for i in links2:
    cont2 += 1
    print(i)
print(f"Encontrei {cont2} links na categoria 2")
print()

print("LINKS 3")
for i in links3:
    cont3 += 1
    print(i)
print(f"Encontrei {cont3} links na categoria 3")
print()

print("LINKS 4")
for i in links4:
    cont4 += 1
    print(i)
print(f"Encontrei {cont4} links na categoria 4")
print()

print("LINKS 5")
for i in links5:
    cont5 += 1
    print(i)
print(f"Encontrei {cont5} links na categoria 5")
print()

# print("LINKS 1")
# for i in range(len(links1)):
#     for j in range(len(links1[i])):
#         if j == 7:
#             cont1 += 1
#             print(links1[i][j])
# print(f"Foram encontrados {cont1} links da categoria 1")
# print()
# print()
# for i in links2:
#     print(i)
# print("LINKS 2")
# for i in range (len(links2)):
#     for j in range (len(links2[i])):
#         if j == 7:
#             cont2 += 1
#             print(links2[i][j])
# print(f"Foram encontrados {cont2} links da categoria 2")
# print()
# print("LINKS 3")
# for i in range (len(links3)):
#     for j in range (len(links3[i])):
#         if j == 6:
#             cont3 += 1
#             print(links3[i][j])
# print(f"Foram encontrados {cont3} links da categoria 3")
# print()
# print("LINKS 4")
# for i in range (len(links4)):
#     for j in range (len(links4[i])):
#         if j == 5:
#             cont4 += 1
#             print(links4[i][j])
# print(f"Foram encontrados {cont4} links da categoria 4")
# print()
# print("LINKS 5")
# for i in range (len(links5)):
#     for j in range (len(links5[i])):
#         if j == 7:
#             cont5 += 1
#             print(links5[i][j])
# print(f"Foram encontrados {cont5} links da categoria 5")
# print()

