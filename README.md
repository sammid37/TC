# Web-Scrapper-Wikipedia
Projeto de final de período para a disciplina Teoria da Computação.
O intuito deste Web Scrapper é extrair informações da página do artigo utilizando expressões regulares, foi feito o uso de outras bibliotecas para filtrar esta busca dentro da página HTML.


# Requisitos do programa:
* Listar os tópicos do índice do artigo 
* Listar todos os nomes de arquivos de imagens presentes no artigo 
* ~~Listar todas as referências bibliográficas disponíveis na página(removido pelo professor)
* Listar todos os links para outros artigos da Wikipedia citados no conteúdo do artigo
## Outras funcionalidades
* Verifica se a URL digitada pertence ao domínio da Wikipedia
* A listagem de links externos está organizada por links existentes e inexistente(ou seja, não foi criada um artigo na wikipedia sobre o determinado assunto)

# Bibliotecas utilizadas
* re (regular expression)
* requests
* Beautiful Soup
