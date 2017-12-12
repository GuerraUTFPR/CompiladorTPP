# -*- coding: utf-8 -*-

from TppSyn import Parser
from llvmlite import ir
from sem import Semantica


class Ger(object):
	"""docstring for Ger"""
	def __init__(self, codigo):
		self.codigo = codigo

		self.arvore = Parser(codigo).ast # obtém a arvore sintática
		self.semantica = Semantica(codigo) #instancia a semantica
		self.tabelaS = self.semantica.listaDeSimbolos # obtem a tabela de simbolos da semantica
		self.tabelaF = self.semantica.listaDeFuncoes # obtém a tabela de função da semantica

		self.listaVar =[]
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
						self.declaraVariavel(nodeAux, 0) #passa o néto para declaração de variaveis
						
				else:
					if node.child[0].child[0].type == 'declaracao_variaveis':
						nodeAux2 = node.child[0].child[0]
						self.declaraVariavel(nodeAux2, 0)	#passa o néto para declaração de variaveis					

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
							for i in range(0, len(parametros)): #itera sobre os parametros
								if parametros[i][0] == 'inteiro': #se for do tipo inteiro...
									args.append(ir.IntType(32)) # adiciona o tipo Int(32) nos args da função
								else: # se for difetente de inteiro (flutuante)...
									args.append(ir.FloatType()) # adiciona um tipo flutuante nos args da função														
									

						if self.tabelaF[i].tipoRetorno == 'inteiro': # se o tipo retorno for inteiro...
							tipo_func = ir.FunctionType(ir.IntType(32), (args)) #adiciona o IntType(32) como retorno
						elif self.tabelaF[i].tipoRetorno == 'flutuante': # se for flutuante...
							tipo_func = ir.FunctionType(ir.FloatType(), (args)) #adiciona o FloatType como retorno.
						else: #se nao...
							tipo_func = ir.FunctionType(ir.VoidType(), (args))# adiciona o VoidType como retorno.

						func = ir.Function(self.module, tipo_func, name = self.tabelaF[i].nome) # criação da função, passando o cabeçao com tipo retorno + paramentros
						
						entry = func.append_basic_block('entrada_' + self.tabelaF[i].nome)# cria o bloco de entrada
						#corpo da função aqui, passar o node para outra função percorrer procurando por declarações...
						exit = func.append_basic_block('saida_' + self.tabelaF[i].nome) # cria o bloco de saida

						builder = ir.IRBuilder(entry) # Adiciona o bloco de entrada

						self.declaraVariavel(node, builder) #chama a função que percorre variaveis, passando o nó cabeçalho e o builder

						self.atribuiValor(node, builder)

			for son in node.child: # for para iterar recursivamente na arvore
				self.montaFuncao(son)






#======================================================================================================================
	def declaraVariavel(self, node, builder): # função que faz declaração de variavel
		if node is not None: # se o node for diferente de nulo...	
			if node.type == 'declaracao_variaveis':	# se o tipo do nó for declaração de váriavel...			
				if node.child[0].type == 'inteiro': # se a declaração de variavel for de inteiros...
					tipo = ir.IntType(32) # criando uma variavel para i32			
					self.listaVariavel(node.child[1], tipo, builder) #chama função que percorre as variaveis da lista
				else: # se for flutuante
					tipo = ir.FloatType() # tipo recebe float
					self.listaVariavel(node.child[1], tipo, builder) # chama função que percorre as variaveis
			for son in node.child:
				self. declaraVariavel(son, builder)


	def listaVariavel(self, node, tipo, builder):
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
				self.listaVar.append(var)

			if node.type == 'var' and builder != 0: # se encontrar um nó do tipo var e o builder for diferente de zero significa que é var de função					
				var = builder.alloca(tipo, name = node.value)	#declara a variavel com o tipo passado
				var.align = 4
				self.listaVar.append(var)
				
			for son in node.child:
				self.listaVariavel(son, tipo, builder)



	def atribuiValor(self, node, builder):
		if node is not None:
			if node.type == 'atribuicao':
				pass

#=======================================================================================================================


		

if __name__ == '__main__':
	from sys import argv
	f = open(argv[1])
	x = Ger(f.read())