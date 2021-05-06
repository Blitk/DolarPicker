from time import sleep
from bs4 import BeautifulSoup
from csv import DictWriter, DictReader
import requests
import datetime
import os



def Recupera():
	with open("dolar.csv") as arquivo:
		leitor = DictReader(arquivo)
		lista = []
		for linha in leitor:
			lista.append(linha)
		return lista


def Guarda(hora, data, dolar, dados):

	with open("dolar.csv", 'w') as arquivo:

		dados.append({"Valor em BRL":dolar, "Horario":hora, "Data": data})
		cabecalho = ["Valor em BRL", "Horario", "Data"]
		escritor = DictWriter(arquivo, fieldnames=cabecalho)
		escritor.writeheader()
		for item in dados:
			escritor.writerow(item)


def Carrega():
	with open("dolar.csv") as arquivo:
		leitor = DictReader(arquivo)
		lista = []
		for linha in leitor:
			lista.append(linha["Valor em BRL"])
		return lista



def Grafico(valores):
	frase = ''
	for x in valores:
		frase += " " + str(x)

	os.system(f'python3 Grafico.py {frase}')


print("\n\n")
url = "https://economia.uol.com.br/cotacoes/cambio/"


while True:
	dados = Recupera()
	hora = datetime.datetime.now()

	data = f"{hora.day}/{hora.month}/{hora.year}"
	horario = f"{hora.hour}:{hora.minute}"

	pagina = requests.get(url)
	crawler = BeautifulSoup(pagina.text, "html.parser")
	crawler = crawler.find_all("input")

	for item in crawler:
		if item.get("name") == "currency2":
			dolar = item.get('value').replace(',', '.')
			dolar = float(dolar)
			dolar = round(dolar, 2)

	print(f'Valor em BRL às \033[34m{horario}\033[0m:\033[32m R${dolar}\033[0m\n\n')
	Guarda(horario, data, dolar, dados)
	valores = Carrega()
	# Grafico(valores)
	sleep(900)


