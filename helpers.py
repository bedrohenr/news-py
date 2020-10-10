#Imports lib requests
import requests
#Imports constants from config.py
from config import URL_BASE_TOP_HEADLINES, URL_BASE_EVERYTHING, API_KEY

def top_news(country, source = None, category = None, search = None):
    """
    Retorna as top notícias do dia
    """
    #Variable checking (if exists)
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

