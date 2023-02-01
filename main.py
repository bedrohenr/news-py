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

    # País é um parametro aceitavel somente na escolha 1 (Top Noticias)
country = ''
if choice != 2:
    country = input("País da notícia* (br, us...): ")

language = input("Linguagem desejada(pt, en...): ")

print()

#function calling
getNews(choice, country, search, language)

