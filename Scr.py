from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'https://resultados.as.com/resultados/futbol/primera/2020_2021/jornada/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Equipos
eq = soup.find_all('span', class_='nombre-equipo')
print(eq)

