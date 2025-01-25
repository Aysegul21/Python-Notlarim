import requests

from bs4 import BeautifulSoup

url =  "https://www.imdb.com/"

response = requests.get(url)

print(response)