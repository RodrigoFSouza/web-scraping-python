import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.chrome.options import Options

options = Options()
#options.add_argument('--headless') # nao abre o navegador
#options.add_argument('window-size=600,800')


servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico, options=options)

navegador.get('https://www.airbnb.com')
sleep(5)
elemento = navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div/div/div[1]/div/div/div/header/div/div[2]/div[1]/div/button[1]')
elemento.submit()
#input_onde = navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div[1]/div/div[2]/div/div/div/div/div/div[1]/div/div/div/header/div/div[2]/div[2]/div/div/div/form/div[2]/div/div[1]/div/label/div/input')
#input_onde.send_keys('São Paulo')
#input_onde.submit()


#site = BeautifulSoup(navegador.page_source, 'html.parser')

#print(site.prettify())
sleep(1000)
