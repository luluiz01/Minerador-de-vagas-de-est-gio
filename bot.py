import telepot as t
import json
# import pprint

# bot = t.Bot('937967716:AAGDEluEFsRLF_l8q77ZjmVaSU1HsfGtGrE')


# #bot com seu token como argumento
# def get_bot_info():
# 	return bot.getMe()

# #print(bot)
# #print(bot.getMe())

# #Retorna uma lista com as mensagens recebidas pelo bot
# def get_bot_update():
# 	bot.deleteWebhook()
# 	response = bot.getUpdates()
# 	return response

# #Envia uma mensaggem para o canal
# # def send_messege():
# # 	mensagem = bot.sendMessage(-1001188887351, "Fala aeee")
# # 	return mensagem


def send_messege():
    bot = t.Bot('937967716:AAGDEluEFsRLF_l8q77ZjmVaSU1HsfGtGrE')

    with open('vagas.json') as file_data:  #Abre o Json
        vagas = json.load(file_data)          # Atribui o dicionário a função vagas

        for code_vaga in vagas:
            vaga = vagas[code_vaga]

            message = '{}\n{}\n{} - {}\n{}\n{}'.format(
                vaga["Titulo"], vaga["Codigo"], vaga["Link"], vaga["Data"],
                vaga["Cidade"], vaga["Descricao"])
            #print(message)

            bot.sendMessage(-1001188887351, message)  # id do canal e objeto da mensagem 