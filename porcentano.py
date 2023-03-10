from datetime import datetime
from PIL import Image

#---------------------------- Pegando as datas
now = datetime.now()
dia = now.day
mes = now.month
ano = now.year
data = str(ano) + '-' + str(mes) + '-' + str(dia)

#verificar se o ano se passou
ano_atual = 0
arquivo = open('ano_atual.txt', 'r')
for a in arquivo:
	ano_atual = int(a)
arquivo.close()

if(ano_atual<=ano):
	arquivo = open('ano_atual.txt', 'w')
	arquivo.writelines(str(ano))
	ano_atual = ano
	arquivo.close()

#inicial
d1 = datetime.strptime(str(ano_atual-1)+'-12-31', '%Y-%m-%d')


#final
d2 = datetime.strptime(data, '%Y-%m-%d')

#---------------------------- fazendo a diferença
quantidade_dias = abs((d2 - d1).days)

#---------------------------- caso o ano seja bissesto
dias = 365
if(ano % 4 == 0):
	dias = 366
else:
	dias = 365
#---------------------------- caso o ano termine
if(quantidade_dias>dias):
	d1 = datetime.strptime(data, '%Y-%m-%d')

#---------------------------- calculando a porcentagem
porcentagem = (quantidade_dias*100)/dias
porcentagem = round(porcentagem,2)



#---------------------------- criando a imagem da barra de progresso
im = Image.new("RGB", (410, 100), "#FFFFFF")

im.paste((0,0,0),(10,10,400,90))

im.paste((255,255,255),(11,11,399,89))

im.paste((0,0,0),(21,21,dias+21,79))

im.paste((0,255,0),(21,21,quantidade_dias+21,79))


im.save("teste.png")

from TwitterAPI import TwitterAPI
import configparser

#---------------------------- lendo arquivo de configuração
config = configparser.ConfigParser()
config.read('config.ini')

api = TwitterAPI(consumer_key = config['twitter']['consumer_key'],
					consumer_secret = config['twitter']['consumer_secret'],
					access_token_key = config['twitter']['access_token_key'],
					access_token_secret = config['twitter']['access_token_secret'])

file = open('teste.png', 'rb')
imagem = file.read()


if(quantidade_dias==dias):
	api.request('statuses/update_with_media', {'status':str(ano)+" está "+str(porcentagem)+"%"+" completo!, Obrigado por seguir e tenha um ótimo "+str(ano+1)+"!"}, {'media[]':imagem})
else:
	api.request('statuses/update_with_media', {'status':str(ano)+" está "+str(porcentagem)+"%"+" completo."}, {'media[]':imagem})
