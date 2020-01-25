from bs4 import BeautifulSoup
import requests

def carrega_html(nome_arquivo):
	# file_name = "apinfo_pagina_1.html"
	with open(nome_arquivo, "r") as f:
		soup = BeautifulSoup(f.read(), "html.parser")

	return soup

def pega_pagina(url):
	# print('\n\n Post \n\n')
	# Faz a filtragem no site e retorna vagas de Brasilia
	# filtro = {"cod_cidade[]": 70000}
  filtro = {"estado[]": 'DF'}  
  post_result = requests.post(url, filtro)
  soup = BeautifulSoup(post_result.text, "html.parser")
  f = open("apinfo.txt", "w")
  f.write(str(soup))
  f.close()

  return soup


def filtrarPelaData(soup):
	data = []
	for item in soup.select('.info-data'):
			texto = item.get_text().strip().split()
			data.append(texto[-1])
	return data


def filtrarPelaCidade(soup):
    cidade = []
    for item in soup.select('.info-data'):
        texto = item.get_text().strip().split()
        cidade.append(texto[0])
    return cidade


# busca o título da vaga
def filtrarPeloTitulo(soup):
    titulo = []
    for item in soup.select('.cargo'):
        texto = item.get_text().strip()
        titulo.append(texto)
    return titulo


def filtrarPeloLink(soup):
    links = []
    for item in soup.select('.texto'):
        links.append(item.a.get('href'))
    return links


def filtrarPeloCodigo(soup):
    cods = []
    for item in soup.select('.texto'):
        #print('p:')
        #print(item.find_all('p'))
        empresa_cod = item.find_all('p')[1]
        #print(list(empresa_cod))
        cod = list(empresa_cod)[6].strip()
        cods.append(cod)
    return cods


# obs: precisa melhorar a descrição
# busca a descrição da vaga
#Funcao para buscar a Descricao da Vaga de emprego
def filtrarPelaDescricao(soup):
  #cria lista onde serão adicionados as descriçoes de cada vaga
  descricao = []
  #Percorre toda a entrada buscando a class .texto
  #onde inicia a informacoes sobre a vaga
  for item in soup.select('.texto'):
    text = ''
    #Recupera a primeiro paragrafo que é onde está a descrição
    texto = item.find_all('p')[0]
    #transforma o primeiro paragrafo em lista
    lis = list(texto)
    #percorre a lista
    for x in range(len(lis)):
      #verifica se o item na lista possue tag html
      #caso sim não inclui no texto para nao ocorrer #erro no Json
      if(lis[x].find("<") == -1 ):
        text = text + lis[x]
    #apos terminar o paragrafo, adiciona na lista
    descricao.append(text)
  return descricao