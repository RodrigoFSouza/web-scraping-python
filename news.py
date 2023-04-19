import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')
content = response.content
site = BeautifulSoup(content, 'html.parser')

noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
    link = titulo.get('href')

    if not (titulo.text == 'Vídeos curtos do g1'):
        if(subtitulo):
            lista_noticias.append([titulo.text, subtitulo.text, link])
        else:
            lista_noticias.append([titulo.text, '', link])

news = pd.DataFrame(lista_noticias, columns=['Titulo', 'Subtítulo', 'Link'])
news.to_excel('noticias.xlsx', index=False)
