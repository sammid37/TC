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


#~ Fazendo a busca dos links externos
# Existem diversos padrões de links no corpo do artigo da wikipedia
# Alguns possuem classes, outros não, aluns redirecionam para artigos existentes(links azuis) e outros não(links vermelhos)
links1 = re.findall("\<(a) (href)\=\"\/(wiki)\/\S*\" (class)\=\"(mw-redirect)\" (title)\=\"([^\"\>\<]*)\"\>([^\"\>\<]*)\<\/(a)\>", conteudoWiki.decode("utf-8")) # class mw-redirect, href = /wiki/, title="algumacoisa"
# links2 = re.findall("\<(a) (href)\=\"\/(wiki)\/\S*\" (title)\=\"\"\>([^\"\<\>]*)\<\/(a)>", conteudoWiki.decode("utf-8")) # sem classe, href=/wiki/, title=""
links3 = re.findall("\<(a) (href)\=\"\/(wiki)\/\S*\" (title)\=\"([^\"\>\<]*)\"\>([^\"\>\<]*)\<\/(a)\>", conteudoWiki.decode("utf-8")) # # sem classe, href = /wiki/, title="alguma coisa"
links4 = re.findall("\<(a) (href)\=\"\/(w)\/\S*\" (class)\=\"(new)\" (title)\=\"([^\"\<\>]*)\"\>([^\"\<\>]*)\<\/(a)\>", conteudoWiki.decode("utf-8")) # class new, href = /w/
# links5 = re.findall("\<(a) (href)\=\"\/(w)\/\S*\" (class)\=\"(new)\" (title)\=\"\"\>([^\"\>\<]*)\<\/(a)\>", conteudoWiki.decode("utf-8"))

# criando listas vazias para armazenas títulos de artigos externos e inexistentes
artigos_externos = []
artigos_inexistente = []

cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0

print("Exibindo os links do artigo: ")
print("LINKS 1")
for i in range(len(links1)):
    for j in range(len(links1[i])):
        if j == 8:
            cont1 += 1
            artigos_externos.append(links1[i][j])
            # print(links1[i][j])
if cont1 == 0:
    print("Não encontrei links que se encaixem com este formato")
else:
    print(f"Foram encontrados {cont1} links da categoria 1")
print()

print("LINKS 3")
for i in range (len(links3)):
    for j in range (len(links3[i])):
        if j == 5:
            cont3 += 1
            artigos_externos.append(links3[i][j])
            # print(links3[i][j])
if cont3 == 0:
    print("Não encontrei links que se encaixem com este formato")
else:
    print(f"Foram encontrados {cont3} links da categoria 3")
print()

print("LINKS 4")
for i in range (len(links4)):
    for j in range (len(links4[i])):
        # if j == 8:
        cont4 += 1
        artigos_inexistente.append(links4[i][j])
        print(links4[i][j])
if cont4 == 0:
    print("Não encontrei links que se encaixem com este formato")
else:
    print(f"Foram encontrados {cont4} links da categoria 4")
print()
print()

# transformando as listas vazias em conjuntos que permitem a impressão de valores únicos
ae = set(artigos_externos)
ai = set(artigos_inexistente)
# organizando em ordem alfabética :)
sorted_ae = sorted(ae)
sorted_ai = sorted(ai)

print(f"Exibindo {len(ae)} títulos de artigos externos:")
for externo in sorted_ae:
    print(f"◉ {externo}")
print()
print(f"Exibindo {len(ai)} títulos de artigos inexistentes:")
for inexistente in sorted_ai:
    print(f"◉ {inexistente}")
print()
print()

print("Fim do programa :D")
