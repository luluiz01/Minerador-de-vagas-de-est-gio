from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import time

url = 'https://www.apinfo.com/apinfo/inc/list4.cfm'
soup = BeautifulSoup(urlopen(url), "html.parser")

time.sleep(2)

print('\n\n Post \n\n')
# Faz a filtragem no site e retorna vagas de Brasilia
filtro = {"cod_cidade[]": 70000}
post_result = requests.post(url, filtro)
soup = BeautifulSoup(post_result.text, "html.parser")

print('-' * 82)

# busca a data e a cidade em que a vaga foi publicada
data = []
cidade = []
for item in soup.select('.info-data'):
    texto = item.get_text().strip().split()
    data.append(texto[-1])
    cidade.append(texto[0])

print(data)
print(cidade)

print('-' * 82)

# busca o título da vaga
titulo = []
for item in soup.select('.cargo'):
    texto = item.get_text().strip()
    titulo.append(texto)
print(titulo)

print('-' * 82)

# busca a descrição da vaga
descricao = []
empresas = []
cods = []
for item in soup.select('.texto'):
    texto = item.find_all('p')[0]
    descricao.append(texto)

    empresa_cod = item.find_all('p')[1]
    empresa = list(empresa_cod)[2].strip()
    empresas.append(empresa)
    cod = list(empresa_cod)[6].strip()
    cods.append(cod)
print(cods)
print('Depois do I')

for i, v in enumerate(descricao):
    print(f'{i + 1}º vaga')
    print(f'{v}', end='\n\n')
