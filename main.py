#imports functions from helpers.py
from assets.helpers import getNews

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

search = input("Pesquisa (Palavra ou Frase): ")

country = ''
if choice != 2:
    country = input("País da notícia* (br, us...): ")

language = input("Linguagem desejada(pt, eng...)")
category = input("Categoria negocios, politica, geral): ")
print()

#function calling
getNews(choice, country, category, search, language)

