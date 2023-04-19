import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
import pandas as pd
from selenium.webdriver.chrome.options import Options

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()

url = 'https://www.flashscore.com/'
navegador.get(url)

sleep(3)
acceptAll = navegador.find_element(By.ID, 'onetrust-accept-btn-handler')
acceptAll.click()

sleep(2)
brasilLink = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[22]/a')
brasilLink.click()

sleep(1)
serieALink = navegador.find_element(By.XPATH, '/html/body/div[4]/div[1]/div/div/aside/div/div[4]/div/div[22]/span[1]/a')
serieALink.click()

sleep(1)

site = BeautifulSoup(navegador.page_source, 'html.parser')

navegador.close()

times = site.findAll('div', attrs={'class': 'ui-table__row'})

dados_times = []
for time in times:
    rank = time.find('div', attrs={'class': 'tableCellRank'})
    nome = time.find('a', attrs={'class': 'tableCellParticipant__name'})

    dados = []
    valores = time.findAll('span', attrs={'class': 'table__cell table__cell--value'})
    for valor in valores:
        dados.append(valor.text)

    dados_times.append([rank.text.replace(".", ""), nome.text, dados[0], dados[1], dados[2], dados[3]])
    print()

data = pd.DataFrame(dados_times, columns=['Posicao', 'Equipe', 'Jogos', 'Vitórias', 'Empates', 'Derrotas'])
data.to_excel('brasileirao.xlsx', index=False)
