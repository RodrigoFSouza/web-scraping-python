from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get('https://www.flashscore.com/')

time.sleep(3)

navegador.find_element(By.ID, 'searchWindow').click()
inputSearch = navegador.find_element(By.XPATH, '//*[@id="search-window"]/div/div/div[2]/input')
inputSearch.send_keys('Champions League')

time.sleep(10000)

