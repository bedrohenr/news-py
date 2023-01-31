from os import getenv, path
from dotenv import load_dotenv
from pathlib import Path

# Setting the api key
if not path.exists('.env'): 
	print('No .env file located.\n Log in https://newsapi.org/, retrieve your key and insert it below.')
	key = input("Insert your newsapi's API key: ")

	file = open('./.env', 'w')
	file.write(f"ENV_API_KEY={key}")
	file.close()


env_path = Path('.env')
# Load env variable
load_dotenv(dotenv_path=env_path)

# Constants declaration 
API_KEY = getenv('ENV_API_KEY')
URL_BASE_TOP_HEADLINES = "https://newsapi.org/v2/top-headlines?"
URL_BASE_EVERYTHING = "https://newsapi.org/v2/everything?"


