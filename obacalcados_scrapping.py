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

urls = {
        'bolsas': 'https://www.obacalcados.com.br/loja/catalogo.php?loja=875323&categoria=57&',
        'botas': 'https://www.obacalcados.com.br/loja/catalogo.php?loja=875323&categoria=59&',
        'tenis': 'https://www.obacalcados.com.br/loja/catalogo.php?loja=875323&categoria=77&',
        'rasteirinhas': 'https://www.obacalcados.com.br/loja/catalogo.php?loja=875323&categoria=71&',
        'saltos': 'https://www.obacalcados.com.br/loja/catalogo.php?loja=875323&categoria=73&',
        'sapatilhas': 'https://www.obacalcados.com.br/loja/catalogo.php?loja=875323&categoria=53&'
       }

info_produtos = []
keys_urls_list = list(urls.keys())
for key in keys_urls_list:
    url = urls.get(key)
    print(url)

    def scrapping(site, categoria):
        produtos = site.findAll('li', attrs={'class': 'page-catalog__item page-catalog__item--showcase'})

        for produto in produtos:
            nome = produto.find('h2', attrs={'class': 'product__name'})
            preco = produto.find('p', attrs={'class': 'product__price product__price--current'})
            link = produto.find('a', attrs={'class': 'product__link product__link--photo'})

            valor = preco.text.replace('R$', '').strip()
            info_produtos.append([nome.text, link['href'], categoria, valor])

    navegador.get(url + "pg=1")
    sleep(5)
    site = BeautifulSoup(navegador.page_source, 'html.parser')
    totalPages = site.find('span', attrs={'class': 'page-catalog__text page-catalog__text--paginate-count'})
    scrapping(site, key)
    for x in range(2, int(totalPages.text)):
        print(x)

    if (totalPages):
        for i in range(2, int(totalPages.text)):
            navegador.get(url + "pg=" + str(i))
            sleep(5)
            site = BeautifulSoup(navegador.page_source, 'html.parser')
            scrapping(site, key)

navegador.close()

data = pd.DataFrame(info_produtos, columns=['Produto', 'Link', 'Categoria', 'Preco'])
data.to_csv('obacalcados_botas.csv', index=False)