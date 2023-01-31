#imports functions from helpers.py
from assets.helpers import top_news, all_news

print('##### NEWS API #####')

while True:
    choice = int(input("Escolha entre Top notícias e Todas as notícias.\n[1 - Top] [2 - Todas]: "))
    if choice == 1:
        break
    elif choice == 2:
        break
    else:
        print("Escolha inválida")

print("Insira as informações solicitadas abaixo")

country = input("País da notícia (br, us):*")
search = input("Pesquisa (Palavra ou Frase): ")
source = input("Fonte (globo, bbc, google-News): ")
category = input("Categoria (negocios, politica, geral): ")
print()

#function calling
if choice == 1:
    top_news(country, search = search)
elif choice == 2:
    all_news(search, language = 'pt')
