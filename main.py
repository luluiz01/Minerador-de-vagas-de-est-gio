import funcoes as f
import bot
import telepot
import pprint
import scraping as sc
#print(soup)

# url = 'https://www.apinfo.com/apinfo/inc/list4.cfm'
# soup = f.pega_pagina(url)
# print(soup)

minerar = True

if minerar:
	nome_arquivo = 'apinfo_pagina_1.html'
	soup = f.carrega_html(nome_arquivo)

	titulo = f.filtrarPeloTitulo(soup)
	#print(titulo)

	datas = f.filtrarPelaData(soup)
	#print(datas)

	cidade = f.filtrarPelaCidade(soup)
	#print(cidade)

	codigo = f.filtrarPeloCodigo(soup)
	#print(codigo)

	link = f.filtrarPeloLink(soup)
	#print(link)

	descricao = f.filtrarPelaDescricao(soup)
	#print(descricao)

#token = bot.get_bot_info()
#print(token)

#update = bot.get_bot_update()
#print(update)

#mensagem = bot.send_messege()

vagas = sc.pega_vagas(nome_arquivo)
print("-----------------------------------")
#print(vagas)

dicio = sc.vagas_to_dict(vagas)
print(dicio)

bot.send_messege()