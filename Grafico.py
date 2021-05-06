import matplotlib.pyplot as pyplot
import sys
from csv import DictWriter, DictReader
from time import sleep

def Carrega():
	with open("dolar.csv") as arquivo:
		leitor = DictReader(arquivo)
		lista = []
		for linha in leitor:
			lista.append(linha["Valor em BRL"])
		return lista


valores = []

try:
	arg = sys.argv[1: -1]
	for x in arg:
		valores.append(float(x))

except:
	pass

else:
	valores = Carrega()
	pyplot.plot(valores)
	pyplot.show()

