# -*- coding: utf-8 -*-

from TppSyn import Parser
from llvmlite import ir
from sem import Semantica
from llvmlite import binding as llvm



# lc saida.ll
# vai te gerar um .s
# gcc -c saida.s -o file.o
# gcc file.o -o file



class Ger(object):
	"""docstring for Ger"""
	def __init__(self, codigo):
		self.codigo = codigo

		self.arvore = Parser(codigo).ast # obtém a arvore sintática
		self.semantica = Semantica(codigo) #instancia a semantica
		self.tabelaS = self.semantica.listaDeSimbolos # obtem a tabela de simbolos da semantica
		self.tabelaF = self.semantica.listaDeFuncoes # obtém a tabela de função da semantica

		
		self.listaVar =[]
		self.aux = []
		self.flag = 0

		# llvm.initialize()
		# llvm.initialize_native_asmprinter()
		# llvm.initialize_native_target()
		# target = llvm.Target.from_triple("x86_64-x86_64-linux-gnu")
		# target_machine = target.create_target_machine(codemodel='x86_64-x86_64-linux-gnu')
		# mod = llvm.parse_assembly('target triple = "x86_64-x86_64-linux-gnu"')


		self.module = ir.Module("modulo.bc") #cira um modulo
		self.arquivo = open('GenWar.ll', 'w') #abre um arquivo para saida em llvm intermediário	

		
		self.declaraVariavelGlobal(self.arvore)	# declaração de váriaveis global
		self.montaFuncao(self.arvore) #chama a função que monta as funções, tanto a main quanto as outras.

		self.arquivo.write(str(self.module))
		self.arquivo.close()
		print(self.module)




		
		for i in range (0, len(self.tabelaS)):
			#print self.tabelaS[i]
			pass

		for i in range(0, len(self.tabelaF)):
			#print self.tabelaF[i]
			pass


	def declaraVariavelGlobal(self, node):
		if node is not None: #se o nó for diferente de nulo
			if node.type == 'lista_declaracoes': # se o nó for lista de declaraçoes	
				if len(node.child) > 1: #se tiver mais de um filho, para não pegar declaração de função
					if node.child[1].child[0].type == 'declaracao_variaveis': # e o neto for declaração de variaveis 
						nodeAux = node.child[1].child[0]
						self.declaraVariavel(nodeAux, 0, "global") #passa o néto para declaração de variaveis zero para o builder e o escopo
						
				else:
					if node.child[0].child[0].type == 'declaracao_variaveis':
						nodeAux2 = node.child[0].child[0]
						self.declaraVariavel(nodeAux2, 0, "global")	#passa o néto para declaração de variaveis	zero para o builder e o escopo				

			for son in node.child:
				self.declaraVariavelGlobal(son)


	def montaFuncao(self, node):
		if node is not None: # se o node for difrente de nulo...
			if node.type == 'cabecalho': #se o no for cabeçalho ...
				for i in range(0,len(self.tabelaF)):	#percorre a tabela de função...					
					if node.value == self.tabelaF[i].nome: #se encontrar na tabela de função...

						args = [] #declara um array de argumentos
						if len(self.tabelaF[i].parametros) > 0: # se houver argumentos
							parametros = self.tabelaF[i].parametros # paramentos recebe uma tupla com tipo e variavel
							for x in range(0, len(parametros)): #itera sobre os parametros
								if parametros[x][0] == 'inteiro': #se for do tipo inteiro...
									args.append(ir.IntType(32)) # adiciona o tipo Int(32) nos args da função
								else: # se for difetente de inteiro (flutuante)...
									args.append(ir.FloatType()) # adiciona um tipo flutuante nos args da função														
							
						flag = 0 # flag para verificar tipo 0 = void, 1 = inteiro, 2 = flutuante
						if self.tabelaF[i].tipoRetorno == 'inteiro': # se o tipo retorno for inteiro...
							tipo_func = ir.FunctionType(ir.IntType(32), (args)) #adiciona o IntType(32) como retorno
							flag = 1							
						elif self.tabelaF[i].tipoRetorno == 'flutuante': # se for flutuante...
							tipo_func = ir.FunctionType(ir.FloatType(), (args)) #adiciona o FloatType como retorno.
							flag = 2

						else: #se nao...
							tipo_func = ir.FunctionType(ir.VoidType(), (args))# adiciona o VoidType como retorno.

						if self.tabelaF[i].nome != 'principal':
							func = ir.Function(self.module, tipo_func, name = self.tabelaF[i].nome) # criação da função, passando o cabeçao com tipo retorno + paramentros
						
						else:
							func = ir.Function(self.module, tipo_func, name = 'main')
						
						entry = func.append_basic_block('entrada_' + self.tabelaF[i].nome)# cria o bloco de entrada
						#corpo da função aqui, passar o node para outra função percorrer procurando por declarações...


						builder = ir.IRBuilder(entry) # Adiciona o bloco de entrada						
						
						if flag == 1: # se a flag == 1 (inteiro)
							zero = ir.Constant(ir.IntType(32), 0)
							retValor = builder.alloca(ir.IntType(32), name='retorno') #alloca retorno
							builder.store(zero,retValor) #inicializa com 0
						elif flag == 2: # se a flag == 2(flutuante)
							zero = ir.Constant(ir.FloatType(), 0)
							retValor = builder.alloca(ir.FloatType, name='retorno') #alloca retorno
							builder.store(zero,retValor)# atribui com 0.0


						self.declaraVariavel(node, builder, node.value) #chama a função que percorre variaveis, passando o nó cabeçalho e o builder

						self.atribuiValor(node, builder, node.value) #atribui valores a variaveis

						#self.leia(node)

						#self.escreva(node)

						#self. condicional(node)

						#self.laco(node)

						#self.chamadaFunc(node)


						exit = func.append_basic_block('saida_' + self.tabelaF[i].nome) # cria o bloco de saida
						builder.branch(exit)
						builder.position_at_end(exit)

						t_retValor = builder.load(retValor, name = 'retorno', align=4)
						builder.ret(t_retValor)



			for son in node.child: # for para iterar recursivamente na arvore
				self.montaFuncao(son)





#======================================================================================================================
	def declaraVariavel(self, node, builder, escopo): # função que faz declaração de variavel
		if node is not None: # se o node for diferente de nulo...	
			if node.type == 'declaracao_variaveis':	# se o tipo do nó for declaração de váriavel...			
				if node.child[0].type == 'inteiro': # se a declaração de variavel for de inteiros...
					tipo = ir.IntType(32) # criando uma variavel para i32			
					self.listaVariavel(node.child[1], tipo, builder, escopo) #chama função que percorre as variaveis da lista
				else: # se for flutuante
					tipo = ir.FloatType() # tipo recebe float
					self.listaVariavel(node.child[1], tipo, builder,escopo) # chama função que percorre as variaveis
			for son in node.child:
				self. declaraVariavel(son, builder, escopo)


	def listaVariavel(self, node, tipo, builder, escopo):
		if node is not None:
			if node.type == 'var' and builder == 0: # se encontrar um no do tipo var e o builder for zero, signigica que é var global
				var = ir.GlobalVariable(self.module, tipo, str(node.value)) # passa o tipo, e o nome da variavel				
				if str(tipo) == 'i32': # se o tipo for inteiro...					
					zero = int(0)
					var.initializer = ir.Constant(ir.IntType(32), zero)
				else: # se o tipo for float					
					zero = float(0)
					var.initializer = ir.Constant(ir.FloatType(), zero)

				var.linkage = "common"
				var.align = 4
				self.listaVar.append([var, escopo])

			if node.type == 'var' and builder != 0: # se encontrar um nó do tipo var e o builder for diferente de zero significa que é var de função					
				var = builder.alloca(tipo, name = node.value)	#declara a variavel com o tipo passado
				var.align = 4
				self.listaVar.append([var, escopo]) #adiciona a variavel em uma lista
				
			for son in node.child:
				self.listaVariavel(son, tipo, builder,escopo)


	def atribuiValor(self, node, builder, escopo): #atribuição de valor para variavel
		if node is not None:
			aux = []
			del aux[:]
			if node.type == 'atribuicao': # se o nó for atribuição
				self.flag = 0			
				self.getNum(node.child[1], aux)				
				if len(aux) == 3:
					for i in range(0, len(self.listaVar)):
						if node.child[0].value == self.listaVar[i][0].name and escopo == self.listaVar[i][1]: # se o filho a esquerda de atribuição estiver na lista de var(llvm) e o escopo for igual...
							resultado = self.listaVar[i][0] # load da váriavel a ser atribuido um valor...	
							
							for x in range(0, len(self.listaVar)):													
								if aux[1] == self.listaVar[x][0].name:									
									op1 = self.listaVar[x][0].name
									t_op1 = builder.load(self.listaVar[x][0], self.listaVar[x][0].name)
							else:
								try:
									op1 = int(aux[1])
									t_op1 = ir.Constant(ir.IntType(32), op1)
								except Exception:
									try:
										op1 = float(aux[1])
										t_op1 = ir.Constant(ir.FloatType(), op1)										
									except Exception as e:
										pass

							
							for x in range(0, len(self.listaVar)):													
								if aux[2] == self.listaVar[x][0].name:									
									op2 = self.listaVar[x][0].name
									t_op2 = builder.load(self.listaVar[x][0], self.listaVar[x][0].name)
							else:
								try:
									op2 = int(aux[2])
									t_op2 = ir.Constant(ir.IntType(32), op2)
								except Exception:
									try:
										op2 = float(aux[2])
										t_op2 = ir.Constant(ir.FloatType(), op2)											
									except Exception as e:
										pass
					

							if type(op1) == int:
								if aux[0] == '+':
									t_resultado = builder.add(t_op1, t_op2, name=resultado.name, flags=())
									builder.store(t_resultado, resultado)
									pass								

								elif aux[0] == '-':
									t_resultado = builder.sub(t_op1, t_op2, name=resultado.name, flags=())
									builder.store(t_resultado, resultado)
									pass

								elif aux[0] == '*':
									t_resultado = builder.mul(t_op1, t_op2, name=resultado.name, flags=())
									builder.store(t_resultado, resultado)
									pass

								elif aux[0] == '/':
									t_resultado = builder.udiv(t_op1, t_op2, name=resultado.name, flags=())
									builder.store(t_resultado, resultado)
									pass

							else:
								if aux[0] == '+':
									t_resultado = builder.fadd(t_op1, t_op2, name=resultado.name, flags=())
									builder.store(t_resultado, resultado)
									pass								

								elif aux[0] == '-':
									t_resultado = builder.fsub(t_op1, t_op2, name=resultado.name, flags=())
									builder.store(t_resultado, resultado)
									pass

								elif aux[0] == '*':
									t_resultado = builder.fmul(t_op1, t_op2, name=resultado.name, flags=())
									builder.store(t_resultado, resultado)
									pass

								elif aux[0] == '/':
									t_resultado = builder.fudiv(t_op1, t_op2, name=resultado.name, flags=())
									builder.store(t_resultado, resultado)
									pass


				elif len(aux) == 1:					
					for i in range(0, len(self.listaVar)):
						if node.child[0].value == self.listaVar[i][0].name and escopo == self.listaVar[i][1]: # se o filho a esquerda de atribuição estiver na lista de var(llvm) e o escopo for igual...
							resultado = self.listaVar[i][0] # load da váriavel a ser atribuido um valor...						pass
							for x in range(0, len(self.listaVar)):													
									if aux[0] == self.listaVar[x][0].name:									
										op1 = self.listaVar[x][0].name
										t_op1 = builder.load(self.listaVar[x][0], self.listaVar[x][0].name)
										builder.store(t_op1, resultado)

							
							try:
								op1 = int(aux[0])
								t_op1 = ir.Constant(ir.IntType(32), op1)
								builder.store(t_op1, resultado)
							except Exception:
								try:
									op1 = float(aux[0])
									t_op1 = ir.Constant(ir.FloatType(), op1)
									builder.store(t_op1, resultado)										
								except Exception as e:
									pass


			for son in node.child:
				self.atribuiValor(son, builder, escopo)


	def getNum(self, node, aux): # essa função deverá resolver as expressoes para retornar um valor para uma váriavel
		if node is not None:			
			if (node.type == 'expressao_multiplicativa' or node.type == 'expressao_aditiva') and len(node.child) == 3 and self.flag == 0: # se o nó for epxr multiplicativa ou expr aditiva e tiver tamnho maior que 1...				
				operador = node.child[1].value # operador é o nó do meio			
				numero1 = self.getValor(node.child[0]) #primeiro operando				
				numero2 = self.getValor(node.child[2]) #segundo operando				
				aux.append(operador)
				aux.append(numero1) #codigo escrito por matheus g
				aux.append(numero2)	
				self.flag = 1
			elif(node.type == 'fator' and node.child[0].type != 'chamada_funcao' and (node.child[0].type == 'var' or node.child[0].type == 'numero') and self.flag == 0 ):								
				numero = node.child[0].value
				aux.append(numero)
				self.flag = 2
			#elif tratar chamada de função
			

			for son in node.child:
				self.getNum(son, aux)


	def getValor(self, node):	
		while(node is not None):
			if node.type == 'var' or node.type == 'numero':
				return node.value
			else:
				node = node.child[0]

	

#=======================================================================================================================


		

if __name__ == '__main__':
	from sys import argv
	f = open(argv[1])
	x = Ger(f.read())