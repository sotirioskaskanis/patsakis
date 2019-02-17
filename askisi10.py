from bs4 import BeautifulSoup
import requests

link = input("")
selida = requests.get(link)
kodikas = BeautifulSoup(selida.text, 'lxml')

Grammes = 0
links = 0

links = len(html.find_all('a'))

Grammes = len(html.find_all('br')) + len(html.find_all('p'))

print(links)
print(Grammes)