# -*- coding: utf-8 -*-

from TppSyn import Parser



class Funcao():
	"""docstring for Funcao"""
	def __init__(self, tipoRetorno, nome, parametros):
		self.tipoRetorno = tipoRetorno
		self.nome = nome
		self.parametros = parametros
		self.utilizado = 0

	def __str__(self):
		return str(self.tipoRetorno) + ' ' + str(self.nome) + ' ' + str(self.parametros) + ' ' + str(self.utilizado)



class Simbolo():
	def __init__(self, tipo, escopo, nome, dimensao):
		self.tipo = tipo
		self.escopo = escopo
		self.nome = nome
		self.dimensao = dimensao
		self.utilizado = 0
		self.tamanho = 0
		self.valor = 0

	def __str__(self):
		return self.escopo + ' ' + self.tipo + ' ' + self.nome + ' ' + ' ' + str(self.valor)+ ' '+ str(self.dimensao) + ' ' + str(self.utilizado)



class Semantica():
	def __init__(self, codigo):
		self.flagRet = 0
		self.listaDeSimbolos = []
		self.listaDeFuncoes = []
		self.count = 0
		self.codigo = codigo
		self.arvore = Parser(codigo).ast
		self.montaFuncao(self.arvore)
		self.alocaVarFunc()
		self.alocaVarGlobal(self.arvore)
		self.alocaVarLocal(self.arvore)
		self.verificaPrincipal()
		self.verificaChamadaFunc(self.arvore)
		self.verificaUtilFunc()
		#self.verificaRet(self.arvore)
		self.verUtil(self.arvore)
		self.verificaVarUtil()
		self.atualizarSbtabela(self.arvore)


		for i in range(0, len(self.listaDeFuncoes)):
			#print self.listaDeFuncoes[i]
			pass

		for i in range (0, len(self.listaDeSimbolos)):
			print self.listaDeSimbolos[i]
			pass


	def montaFuncao(self, node):
		if node is not None:
			if node.type == 'declaracao_funcao': #se o nó for declaração de função
				if len(node.child) == 2: #caso a função tenha tipo de retorno
					tipoRetorno = node.child[0].type
					nome = node.child[1].value
					if node.child[1].child[0].child[0] is not None: #se houver parametros
						parametros = getParametro(node)
					else:
						parametros = []
				else:
					tipoRetorno = 'vazio' # se não houver tipo de retorno
					nome = node.child[0].value
					if node.child[0].child[0].child[0] is not None: # se houver parametros
						parametros = getParametro(node)
					else:
						parametros = []

				funcao = Funcao(tipoRetorno, nome, parametros) #cria um obj função

				flag = 0
				for i in range(0, len(self.listaDeFuncoes)): # percorre a lista de função
					if funcao.nome == self.listaDeFuncoes[i].nome: #caso exista uma função já declarada com o mesmo nome
						flag = 1

				if flag == 0:
					self.listaDeFuncoes.append(funcao)
				else:
					print 'ERRO: Função "' + funcao.nome + '" já declarada.' # erro de função declarada

			for son in node.child:
				self.montaFuncao(son)



	def alocaVarGlobal(self, node):
		if node is not None:
			if node.type == 'declaracao' and node.child[0].type != 'declaracao_funcao': #se o nó for declaração e não for declaração de função
				tipo = node.child[0].child[0].type #obtém o tipo do nó
				var = getVar(node.child[0].child[1]) # obtém lista de declarações, passando lista_variaveis
				listVar = [tipo, var] #adciona a tupla tipo + variaveis
				
				for i in range(1, len(listVar)):
					for j in range(0, len(listVar[i])):
						variavel = Simbolo(listVar[0], 'global', listVar[1][j][0], listVar[1][j][1])
						flag = 0
						for k in range(0, len(self.listaDeSimbolos)):
							if variavel.nome == self.listaDeSimbolos[0].nome: #verifica se ja tem alguma váriavel declarada
								flag = 1

						if flag == 0:
							self.listaDeSimbolos.append(variavel)

						else:
							print 'ERRO: Variável "' + variavel.nome + '" já declarada'

				del var[:]
			for son in node.child:
				self.alocaVarGlobal(son)



	def alocaVarLocal(self, node):
		if node is not None:
			if node.type == 'cabecalho':							
				self.getVarLocal(node.child[1], node.value)	
							
			for son in node.child:
				self.alocaVarLocal(son)



	def getVarLocal(self, node, escopo):	
		if node is not None:
			if node.type == 'declaracao_variaveis':			
				tipo = node.child[0].type				
				self.getVar2(node.child[1], tipo, escopo)	

			for son in node.child:			
				self.getVarLocal(son, escopo)



	def getVar2(self, node, tipo, escopo):
		
		if node is not None:
			if node.type == 'var':
				if len(node.child) == 1:
					dimensao = 0
					dimensao = getIndice2(node, dimensao)
				else:
					dimensao = 0

				flag = 0
				simbolo = Simbolo(tipo, escopo, node.value, dimensao)
				#print simbolo.escopo
				for i in range(0, len(self.listaDeSimbolos)):					
					if simbolo.nome == self.listaDeSimbolos[i].nome and simbolo.escopo == self.listaDeSimbolos[i].escopo:
						flag = 1

				if flag == 0:
					self.listaDeSimbolos.append(simbolo)
				else:
					print 'ERRO: Variável "' + simbolo.nome + '" já declarada na função "' + simbolo.escopo + '".'
					
				
			for son in node.child:
				self.getVar2(son, tipo, escopo)	



	def getIndice2(node, count):
		while(node.child[0].type == 'indice'):
			count += 1
			node = node.child[0]
		return count


	def verificaPrincipal(self): #verifica se a função principal foi declarada
		flag = 0
		for i in range(0, len(self.listaDeFuncoes)):
			if self.listaDeFuncoes[i].nome == 'principal':
				flag = 1
				self.listaDeFuncoes[i].utilizado = 1
		if flag == 0:
			print 'ERRO: Função principal não declarada!'



	def alocaVarFunc(self):
		for i in range(0, len(self.listaDeFuncoes)):
			for j in range(0, len(self.listaDeFuncoes[i].parametros) ):
				simbolo = Simbolo(self.listaDeFuncoes[i].parametros[j][0] ,self.listaDeFuncoes[i].nome, self.listaDeFuncoes[i].parametros[j][1], 0)
				flag = 0
				for i in range(0, len(self.listaDeSimbolos)):					
					if simbolo.nome == self.listaDeSimbolos[i].nome and simbolo.escopo == self.listaDeSimbolos[i].escopo:
						flag = 1

				if flag == 0:
					simbolo.utilizado = 1
					self.listaDeSimbolos.append(simbolo)
				else:
					print 'ERRO: Variável "' + simbolo.nome + '" já declarada na função "' + simbolo.escopo + '".'



	def verificaChamadaFunc(self, node): ##verificar se os parametros está correto
		if node is not None:
			if node.type == 'chamada_funcao':
				nome = node.value
				for i in range(0, len(self.listaDeFuncoes)):
					if nome == self.listaDeFuncoes[i].nome:
						self.listaDeFuncoes[i].utilizado = 1

			for son in node.child:
				self.verificaChamadaFunc(son)
	

	def verificaUtilFunc(self):
		for i in range(0, len(self.listaDeFuncoes)):
			if self.listaDeFuncoes[i].utilizado == 0:
				print 'AVISO: Função "' + self.listaDeFuncoes[i].nome + '" declarada e não utilizada.'
			



	def verificaRet(self, node):
		if node is not None:
			if node.type == 'declaracao_funcao':				
				if node.child[0].type == 'flutuante' or node.child[0].type == 'inteiro':					
					self.verificaRet2(node, node.child[0].type, node.child[1].value)

					self.verificaRet3(node.child[1])

					if self.flagRet != 1:
						print 'ERRO: Função "'+node.child[1].value + '" sem retorno'

					self.flagRet = 0
					
			for son in node.child:
				self.verificaRet(son)

	def verificaRet3(self, node):
		if node is not None:
			if node.type == 'retorna':
				self.flagRet = 1
			for son in node.child:
				self.verificaRet3(son)

			


	def verificaRet2(self, node, tipo, escopo):
		if node is not None:
			if node.type == 'retorna':
				while (node.type != 'fator'):
					node = node.child[0]

				num =  node.child[0].value

				flag = 0
				## erro para expressoes
				for i in range(0, len(num)):
					if num[i] == '.':
						flag = 1
				
				if flag == 1:
					num = float(num)
				else:
					num = int(num)

				#print tipo

				if tipo == 'inteiro':
					aux = 'int'
				elif tipo == 'flutuante':
					aux = 'float'

				#print aux
				teste = str(type(num))
				
				if teste[7] == 'i':
					aux2 = 'int'
				else:
					aux2 = 'float'


				if aux2 != aux:
					print 'AVISO: retorno da funcao "'+escopo+'" com tipo incompativel.'
		

			for son in node.child:
				self.verificaRet2(son, tipo, escopo)



	def verUtil(self, node):
		if node is not None:
			if node.type == 'cabecalho':
				escopo = node.value
				self.verificaUtil(node,escopo)
			for son in node.child:
				self.verUtil(son)


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




	def atualizarSbtabela(self, node):
		if node is not None:
			if node.type == 'cabecalho':
				self.atualizarSbtabela2(node, node.value)

			for son in node.child:
				self.atualizarSbtabela(son)

	def atualizarSbtabela2(self, node, cabecalho):
		if node is not None:			
			if node.type == 'atribuicao':
				variavel = node.child[0].value			
				self.atualizarSbtabela3(node.child[1], variavel, cabecalho, 0)

			for son in node.child:
				self.atualizarSbtabela2(son, cabecalho)


	def atualizarSbtabela3(self, node, variavel, cabecalho, nivel):
		if node is not None:			
			if node.type == 'fator' and node.child[0].type == 'numero' and nivel == 0: ## pega atribuição somente de numeros
				for i in range(0, len(self.listaDeSimbolos)):				
					if variavel == self.listaDeSimbolos[i].nome and cabecalho == self.listaDeSimbolos[i].escopo:
						tipo = self.listaDeSimbolos[i].tipo						
						try:
							num = int(node.child[0].value)
							pass
						except Exception as e:
							num = float(node.child[0].value)

						if str(type(num))[7] == self.listaDeSimbolos[i].tipo[0]:

							self.listaDeSimbolos[i].valor = num
						else:
							print 'Warning: Atrbuição de tipo incompatível.'
							

						
				nivel = 0

			elif node.type == 'fator' and node.child[0].type != 'numero': # caso a atribuição seja uma chamada de função
				nivel = 1
				
			for son in node.child:
				self.atualizarSbtabela3(son, variavel, cabecalho, nivel)




##########################################################################


paramList = []


def getParametro(node):
	if node is not None:
		if node.type == 'parametro':
			nome = node.value
			tipo = node.child[0].type
			paramList.append([tipo, nome])

		for son in node.child:
			getParametro(son)

	return paramList


listVar = []


def getVar(node):
	if node is not None:
		if node.type == 'var':
			if len(node.child) == 1:
				dimensao = 0
				dimensao = getIndice(node, dimensao)
			else:
				dimensao = 0

			
			listVar.append([node.value, dimensao])
			dimensao = 0

		for son in node.child:
			getVar(son)

	return listVar


def getNum(node):
	if node is not None:
		if node.type == 'fator':
			numero = node.child[0].value
			return numero
		
		for son in node.child:
			getNum(son)


def getIndice(node, count):
	while(node.child[0].type == 'indice'):
		count += 1
		node = node.child[0]
	return count

##########################################################################


if __name__ == '__main__':
	from sys import argv
	f = open(argv[1])
	x = Semantica(f.read())