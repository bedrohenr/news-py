#imports lib requests
import requests
#imports constants from config.py
from assets.config import URL_BASE_TOP_HEADLINES, URL_BASE_EVERYTHING, API_KEY

    # returns & for url or not
def paramCount(param_count):
    if param_count != 0:
        return '&'
    else:
        return ''

def getUrl(news_type, country, search, language):
    params = ''
    param_count = 0
    if country:
        params += paramCount(param_count)
        param_count += 1

        params += f"country={country}"

    if search:
        params += paramCount(param_count)
        param_count += 1

        params += f"q={search}"

    if language:
        params += paramCount(param_count)
        param_count += 1

        params += f"language={language}"

    params += paramCount(param_count)
    params += f"pageSize=20&apiKey={API_KEY}"

    url = ''
    if news_type == 1:
        url = f"{URL_BASE_TOP_HEADLINES}{params}"
    elif news_type == 2:
        url = f"{URL_BASE_EVERYTHING}{params}"

    return url

#shows the top news
def getNews(choice, country = None, search = None, language = None):
    """
    Returns the news of newsapi.org given user input parameters
    """

    url = getUrl(choice, country, search, language)

    #response in json using the lib requests
    response = requests.get(url).json()

    if not response['status'] or response['status'] != 'ok':

        print("Error. \nProgram exited.")
        if response['code'] == 'parametersMissing':
            msg = "Tente incluir mais parametros; Como pesquisa ou pais da noticia"
            print("Message: " + msg)
        exit()

    #accessing the articles in the json (response)
    articles = response['articles']

    #empty array to store the articles's details
    news = []

    #adding to the list via For loop (Title, Url, PublishedAt)
    for article in articles:
        news.append(
            f"{article['title']}\n\n"
            f"URL: {article['url']}\n\n"
            f"Publicado em: {article['publishedAt']}\n\n"
        )

    #returns the complete array
    output(country, search, news)
    return 0


def output(country, search, news):
        # Title
    if search:
        print(f"___ Top noticias sobre: {search.capitalize()} ___")
    elif country:
        print(f"___ Top noticias do pais: {country.upper()} ___")

    if news:
        for numero in range(len(news)):
            print(f"{numero + 1} - {news[numero]}")
    else:
        print("Nenhuma noticia encontrada.")
