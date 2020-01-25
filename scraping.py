import funcoes
import json

def pega_vagas(nome_arquivo):
  data = []
  cidade = []
  titulo = []
  link = []
  codigo = []
  descricao = []
  
  soup = funcoes.carrega_html(nome_arquivo)
  
  data.extend(funcoes.filtrarPelaData(soup))      
  cidade.extend(funcoes.filtrarPelaCidade(soup))
  titulo.extend(funcoes.filtrarPeloTitulo(soup))
  link.extend(funcoes.filtrarPeloLink(soup))
  codigo.extend(funcoes.filtrarPeloCodigo(soup))
  descricao.extend(funcoes.filtrarPelaDescricao(soup))

  vagas = {}

  for i in range(len(titulo) - 1):
    vagas_dict = {
      "Titulo": titulo[i],
      "Codigo": codigo[i],
      "Link": link[i],
      "Data": data[i],
      "Cidade": cidade[i],
      "Descricao": descricao[i]
    }
    #print(vagas_dict)
      
    vagas[codigo[i]] = vagas_dict
		
  return vagas

def vagas_to_dict(vagas_dict):
	with open('vagas.json', 'w') as json_file:
		json.dump(vagas_dict, json_file, ensure_ascii=False)
    

