#imports functions from helpers.py
from helpers import top_news, all_news

print('##### NEWS API #####')

while True:
    choice = int(input("Escolha entre Top notícias e Todas as notícias. \n [1 - Top] [2 - Todas]: "))
    if choice == 1:
        break
    elif choice == 2:
        break
    else:
        print("Escolha inválida")
        
print("Insira as informações solicitadas abaixo")

country = input("Insira o país da notícia (br, us): ")
search = input("Insira sua pesquisa (palavra ou frase): ")
source = input("Insira a fonte (globo, bbc, google-News): ")
category = input("Insira a categoria (business, general): ")
print()

#Function calling
if choice == 1:
    top_news(country, search = search)
elif choice == 2:
    all_news(search, language = 'pt')