from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

url = 'https://www.apinfo.com/apinfo/inc/list4.cfm'
soup = BeautifulSoup(urlopen(url), "html.parser")

print('\n\n Post \n\n')
# Faz a filtragem no site e retorna vagas de Brasilia
filtro = {"cod_cidade[]": 70000}
post_result = requests.post(url, filtro)
soup = BeautifulSoup(post_result.text, "html.parser")


def filtrarPelaData():
    data = []
    for item in soup.select('.info-data'):
        texto = item.get_text().strip().split()
        data.append(texto[-1])
    return print(data)


def filtrarPelaCidade():
    cidade = []
    for item in soup.select('.info-data'):
        texto = item.get_text().strip().split()
        cidade.append(texto[0])
    return print(cidade)


# busca o título da vaga
def filtrarPeloTitulo():
    titulo = []
    for item in soup.select('.cargo'):
        texto = item.get_text().strip()
        titulo.append(texto)
    return print(titulo)


def filtrarPeloLink():
    links = []
    for item in soup.select('.texto'):
        links.append(item.a.get('href'))
    return print(links)


def filtrarPeloCodigo():
    cods = []
    for item in soup.select('.texto'):
        empresa_cod = item.find_all('p')[1]
        cod = list(empresa_cod)[6].strip()
        cods.append(cod)
    return print(cods)


# obs: precisa melhorar a descrição
# busca a descrição da vaga
def filtrarPelaDescricao():
    descricao = []
    for item in soup.select('.texto'):
        texto = item.find_all('p')[0]
        descricao.append(texto)
    return print(descricao)
