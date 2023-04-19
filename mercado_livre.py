import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_produtos = []
url_base = 'https://lista.mercadolivre.com.br/'

produto_pesquisado = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_pesquisado)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result shops__cardStyles ui-search-result--core andes-card--padding-default'})

for produto in produtos:
    nome = produto.find('h2', attrs={'class': 'ui-search-item__title shops__item-title'})
    link = produto.find('a', attrs={'class': 'ui-search-item__group__element shops__items-group-details ui-search-link'})
    preco = produto.find('span', attrs={'class': 'price-tag ui-search-price__part shops__price-part'}).find('span', attrs={'class': 'price-tag-fraction'})

    print("Titulo produto: ", nome.text)
    print("Link: ", link['href'])
    print("R$ ", preco.text)

    lista_produtos.append([nome.text, link['href'], "R$ " + preco.text])

dados = pd.DataFrame(lista_produtos, columns=['Nome', 'Link', 'Preco'])
dados.to_excel('produtos.xlsx', index=False)