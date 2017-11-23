# -*- coding: utf-8 -*-

from TppSyn import Parser

ret = 0


class Funcao():
	"""docstring for Funcao"""
	def __init__(self, tipoRetorno, nome, parametros):
		self.tipoRetorno = tipoRetorno
		self.nome = nome
		self.parametros = parametros
		self.utilizado = 0

	def __str__(self):
		return str(self.tipoRetorno) + ' ' + self.nome + ' ' + str(self.parametros) + ' ' + str(self.utilizado)



class Simbolo():
	def __init__(self, tipo, escopo, nome, dimensao):
		self.tipo = tipo
		self.escopo = escopo
		self.nome = nome
		self.dimensao = dimensao
		self.utilizado = 0

	def __str__(self):
		return self.escopo + ' ' + self.tipo + ' ' + self.nome + ' ' + str(self.dimensao) + ' ' + str(self.utilizado)



class Semantica():
	def __init__(self, codigo):
		self.listaDeSimbolos = []
		self.listaDeFuncoes = []		
		self.codigo = codigo
		self.arvore = Parser(codigo).ast
		self.addVarFunc()
		self.montarTabelaSimbolos(self.arvore)
		self.verificaPrincipal()
		self.verificaVarUtil()
			

		#for i in range (0, len(self.listaDeSimbolos)):
			#print self.listaDeSimbolos[i]

		#for i in range (0, len(self.listaDeFuncoes)):
			#print self.listaDeFuncoes[i]


	def montarTabelaSimbolos(self, node):
		if node is not None:
			if node.type == 'declaracao': # procurando por variaveis globais
				if node.child[0].type == 'declaracao_variaveis': # fugindo de nós de declaração_função p/ não pegar variaveis de funções
					aux = node.child[0].child[1]
					listaVar = percorreVariaveis(aux) #chama função que pega todas as variaveis
					tipo = node.child[0].child[0].type # obtém os tipos das variaveis
					flag = 0
					for i in range(0, len(listaVar)): #itera sobre a lista de variaveis retornadas
						simbolo = Simbolo(str(tipo), 'global', str(listaVar[i]), '0') #cria um obj simbolo, o ultimo parametro dimensão não foi tratado se é array ou nao
						
						for j in range (0, len(self.listaDeSimbolos)):
							if simbolo.nome == self.listaDeSimbolos[j].nome and simbolo.escopo == self.listaDeSimbolos[j].escopo:
								print 'ERRO1: Variável "' + simbolo.nome + '" já declarada no escopo global. A última declaração será desconsiderada.'
								flag = 1
						if flag == 0:
							self.listaDeSimbolos.append(simbolo) #add na lista de simbolos
					del listaVar[:]
				

			if node.type == 'declaracao_funcao': #procura o nó declaracão_função
				listaFunc  = (montaFuncao(node))			
			
				for i in range (0, len(listaFunc)):					
				 	flag = 0
					for j in range(0, len(self.listaDeFuncoes)):
						flag = 0
						if listaFunc[i].nome == self.listaDeFuncoes[j].nome:
			 				print 'ALERTA: função "'+ listaFunc[i].nome + '" já declarada! A segunda função declarada foi desconsiderada.'
							flag = 1							

				 	if flag == 0:
				 		self.listaDeFuncoes.append(listaFunc[i])

				del listaFunc[:]

			 	
				



			if node.type == 'cabecalho':
				escopo = node.value				
				listaVar = montaVar(node.child[1], escopo)
				#print 'a ser analisado ' + str(listaVar)			

				# if len(listaVar) < 2:
				# 	print listaVar					
				# 	escopo, tipo, listaVar1 = listaVar[0].split(' ')
				# 	listaVar1 = listaVar1.replace('[', '')
				# 	listaVar1 = listaVar1.replace(']', '')
				# 	listaVar1 = listaVar1.replace('\'', '')
				# 	simbolo = Simbolo(str(tipo), str(escopo), str(listaVar1), 0)
					
								
			
				# 	flag = 0
				# 	for i in range(0, len(self.listaDeSimbolos)):
				# 		if simbolo.nome == self.listaDeSimbolos[i].nome and self.listaDeSimbolos[i].escopo == 'global':
				# 			print 'ALERTA: Variável ja declarada no escopo global, a variavel "' + simbolo.nome + '" da função "' + simbolo.escopo + '" não será declarada!'
				# 			flag = 1
				# 		elif simbolo.nome == self.listaDeSimbolos[i].nome and simbolo.escopo == self.listaDeSimbolos[i].escopo:
				# 			print 'ALERTA: Variável ja declarada no escopo "' + simbolo.escopo + '", a variavel "' + simbolo.nome + '" da função "' + simbolo.escopo + '" não será declarada!'
				# 			flag = 1
				# 	if flag == 0:						
				# 		self.listaDeSimbolos.append(simbolo)
							
		   	#2 ou mais variaveis declaradas
		   		for i in range(0, len(listaVar)):
		   			listaVar1 = str(listaVar[i]).replace(', ', ',')
		   			#print listaVar1

		   			escopo = str(listaVar1).split(' ')[0]
		   			#print escopo
		   			tipo = str(listaVar1).split(' ')[1]
		   			#print tipo
		   			listaux = str(listaVar1.split(' ')[2])
		   		
		   			listaux = listaux.replace('[', '')
					listaux = listaux.replace(']', '')
					listaux = listaux.replace('\'', '')
					listaux2 =[]
					
					for i in range(0,len(listaux)):
						if listaux[i] != ',':
							listaux2.append(listaux[i])

					for i in range(0, len(listaux2)):
						flag = 0
						simbolo = Simbolo(str(tipo), str(escopo), str(listaux2[i]), 0)
						for j in range(0, len(self.listaDeSimbolos)):																
							if simbolo.nome == self.listaDeSimbolos[j].nome and simbolo.escopo == self.listaDeSimbolos[j].escopo:
								print 'ALERTA: Variável já declarada no escopo "'+ simbolo.escopo + '", a variavel "' + simbolo.nome + '" da função "' + simbolo.escopo + '" não será declarada!'
								flag = 1
							elif simbolo.nome == self.listaDeSimbolos[j].nome and self.listaDeSimbolos[j].escopo == 'global':
								print 'ALERTA: Variável ja declarada no escopo global, a variavel "' + simbolo.nome + '" da função "' + simbolo.escopo + '" não será declarada!'
								flag = 1
						if flag == 0:
							self.listaDeSimbolos.append(simbolo)
					del listaux2[:]
		   			
				del listaVar[:]


			if node.type == 'cabecalho':
				escopo = node.value
				self.verificaUtil(node,escopo )

			if node.type == 'cabecacalho':
				escopo = node.value
				self.verificaRet(node, escopo)



			for son in node.child:
				self.montarTabelaSimbolos(son)

	




	def addVarFunc(self):
		#print self.listaDeFuncoes[0]
		aux = ""
		lista = []
		lista2 =[]

		for i in range(0, len(self.listaDeFuncoes)):
			escopo = str(self.listaDeFuncoes[i]).split(' ')[1]
			aux = str(self.listaDeFuncoes[i]).split(' ')
			aux = str(aux).replace('[', '')
			aux = str(aux).replace(']', '')
			aux = str(aux).replace('"', '')
			aux = str(aux).replace('\'', '')
			aux = str(aux).replace(',', '')
			aux = aux.split(' ')
			#aux = str(aux[2:len(aux)-1])
			aux.pop(0)
			escopo = aux[0]
			
			aux.pop(0)
			aux.pop(len(aux)-1)
			i = 0
			while (i < len(aux)-1):
				tipo = aux[i]
				nome = aux[i+1]
				simbolo = Simbolo(tipo, escopo, nome, 0)
				self.listaDeSimbolos.append(simbolo)
				i = i +2

	def verificaPrincipal(self): #verifica se a função principal foi declarada
		flag = 0
		for i in range(0, len(self.listaDeFuncoes)):
			#print self.listaDeFuncoes[i]
			if self.listaDeFuncoes[i].nome == 'principal':
				flag = 1
				self.listaDeFuncoes[i].utilizado = 1
		if flag == 0:
			print 'ERRO: Função principal não declarada!'
			


	def verificaRet(self, node, escopo):
		if node is not None:
			if node.type is 'retorna':
				node = goTofolha(node)
				valor = node.value
				print valor

			for son in node.child:
				self.verificaRet(son)
		



	



	def verificaUtil(self, node, escopo):
		if node is not None:
			if node.type == 'atribuicao':
				nome = node.child[0].value
				for i in range(0, len(self.listaDeSimbolos)):					
					if self.listaDeSimbolos[i].nome == nome and self.listaDeSimbolos[i].escopo == 'global':
						self.listaDeSimbolos[i].utilizado = 1
					elif self.listaDeSimbolos[i].nome == nome and self.listaDeSimbolos[i].escopo == escopo:
						self.listaDeSimbolos[i].utilizado = 1				
					
				listAux = []			
				for i in range(0, len(self.listaDeSimbolos)):
					listAux.append(self.listaDeSimbolos[i].nome)						
				#print listAux
				if nome not in listAux:
					print 'ALERTA: Utilizando Variável "'+ nome + '" sem declaração.'

			for son in node.child:
				self.verificaUtil(son, escopo)

	def verificaVarUtil(self):
		for i in range(0, len(self.listaDeSimbolos)):		
			if self.listaDeSimbolos[i].utilizado == 0:
				print 'ALERTA: Variável "' + self.listaDeSimbolos[i].nome + '" da função "'+ self.listaDeSimbolos[i].escopo +'" declarada e não utilizada.'



def goTofolha(node):
	while (node is not None):
		node = node.child[0]

	return node

aux3 = []

aux1 = []

def montaVar(node, escopo):	
	if node is not None:
		if node.type == 'declaracao_variaveis':
			tipo = node.child[0].type
			listaVar1 = percorreVariaveis(node.child[1])
			aux1.append(escopo + ' ' + tipo + ' ' + str(listaVar1))	
			del listaVar1[:]

		for son in node.child:
			montaVar(son, escopo)

	for i in range(0, len(aux1)):		
		aux1[i].split(" ")

	return aux1


aux2 = []
def percorreVariaveis(node): #função que percore var, recebe um nó lista_parametros
	if node is not None:
		if node.type == 'var':
			aux2.append(str(node.value))
		for son in node.child:
			percorreVariaveis(son)
	
	return aux2



auxfunc = []
def montaFuncao(node): #função que itera sobre o nó declaracao_funcao
	if node.type == 'declaracao_funcao':
		if node.child[0].type == 'cabecalho':
			nomeFunc = node.child[0].value
			tipoRetorno = 'void'
			if node.child[0].child[0].child[0] is None: #se for nulo significa que a funcao não tem parametros
				parametro = 'vazio' #atribui vazio a parametro
				func = Funcao(str(tipoRetorno), str(nomeFunc), parametro)
				auxfunc.append(func)
			else:
				listaParametros = percorreParametros(parametros) #se for diferente de nulo significa que existe parametros, nesse caso é chamada uma outra função que itera sobre os parametros
				func = Funcao(str(tipoRetorno), str(nomeFunc), listaParametros)
				auxfunc.append(func)			

		else:
			tipoRetorno = node.child[0].type #pega o tipo do filho a esquerda
			nomeFunc = node.child[1].value #o valor do filho a direita
			parametros = node.child[1].child[0] # atribui a parametros o filho do filho a direita
			if parametros.child[0] is None: #se for nulo significa que a funcao não tem parametros
				parametro = 'vazio' #atribui vazio a parametro
				func = Funcao(str(tipoRetorno), str(nomeFunc), parametro)
				auxfunc.append(func)
			else:
				listaParametros = percorreParametros(parametros) #se for diferente de nulo significa que existe parametros, nesse caso é chamada uma outra função que itera sobre os parametros
				func = Funcao(str(tipoRetorno), str(nomeFunc), listaParametros)
				auxfunc.append(func)

		for son in node.child: #continua a iteração
			montaFuncao(son)
	return auxfunc


aux = []
def percorreParametros(node): #função que percore parametros, recebe um nó lista_parametros
	if node is not None:
		if node.type == 'parametro': # se encontrar um nó parametro
			aux.append(str(node.child[0].type) + ' ' + str(node.value)) #adiciona em uma lista
		for son in node.child:
			percorreParametros(son)
	return aux


if __name__ == '__main__':
	from sys import argv, exit
	f = open(argv[1])
	
	x = Semantica(f.read())

	#print 'fim da semantica'
