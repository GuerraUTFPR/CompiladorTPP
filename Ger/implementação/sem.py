# -*- coding: utf-8 -*-

from TppSyn import Parser
from llvmlite import ir



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


		#self.module = ir.Module("modulo.bc")



		self.tipoAjuda = ''
		self.escopo1 = ''
		self.tipoExp = ''
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
		self.verificaParam(self.arvore)
		self.verificaUtilFunc()
		self.atualizarSbtabela(self.arvore)
		self.verificaRet(self.arvore)
		self.verUtil(self.arvore)
		self.verificaExp(self.arvore)
		self.verificaVarUtil()

		#self.arquivo = open('GenWar.ll', 'w')

		#self.arquivo.write(str(self.module))
		#self.arquivo.close()
		#print(self.module)

		#return self.listaDeSimbolos




		for i in range(0, len(self.listaDeFuncoes)):
			#print self.listaDeFuncoes[i]
			pass

		for i in range (0, len(self.listaDeSimbolos)):
			#print self.listaDeSimbolos[i]
			pass


	def iterador(self, node):
		if node is not None:

			for son in node.child:
				iterador(son)


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

					#tipo_func = ir.FunctionType(ir.IntType(32), ())
					#func = ir.Function(self.module, tipo_func, name = funcao.nome)
					#entry = func.append_basic_block('entrada_' +funcao.nome)
					#exit = func.append_basic_block('saida_' + funcao.nome)

					#builder = ir.IRBuilder(entry)


				else:
					print 'ERRO: Função "' + funcao.nome + '" já declarada.' # erro de função declarada

			for son in node.child:
				self.montaFuncao(son)



	def alocaVarGlobal(self, node):
		if node is not None:
			if node.type == 'declaracao' and node.child[0].type != 'declaracao_funcao': #se o nó for declaração e não for declaração de função
				tipo = node.child[0].child[0].type #obtém o tipo do nó
				var = getVar(node.child[0].child[1],tipo) # obtém lista de declarações, passando lista_variaveis
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
				flag = 0
				for i in range(0, len(self.listaDeFuncoes)):
					if nome == self.listaDeFuncoes[i].nome:
						self.listaDeFuncoes[i].utilizado = 1
						flag = 1

				
				if flag == 0:
					print 'ERRO: Chamada de função não declarada.'

				if node.value == 'principal':
					print 'ERRO: Chamada para função principal.'

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


	def verificaRet2(self, node, tipo, escopo):
		if node is not None:
			if node.type == 'retorna':
				aux = node				
				while (aux.type != 'expressao_multiplicativa'):
					aux = aux.child[0]
				if len(aux.child) == 3:
					self.tipoExp = tipo								
					self.verificaExp2(aux, escopo)									
					if tipo != self.tipoExp:
						print 'Warning: Retorno da função "'+ escopo +'" é "' + self.tipoExp + '" o esperado é "' + tipo +'".'


			if node.type == 'retorna':
				aux = node
				while (aux.type != 'expressao_aditiva'):
					aux = aux.child[0]
				if len(aux.child) == 3:
					self.tipoExp = tipo
					self.verificaExp2(aux, escopo)
					if tipo != self.tipoExp:
						print 'Warning: Retorno da função "'+ escopo +'" é "' + self.tipoExp + '" o esperado é "' + tipo +'".'



			if node.type == 'retorna':
				aux = node
				flag = 0
				while (aux.type != 'fator' and flag == 0):
					if (aux.type == 'expressao_multiplicativa' or aux.type == 'expressao_aditiva') and len(aux.child) == 3:
						flag = 1
					else:
						aux = aux.child[0]

				if flag == 0:
					if aux.child[0].type == 'var':
						for i in range(0, len(self.listaDeSimbolos)):
							if escopo == self.listaDeSimbolos[i].escopo and aux.child[0].value == self.listaDeSimbolos[i].nome:
								self.listaDeSimbolos[i].utilizado = 1
								self.tipoAjuda = self.listaDeSimbolos[i].tipo

						if tipo != self.tipoAjuda:
							print 'Warning: Retorno da função "'+ escopo +'" é "' + self.tipoAjuda + '" o esperado é "' + tipo +'".'

					else:
						num = aux.child[0].value
						try:
							num = int(num)
							pass
						except Exception as e:
							num = float(num)

						
						if str(type(num))[7] != tipo[0]:
							print 'Warning: Retorno da função "' + escopo + '" é "' + str(type(num)) + '" o esperado é "' + tipo + '".'

			for son in node.child:
				self.verificaRet2(son, tipo, escopo)


	def verificaRet3(self, node):
		if node is not None:
			if node.type == 'retorna':
				self.flagRet = 1
			for son in node.child:
				self.verificaRet3(son)

			


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
			if node.type == 'fator':
				aux = node
				flag = 0
				if aux.child[0].type == 'var':
					var = aux.child[0].value
					flag = 1

				if aux.child[0].type == 'numero':
					flag = 0
					num = aux.child[0].value
					try:
						num = int(num)
						pass
					except Exception as e:
						num = float(num)

					if str(type(num))[7] == 'i':
						tipo = 'inteiro'
					else:
						tipo = 'flutuante'

				if flag == 1:
					flag2 = 0
					for i in range(0, len(self.listaDeSimbolos)):
						if var == self.listaDeSimbolos[i].nome and cabecalho == self.listaDeSimbolos[i].escopo:
							self.tipoAjuda = self.listaDeSimbolos[i].tipo
							self.listaDeSimbolos[i].utilizado = 1
						else:
							flag2 = 99
						

						for i in range(0, len(self.listaDeSimbolos)):
							if variavel == self.listaDeSimbolos[i].nome:
								tipovarRecebe = self.listaDeSimbolos[i].tipo

					if flag2 == 99:
						print 'Variavel "' + var +'" não declarada'
						pass

					elif tipovarRecebe != self.tipoAjuda:
						print'Atribuição com tipos dfirentes'






			# if node.type == 'fator' and node.child[0].type == 'numero' and nivel == 0: ## pega atribuição somente de numeros
			# 	for i in range(0, len(self.listaDeSimbolos)):				
			# 		if variavel == self.listaDeSimbolos[i].nome and cabecalho == self.listaDeSimbolos[i].escopo:
			# 			tipo = self.listaDeSimbolos[i].tipo						
			# 			try:
			# 				num = int(node.child[0].value)
			# 				pass
			# 			except Exception as e:
			# 				num = float(node.child[0].value)

			# 			if str(type(num))[7] == self.listaDeSimbolos[i].tipo[0]:
			# 				self.listaDeSimbolos[i].valor = num
			# 			else:
			# 				print 'Warning: Atrbuição de tipo incompatível.'


						
			# 	nivel = 0

			# elif node.type == 'fator' and node.child[0].type != 'numero': # caso a atribuição seja uma chamada de função
			# 	nivel = 1
				
			for son in node.child:
				self.atualizarSbtabela3(son, variavel, cabecalho, nivel)



	def verificaExp(self, node):
		if node is not None:
			if node.type == 'cabecalho':
				self.verificaExp2(node, node.value)

			for son in node.child:
				self.verificaExp(son)



	def verificaExp2(self, node, cabecalho):
		if node is not None:
			if node.type == 'expressao_multiplicativa' and len(node.child) == 3:
				operador = node.child[1].type # soma ou subtr
				op1 = node.child[0]
				op2 = node.child[2]
				while (op1.type != 'fator'):
					op1 = op1.child[0]

				tipoOp1 = ''	
				tipoOp2 = ''
				flag = 0
				if op1.child[0].type == 'var':
					var1 = op1.child[0].value

				else:
					num1 = op1.child[0].value
					try:
						num1 = int(num1)
						pass
					except Exception as e:
						num1 = float(num1)

					if str(tyep(num))[7] == 'i':
						tipoOp1 = 'inteiro'
					else:
						tipoOp1 = 'flutuante'



				while (op2.type != 'fator'):
					op2 = op2.child[0]				

				if op2.child[0].type == 'var':
					var2 = op2.child[0].value
					flag = 1

				else:
					flag = 0
					num2 = op2.child[0].value
					try:
						num2 = int(num2)
						pass
					except Exception as e:
						num2 = float(num2)

					if str(type(num2))[7] == 'i':
						tipoOp2 = 'inteiro'
					else:
						tipoOp2 = 'flutuante'					
				
				if flag == 1:				
					for i in range(0, len(self.listaDeSimbolos)):					
						if cabecalho == self.listaDeSimbolos[i].escopo and var1 == self.listaDeSimbolos[i].nome:
							self.listaDeSimbolos[i].utilizado = 1
							tipoOp1 = self.listaDeSimbolos[i].tipo

						if cabecalho == self.listaDeSimbolos[i].escopo and var2 == self.listaDeSimbolos[i].nome:
							self.listaDeSimbolos[i].utilizado = 1
							tipoOp2 = self.listaDeSimbolos[i].tipo

				if tipoOp1 != tipoOp2:
					self.tipoExp = 'inteiro'	
					print 'Warning: Na função "' + cabecalho + '" existe uma operação com tipos diferentes' #("' + var1 +'" é ' + tipoOp1 + ' e "' + var2 + '" é ' + tipoOp2 +').'
				else:
					self.tipoExp = tipoOp1


			elif node.type == 'expressao_aditiva' and len(node.child) == 3:
				operador = node.child[1].type # soma ou subtr
				op1 = node.child[0]
				op2 = node.child[2]
				while (op1.type != 'var'):
					op1 = op1.child[0]
				

				while (op2.type != 'var'):
					op2 = op2.child[0]
				
				
				tipoOp1 = ""				
				
				for i in range(0, len(self.listaDeSimbolos)):					
					if cabecalho == self.listaDeSimbolos[i].escopo and op1.value == self.listaDeSimbolos[i].nome:
						self.listaDeSimbolos[i].utilizado = 1
						tipoOp1 = self.listaDeSimbolos[i].tipo

					if cabecalho == self.listaDeSimbolos[i].escopo and op2.value == self.listaDeSimbolos[i].nome:
						self.listaDeSimbolos[i].utilizado = 1
						tipoOp2 = self.listaDeSimbolos[i].tipo

				if tipoOp1 != tipoOp2:
					self.tipoExp = 'inteiro'
					print 'Warning: Na função "' + cabecalho + '" existe uma operação com tipos diferentes("' + op1.value +'" é ' + tipoOp1 + ' e "' + op2.value + '" é ' + tipoOp2 +').'
				else:
					self.tipoExp = tipoOp1




			for son in node.child:
				self.verificaExp2(son, cabecalho)


	def verificaParam(self, node):
		if node is not None:
			if node.type == 'cabecalho':
				self.escopo1 = node.value
				
			if node.type == 'chamada_funcao':
				func = node.value
				arg = self.percorreArgs(node) 



			for son in node.child:
				self.verificaParam(son)


	def percorreArgs(self, node):
		if node is not None:
			if node.type == 'fator':
				flag = 0
				count = 0
				if node.child[0].type == 'var':
					var = node.child[0].value
					flag = 1					

				else:
					flag = 0
					num = node.child[0].value
					try:
						num = int(num)
						pass
					except Exception as e:
						num = float(num)

					if str(type(num))[7] == 'i':
						tipo = 'inteiro'
					else:
						tipo = 'flutuante'

				if flag == 1:
					tipo = ''
					flag2 = 0
					for i in range(0, len(self.listaDeSimbolos)):
						if self.escopo1 == self.listaDeSimbolos[i].escopo and var == self.listaDeSimbolos[i].nome:
							tipo = self.listaDeSimbolos[i].tipo
							self.listaDeSimbolos[i].utilizado = 1
							flag2 = 1

					if flag2 == 1:
						argumento = [tipo, var]

					else:
						print 'variavel não encotrada'
					flag3 = 0
					for i in range(0, len(self.listaDeFuncoes)):
						count = len(self.listaDeFuncoes[i].parametros)
						if len(self.listaDeFuncoes[i].parametros) > 0:
							if argumento[0] != self.listaDeFuncoes[i].parametros[0]:
								flag3 = 1
								count += 1								
							else:
								count -= 1
					
						if count != 0:
							print'Warnig: quantidade de arugmentos diferentes da quantide de parametros'

					if flag3 == 1:
						print 'Warning: argumentos com tipos diferentes'
						
			


			for son in node.child:
				self.percorreArgs(son)





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


def getVar(node, tipo):
	if node is not None:
		if node.type == 'var':
			if len(node.child) == 1:
				dimensao = 0
				dimensao = getIndice(node, dimensao)
			else:
				dimensao = 0

			erro = 0
			if len(node.child) == 1 and node.child[0].type == 'indice':
				aux = node
				while(aux.type != 'numero'):
					aux = aux.child[0]
				if aux.type == 'numero':
					try:
						num = int(aux.value)
						pass
					except Exception as e:
						num = float(aux.value)

					if str(type(num))[7] == 'f':
						print 'ERRO: Declaração de array com tamanho flutuante.'	
						erro = 1	


			if erro != 1:
				listVar.append([node.value, dimensao])
				dimensao = 0
				erro = 0


		for son in node.child:
			getVar(son, tipo)

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