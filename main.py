#imports functions from helpers.py
from helpers import top_news, all_news

print('##### NEWS API #####')
print("Insira as informações solicitadas abaixo")

country = input("Insira o país da notícia (br, us): ")
search = input("Insira sua pesquisa (palavra ou frase): ")
source = input("Insira a fonte (globo, bbc, google-News): ")
category = input("Insira a categoria (business, general): ")
print()

#Function calling
#top_news(country, search = search)
all_news(search, language = 'pt')