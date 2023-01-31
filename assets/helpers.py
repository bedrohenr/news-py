#imports lib requests
import requests
#imports constants from config.py
from assets.config import URL_BASE_TOP_HEADLINES, URL_BASE_EVERYTHING, API_KEY

#shows the top news
def top_news(country, source = None, category = None, search = None):
    """
    Returns the top news of newsapi.org
    """
    #variable checking (if exists)
    if source:
        url = f"{URL_BASE_TOP_HEADLINES}sources={source}&apiKey={API_KEY}"
    elif category:
        url = f"{URL_BASE_TOP_HEADLINES}country={country}&category={category}&apiKey={API_KEY}"
    elif search:
        url = f"{URL_BASE_TOP_HEADLINES}country={country}&q={search}&apiKey={API_KEY}"
    else:
        url = f"{URL_BASE_TOP_HEADLINES}country={country}&apiKey={API_KEY}"

    #response in json using the lib requests
    response = requests.get(url).json()

    #accessing the articles in the json (response)
    articles = response['articles']

    #empty array to store the articles's details
    top_news = []

    #adding to the list via For loop (Title, Url, PublishedAt)
    for article in articles:
        top_news.append(
            f"{article['title']}\n"
            f"URL: {article['url']}\n"
            f"Publicado em: {article['publishedAt']}\n"
        )

    #returns the complete array
    output_top(country, top_news)
    return 0

#shows all the news
def all_news(search, language = None):
    """
    Returns all news from newsapi.org
    """

    #creates empty array
    all_news = []

    if search:
        if language:
            url = f"{URL_BASE_EVERYTHING}q={search}&language={language}&apiKey={API_KEY}"

        #response in json using the lib requests
        response = requests.get(url).json()

        #accessing the articles in the json (response)
        articles = response['articles']

        #adding to the list via For loop (Title, Url, PublishedAt)
        for article in articles:
            all_news.append(
                f"{article['title']}\n\n"
                f"URL: {article['url']}\n\n"
                f"Publicado em: {article['publishedAt']}\n\n"
            )

    #returns the complete array
    output_top(search, all_news)
    return all_news

#returns the output of the top news
def output_top(country, news):
    print(f"___ Top noticias do pais: {country.upper()} ___")
    if news:
        for numero in range(len(news)):
            print(f"{numero + 1} - {news[numero]}")
    else:
        print("Nenhuma noticia encontrada.")

#returns the output of the news
def output_all(search, news):
    print(f"___ Todas noticias sobre: {search.title()} ___")
    if news:
        for numero in range(len(news)):
            print(f"{numero + 1} - {news[numero]}")
    else:
        print("Nenhuma noticia encontrada.")
