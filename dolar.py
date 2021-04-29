from time import sleep
from bs4 import BeautifulSoup
from csv import DictWriter, DictReader
import requests
import datetime



def Recupera():
	with open("dolar.csv") as arquivo:
		leitor = DictReader(arquivo)
		lista = []
		for linha in leitor:
			lista.append(linha)
		return lista


def Guarda(data, dolar, dados):

	with open("dolar.csv", 'w') as arquivo:

		dados.append({"Valor em BRL":dolar, "Horario":data})
		cabecalho = ["Valor em BRL", "Horario"]
		escritor = DictWriter(arquivo, fieldnames=cabecalho)
		escritor.writeheader()
		for item in dados:
			escritor.writerow(item)



print("\n\n")
url = "https://economia.uol.com.br/cotacoes/cambio/"


while True:
	dados = Recupera()
	hora = datetime.datetime.now()
	data = f"{hora.hour}:{hora.minute} {hora.day}/{hora.month}/{hora.year}"
	pagina = requests.get(url)
	crawler = BeautifulSoup(pagina.text, "html.parser")
	crawler = crawler.find_all("input")

	for item in crawler:
		if item.get("name") == "currency2":
			dolar = "R$" + item.get('value')

	print(f'Valor em BRL às \033[34m{data.split(" ")[0]}\033[0m: \033[32m{dolar}\033[0m\n\n')
	Guarda(data, dolar, dados)
	sleep(900)

