from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import time
#import logging

url = 'https://www.apinfo.com/apinfo/inc/list4.cfm'
soup = BeautifulSoup(urlopen(url), "html.parser")
print("**********************************")

#busca o título da vaga
titulo = []
for item in soup.select('.cargo'):
  texto = item.get_text().strip()
  titulo.append(texto)
print(titulo)

print("**********************************")
#buca o link da vaga
links = []
for item in soup.select('.texto'):
  links.append(item.a.get('href'))
print(links)

#--

#url = "https://www.apinfo.com/apinfo/inc/list4.cfm"
time.sleep(5)
print('\n\n Post \n\n')
filtro = {"cod_cidade[]": 70000}
post_result = requests.post(url, filtro)
#get_result = requests.get(url)
#data = urlopen(url).read()
soup = BeautifulSoup(post_result.text, "html.parser")
print("**********************************")

#busca o título da vaga
titulo = []
for item in soup.select('.cargo'):
  texto = item.get_text().strip()
  titulo.append(texto)
print(titulo)

print("**********************************")
#buca o link da vaga
links = []
for item in soup.select('.texto'):
  links.append(item.a.get('href'))
print(links)
#print(post_result.text)
#print(data)