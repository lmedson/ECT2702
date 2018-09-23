# Implementação Perceptron

import random

class Perceptron:

	def __init__(self, amostras, saidas, taxa_aprendizado=0.1, epocas=1000, limiar=-1):
		self.amostras = amostras
		self.saidas = saidas
		self.taxa_aprendizado = taxa_aprendizado
		self.epocas = epocas
		self.limiar = limiar
		self.n_amostras = len(amostras)
		self.n_atributos = len(amostras[0])
		self.pesos = []

	def treinar(self):

		for amostra in self.amostras:
			amostra.insert(0, -1)

		for i in range(self.n_atributos):
			self.pesos.append(random.random())

		self.pesos.insert(0, self.limiar)
		n_epocas = 0 # contador de épocas

		while True:

			erro = False # erro inicialmente inexiste

			for i in range(self.n_amostras):
				u = 0
				for j in range(self.n_atributos + 1):
					u += self.pesos[j] * self.amostras[i][j]
				y = self.sinal(u) # obtém a saída da rede

				# verifica se a saída da rede é diferente da saída desejada
				if y != self.saidas[i]:
					# calcula o erro
					erro_aux = self.saidas[i] - y
					# faz o ajuste dos pesos para cada elemento da amostra
					for j in range(self.n_atributos + 1):
						self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro_aux * self.amostras[i][j]
					erro = True # o erro ainda existe

			n_epocas += 1 # incrementa o número de épocas

			# critério de parada
			if not erro or n_epocas > self.epocas:
				break

	def teste(self, amostra):
		amostra.insert(0, -1)
		u = 0
		for i in range(self.n_atributos + 1):
			u += self.pesos[i] * amostra[i]
		y = self.sinal(u)
		print('Classe: %d' % y)

	def degrau(self, u):
		if u >= 0.7:
			return 1
		return 0

	def sinal(self, u):
		if u >= 0:
			return 1
		return -1



'''
Dada uma rede do tipo Perceptron formada por um neurônio com três terminais de entrada, 
utilizando pesos iniciais w0 = 0.4, w1 = -0.6 e w2 = 0.6, limiar θ = 0.5 e uma taxa de 
aprendizado = 0.4. Considere que o limiar será sempre multiplicado por -1. responda os itens abaixo:

a) Ensinar a rede a gerar a saída -1 para o padrão 001 e a saída +1 para os padrão 110; 
b) A que classe pertencem os padrões 111, 000, 100 e 011?

'''


amostras = [[0,0,1],[1,1,0]]
saidas = [-1,1]

padroes = [[1,1,1],[0,0,0],[1,0,0],[0,1,1]]

rede = Perceptron(amostras=amostras,saidas=saidas,taxa_aprendizado=0.4,limiar=0.5)
rede.treinar()

for i in range(len(padroes)):
	print(rede.teste((padroes[i])))